#!/usr/bin/env python3
"""
EthCC[9] Transcription Pipeline
Downloads audio from YouTube playlists and transcribes via GPT-4o-mini-transcribe.
Cost: ~$20 for all 308 talks (~$0.003/min)
"""

import os
import sys
import json
import re
import subprocess
import time
import math
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI

# ── Config ──────────────────────────────────────────────────────────────────

PLAYLISTS = {
    "monroe":  "PLfc9R9NWDYvIXQYIIjlQrs9Z7zsCJc2J_",
    "redford": "PLM-Xjhvin-uUY01s84QzYhL35KQQUos44",
    "kelly":   "PL-owlDp9BBavKDDJOpsTAupQhlfaLwYJl",
    "hepburn": "PLhM7rBgpVV-IzjnT4umBqI7WGVLvKQFYw",
    "burton":  "PLUt355rCCNrSi56eo6hDn3s6Ufzn1-zqH",
    "taylor":  "PLqL60kqgLPBA41jhJIBl2sZU6jI-DvCW4",
    "chaplin": "PLSJ8gU1sECuxvjRql4KaDaqqYB1F7qsFu",
}

ROOT = Path(__file__).resolve().parent.parent
AUDIO_DIR = ROOT / "audio"
TRANSCRIPTS_DIR = ROOT / "transcripts"
MAX_FILE_SIZE = 24 * 1024 * 1024  # 24MB (safety margin under 25MB limit)
MAX_WORKERS = 4  # parallel transcription threads
MODEL = "gpt-4o-mini-transcribe"

# Find yt-dlp and ffmpeg executables (Windows PATH may not include pip Scripts)
import shutil
YTDLP = shutil.which("yt-dlp") or str(Path.home() / "AppData/Roaming/Python/Python313/Scripts/yt-dlp.exe")
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

client = OpenAI()  # uses OPENAI_API_KEY env var


# ── Helpers ─────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:80].strip('-')


def parse_title(raw_title: str) -> dict:
    """Parse YouTube title like 'Speaker (Org) - Talk Title' into components."""
    # Remove common suffixes
    raw_title = re.sub(r'\s*\|.*$', '', raw_title)
    raw_title = raw_title.strip()

    # Try pattern: "Speaker (Org) - Title"
    m = re.match(r'^(.+?)\s*\(([^)]+)\)\s*[-–—]\s*(.+)$', raw_title)
    if m:
        return {
            "speaker": m.group(1).strip(),
            "organization": m.group(2).strip(),
            "title": m.group(3).strip(),
        }

    # Try pattern: "Speaker (Org), Speaker2 (Org2) - Title"
    m = re.match(r'^(.+?)\s*[-–—]\s*(.+)$', raw_title)
    if m:
        speaker_part = m.group(1).strip()
        title_part = m.group(2).strip()
        # Extract orgs from speaker part
        orgs = re.findall(r'\(([^)]+)\)', speaker_part)
        speaker_clean = re.sub(r'\s*\([^)]*\)\s*', ' ', speaker_part).strip()
        speaker_clean = re.sub(r'\s*,\s*', ', ', speaker_clean).strip(', ')
        return {
            "speaker": speaker_clean,
            "organization": ", ".join(orgs) if orgs else "",
            "title": title_part,
        }

    # Fallback: whole thing is the title
    return {
        "speaker": "",
        "organization": "",
        "title": raw_title,
    }


def get_playlist_videos(playlist_id: str) -> list[dict]:
    """Get video metadata from a YouTube playlist using yt-dlp."""
    cmd = [
        YTDLP,
        "--flat-playlist",
        "--print", "%(id)s\t%(title)s\t%(duration)s",
        "--no-warnings",
        f"https://www.youtube.com/playlist?list={playlist_id}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    videos = []
    for line in result.stdout.strip().split('\n'):
        if not line.strip():
            continue
        parts = line.split('\t')
        if len(parts) >= 2:
            vid_id = parts[0]
            title = parts[1]
            duration = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0
            # Skip non-talk entries (YouTube UI artifacts)
            if any(skip in title.lower() for skip in [
                'tastenkombinationen', 'wiedergabe', 'allgemein',
                'untertitel', 'sphärische', 'beschreibung'
            ]):
                continue
            videos.append({
                "id": vid_id,
                "title": title,
                "duration": duration,
            })
    return videos


def download_audio(video_id: str, output_path: Path) -> Path:
    """Download audio from YouTube video using yt-dlp."""
    output_template = str(output_path)
    cmd = [
        YTDLP,
        "-x",  # extract audio
        "--audio-format", "mp3",
        "--audio-quality", "5",  # medium quality, smaller files
        "-o", output_template,
        "--no-warnings",
        "--no-playlist",
        f"https://www.youtube.com/watch?v={video_id}",
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    # yt-dlp may add extension
    mp3_path = output_path.with_suffix('.mp3')
    if mp3_path.exists():
        return mp3_path
    # Check without extension changes
    for ext in ['.mp3', '.m4a', '.webm', '.opus']:
        p = output_path.with_suffix(ext)
        if p.exists():
            return p
    return mp3_path


def get_audio_duration(audio_path: Path) -> int:
    """Get audio duration in seconds using ffmpeg."""
    cmd = [FFMPEG, "-i", str(audio_path), "-f", "null", "-"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    duration_match = re.search(r'Duration:\s*(\d+):(\d+):(\d+)', result.stderr)
    if not duration_match:
        return 0
    h, m, s = int(duration_match.group(1)), int(duration_match.group(2)), int(duration_match.group(3))
    return h * 3600 + m * 60 + s


MAX_CHUNK_SECONDS = 600  # 10 minutes per chunk (model limit is ~15-20 min)


def split_audio(audio_path: Path) -> list[Path]:
    """Split audio into 10-minute chunks if longer than 10 minutes."""
    total_seconds = get_audio_duration(audio_path)
    if total_seconds <= MAX_CHUNK_SECONDS:
        return [audio_path]

    num_chunks = math.ceil(total_seconds / MAX_CHUNK_SECONDS)
    chunks = []
    for i in range(num_chunks):
        start = i * MAX_CHUNK_SECONDS
        chunk_path = audio_path.with_stem(f"{audio_path.stem}_chunk{i:03d}")
        cmd = [
            FFMPEG, "-y", "-i", str(audio_path),
            "-ss", str(start), "-t", str(MAX_CHUNK_SECONDS),
            "-acodec", "libmp3lame", "-q:a", "5",
            str(chunk_path),
        ]
        subprocess.run(cmd, capture_output=True, timeout=300)
        if chunk_path.exists() and chunk_path.stat().st_size > 1000:
            chunks.append(chunk_path)

    return chunks if chunks else [audio_path]


def transcribe_file(audio_path: Path) -> str:
    """Transcribe a single audio file using OpenAI API."""
    with open(audio_path, "rb") as f:
        response = client.audio.transcriptions.create(
            model=MODEL,
            file=f,
            response_format="text",
        )
    return response


def transcribe_audio(audio_path: Path) -> str:
    """Transcribe audio, handling chunking if needed."""
    chunks = split_audio(audio_path)
    if len(chunks) == 1:
        return transcribe_file(chunks[0])

    texts = []
    for chunk in chunks:
        text = transcribe_file(chunk)
        texts.append(text)
        # Clean up chunk files
        if chunk != audio_path:
            chunk.unlink(missing_ok=True)

    return "\n\n".join(texts)


def create_markdown(parsed: dict, transcript: str, stage: str, video_id: str, index: int) -> str:
    """Create markdown file content with frontmatter."""
    title = parsed["title"]
    speaker = parsed["speaker"]
    org = parsed["organization"]
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    frontmatter = f"""---
title: "{title.replace('"', '\\"')}"
speaker: "{speaker.replace('"', '\\"')}"
organization: "{org.replace('"', '\\"')}"
stage: "{stage.capitalize()}"
youtube: "{youtube_url}"
---"""

    header = f"# {title}\n"
    if speaker:
        header += f"**{speaker}**"
        if org:
            header += f" ({org})"
        header += f" --- {stage.capitalize()} Stage\n"

    return f"{frontmatter}\n\n{header}\n{transcript}\n"


# ── Main Pipeline ───────────────────────────────────────────────────────────

def process_video(stage: str, index: int, video: dict) -> dict:
    """Download and transcribe a single video. Returns metadata dict."""
    video_id = video["id"]
    raw_title = video["title"]
    parsed = parse_title(raw_title)
    slug = slugify(parsed["title"] or raw_title)
    filename = f"{index:03d}-{slug}"

    audio_dir = AUDIO_DIR / stage
    audio_dir.mkdir(parents=True, exist_ok=True)
    transcript_dir = TRANSCRIPTS_DIR / stage
    transcript_dir.mkdir(parents=True, exist_ok=True)

    md_path = transcript_dir / f"{filename}.md"

    # Skip if already transcribed
    if md_path.exists() and md_path.stat().st_size > 100:
        print(f"  [SKIP] {stage}/{filename} (already exists)")
        return {
            "stage": stage,
            "index": index,
            "title": parsed["title"],
            "speaker": parsed["speaker"],
            "organization": parsed["organization"],
            "file": f"transcripts/{stage}/{filename}.md",
            "youtube": f"https://www.youtube.com/watch?v={video_id}",
            "status": "skipped",
        }

    try:
        # Download
        audio_path = audio_dir / filename
        print(f"  [DL] {stage}/{filename}...")
        mp3_path = download_audio(video_id, audio_path)

        if not mp3_path.exists():
            print(f"  [FAIL] Download failed: {stage}/{filename}")
            return {
                "stage": stage, "index": index, "title": parsed["title"],
                "speaker": parsed["speaker"], "organization": parsed["organization"],
                "file": "", "youtube": f"https://www.youtube.com/watch?v={video_id}",
                "status": "download_failed",
            }

        # Transcribe
        print(f"  [TX] {stage}/{filename} ({mp3_path.stat().st_size // 1024}KB)...")
        transcript = transcribe_audio(mp3_path)

        # Write markdown
        md_content = create_markdown(parsed, transcript, stage, video_id, index)
        md_path.write_text(md_content, encoding="utf-8")

        # Clean up audio
        mp3_path.unlink(missing_ok=True)

        print(f"  [OK] {stage}/{filename}")
        return {
            "stage": stage,
            "index": index,
            "title": parsed["title"],
            "speaker": parsed["speaker"],
            "organization": parsed["organization"],
            "file": f"transcripts/{stage}/{filename}.md",
            "youtube": f"https://www.youtube.com/watch?v={video_id}",
            "status": "done",
        }

    except Exception as e:
        print(f"  [ERR] {stage}/{filename}: {e}")
        # Clean up partial audio
        for ext in ['.mp3', '.m4a', '.webm', '.opus']:
            (audio_dir / filename).with_suffix(ext).unlink(missing_ok=True)
        return {
            "stage": stage, "index": index, "title": parsed["title"],
            "speaker": parsed["speaker"], "organization": parsed["organization"],
            "file": "", "youtube": f"https://www.youtube.com/watch?v={video_id}",
            "status": f"error: {e}",
        }


def generate_index(all_results: list[dict]):
    """Generate INDEX.md from all transcription results."""
    index_path = ROOT / "INDEX.md"

    lines = [
        "# EthCC[9] Talk Index",
        "",
        f"**{sum(1 for r in all_results if r['status'] in ('done', 'skipped'))} talks transcribed** "
        f"from EthCC[9] (March 30 -- April 2, 2026, Cannes)",
        "",
    ]

    # Group by stage
    stages = {}
    for r in all_results:
        stages.setdefault(r["stage"], []).append(r)

    for stage_name in ["chaplin", "monroe", "redford", "kelly", "hepburn", "burton", "taylor"]:
        if stage_name not in stages:
            continue
        talks = stages[stage_name]
        lines.append(f"## {stage_name.capitalize()} Stage ({len(talks)} talks)")
        lines.append("")
        lines.append("| # | Talk | Speaker | Transcript |")
        lines.append("|---|------|---------|------------|")
        for t in sorted(talks, key=lambda x: x["index"]):
            title = t["title"][:70]
            speaker = t["speaker"][:40] if t["speaker"] else ""
            link = f"[transcript]({t['file']})" if t["file"] else "---"
            yt = f"[video]({t['youtube']})"
            lines.append(f"| {t['index']} | {title} | {speaker} | {link} {yt} |")
        lines.append("")

    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nINDEX.md written with {len(all_results)} entries.")


def main():
    print("=" * 60)
    print("EthCC[9] Transcription Pipeline")
    print(f"Model: {MODEL} (~$0.003/min)")
    print("=" * 60)

    all_results = []

    for stage, playlist_id in PLAYLISTS.items():
        print(f"\n--- {stage.upper()} STAGE ---")
        print(f"Fetching playlist {playlist_id}...")
        videos = get_playlist_videos(playlist_id)
        print(f"Found {len(videos)} videos")

        # Process videos with limited parallelism
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {}
            for i, video in enumerate(videos, 1):
                future = executor.submit(process_video, stage, i, video)
                futures[future] = video

            for future in as_completed(futures):
                result = future.result()
                all_results.append(result)

    # Generate index
    generate_index(all_results)

    # Summary
    done = sum(1 for r in all_results if r["status"] in ("done", "skipped"))
    failed = sum(1 for r in all_results if r["status"] not in ("done", "skipped"))
    print(f"\n{'=' * 60}")
    print(f"DONE: {done} transcribed, {failed} failed, {len(all_results)} total")
    print(f"{'=' * 60}")

    # Save results log
    log_path = ROOT / "scripts" / "results.json"
    with open(log_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"Results log saved to {log_path}")


if __name__ == "__main__":
    main()
