#!/usr/bin/env python3
"""
Fetch YouTube auto-captions for videos that failed audio download.
Falls back to free YouTube subtitles instead of paid transcription.
"""

import os
import sys
import json
import re
import subprocess
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_DIR = ROOT / "transcripts"
YTDLP = shutil.which("yt-dlp") or str(Path.home() / "AppData/Roaming/Python/Python313/Scripts/yt-dlp.exe")

PLAYLISTS = {
    "monroe":  "PLfc9R9NWDYvIXQYIIjlQrs9Z7zsCJc2J_",
    "redford": "PLM-Xjhvin-uUY01s84QzYhL35KQQUos44",
    "kelly":   "PL-owlDp9BBavKDDJOpsTAupQhlfaLwYJl",
    "hepburn": "PLhM7rBgpVV-IzjnT4umBqI7WGVLvKQFYw",
    "burton":  "PLUt355rCCNrSi56eo6hDn3s6Ufzn1-zqH",
    "taylor":  "PLqL60kqgLPBA41jhJIBl2sZU6jI-DvCW4",
    "chaplin": "PLSJ8gU1sECuxvjRql4KaDaqqYB1F7qsFu",
}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:80].strip('-')


def parse_title(raw_title):
    raw_title = re.sub(r'\s*\|.*$', '', raw_title).strip()
    m = re.match(r'^(.+?)\s*\(([^)]+)\)\s*[-–—]\s*(.+)$', raw_title)
    if m:
        return {"speaker": m.group(1).strip(), "organization": m.group(2).strip(), "title": m.group(3).strip()}
    m = re.match(r'^(.+?)\s*[-–—]\s*(.+)$', raw_title)
    if m:
        speaker_part = m.group(1).strip()
        orgs = re.findall(r'\(([^)]+)\)', speaker_part)
        speaker_clean = re.sub(r'\s*\([^)]*\)\s*', ' ', speaker_part).strip().strip(', ')
        return {"speaker": speaker_clean, "organization": ", ".join(orgs), "title": m.group(2).strip()}
    return {"speaker": "", "organization": "", "title": raw_title}


def get_playlist_videos(playlist_id):
    cmd = [YTDLP, "--flat-playlist", "--print", "%(id)s\t%(title)s\t%(duration)s",
           "--no-warnings", f"https://www.youtube.com/playlist?list={playlist_id}"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    videos = []
    for line in result.stdout.strip().split('\n'):
        if not line.strip():
            continue
        parts = line.split('\t')
        if len(parts) >= 2:
            vid_id, title = parts[0], parts[1]
            if any(skip in title.lower() for skip in ['tastenkombinationen', 'wiedergabe', 'allgemein', 'untertitel', 'sphärische', 'beschreibung']):
                continue
            videos.append({"id": vid_id, "title": title})
    return videos


def fetch_caption(video_id, output_path):
    """Download auto-generated English captions as SRT, convert to clean text."""
    srt_path = output_path.with_suffix('.en.srt')
    cmd = [
        YTDLP,
        "--write-auto-sub",
        "--sub-lang", "en",
        "--sub-format", "srt",
        "--skip-download",
        "-o", str(output_path),
        "--no-warnings",
        "--no-playlist",
        f"https://www.youtube.com/watch?v={video_id}",
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    # yt-dlp names it with .en.srt suffix
    for candidate in [srt_path, output_path.with_suffix('.en.srt'),
                      Path(str(output_path) + '.en.srt')]:
        if candidate.exists():
            return clean_srt(candidate)
    return None


def clean_srt(srt_path):
    """Convert SRT subtitles to clean paragraph text."""
    text = srt_path.read_text(encoding='utf-8', errors='ignore')
    srt_path.unlink(missing_ok=True)

    lines = []
    for line in text.split('\n'):
        line = line.strip()
        # Skip sequence numbers, timestamps, empty lines
        if not line or line.isdigit() or '-->' in line:
            continue
        # Remove HTML tags
        line = re.sub(r'<[^>]+>', '', line)
        if line and line not in lines[-1:]:  # deduplicate consecutive
            lines.append(line)

    # Join into paragraphs (new paragraph every ~5 sentences)
    paragraphs = []
    current = []
    for line in lines:
        current.append(line)
        if len(current) >= 8:
            paragraphs.append(' '.join(current))
            current = []
    if current:
        paragraphs.append(' '.join(current))

    return '\n\n'.join(paragraphs)


def main():
    print("=" * 60)
    print("Fetching YouTube auto-captions for missing transcripts")
    print("=" * 60)

    total_fetched = 0
    total_skipped = 0
    total_failed = 0

    for stage, playlist_id in PLAYLISTS.items():
        print(f"\n--- {stage.upper()} ---")
        videos = get_playlist_videos(playlist_id)
        print(f"  {len(videos)} videos in playlist")

        for i, video in enumerate(videos, 1):
            parsed = parse_title(video["title"])
            slug = slugify(parsed["title"] or video["title"])
            filename = f"{i:03d}-{slug}"
            md_path = TRANSCRIPTS_DIR / stage / f"{filename}.md"

            if md_path.exists() and md_path.stat().st_size > 100:
                total_skipped += 1
                continue

            print(f"  [CAP] {stage}/{filename}...")
            tmp_path = TRANSCRIPTS_DIR / stage / f"_tmp_{filename}"
            transcript = fetch_caption(video["id"], tmp_path)

            if not transcript:
                print(f"  [FAIL] No captions: {stage}/{filename}")
                total_failed += 1
                continue

            # Write markdown
            title = parsed["title"]
            speaker = parsed["speaker"]
            org = parsed["organization"]
            youtube_url = f"https://www.youtube.com/watch?v={video['id']}"

            content = f"""---
title: "{title.replace('"', '\\"')}"
speaker: "{speaker.replace('"', '\\"')}"
organization: "{org.replace('"', '\\"')}"
stage: "{stage.capitalize()}"
youtube: "{youtube_url}"
transcription: "youtube-auto-captions"
---

# {title}
**{speaker}**{f' ({org})' if org else ''} --- {stage.capitalize()} Stage

{transcript}
"""
            md_path.write_text(content, encoding="utf-8")
            print(f"  [OK] {stage}/{filename}")
            total_fetched += 1

    print(f"\n{'=' * 60}")
    print(f"Captions fetched: {total_fetched}, Skipped: {total_skipped}, Failed: {total_failed}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
