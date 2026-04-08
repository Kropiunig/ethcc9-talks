# EthCC[9] Transcripts

Every talk from EthCC[9], transcribed and searchable.

**~300 talks | 400+ speakers | 7 stages | 4 days | ~113 hours of content**

EthCC[9] ran March 30 -- April 2, 2026 at the Palais des Festivals in Cannes. This repo contains AI-generated transcripts of every recorded talk, structured for use with coding agents like [Claude Code](https://claude.ai/claude-code), Cursor, or any LLM-powered tool.

## Quick Start

```bash
git clone https://github.com/Kropiunig/ethcc9-talks.git
cd ethcc9-talks

# Open with Claude Code
claude

# Then ask:
# "What did Vitalik talk about?"
# "Summarize the DeFi talks"
# "What was said about MEV and PBS?"
# "Which talks covered stablecoins regulation?"
```

## Structure

```
transcripts/
  chaplin/    # Main stage -- DeFi Day, research
  monroe/     # DeFi, L2s, privacy, keynotes
  redford/    # Stablecoins, MEV, institutional
  kelly/      # Euro stablecoins, DAOs, core protocol
  hepburn/    # Regulation, staking, block building
  burton/     # RWA, trading, AI agents, ZK
  taylor/     # Security, formal verification, privacy
INDEX.md      # Full talk list with links
CLAUDE.md     # Agent instructions
```

Each transcript is a markdown file with YAML frontmatter (title, speaker, organization, stage, YouTube URL).

## How It Was Made

All talks were recorded by [StreamETH](https://streameth.org/) and livestreamed to YouTube. Audio was extracted with [yt-dlp](https://github.com/yt-dlp/yt-dlp) and transcribed using OpenAI's `gpt-4o-mini-transcribe` model. The pipeline script is in `scripts/transcribe.py`.

Total transcription cost: ~$20.

## Accuracy

These are AI-generated transcripts. They are very good but not perfect -- expect occasional errors with names, technical terms, or heavy accents. When precision matters, cross-reference with the YouTube recordings linked in each file's frontmatter.

## License

Transcripts are provided under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original talks are the intellectual property of their respective speakers. Video recordings belong to [EthCC](https://ethcc.io/) / [Ethereum France](https://www.ethereum-france.com/).

