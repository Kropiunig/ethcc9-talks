# EthCC[9] Transcripts

Every talk from EthCC[9], transcribed and searchable.

**307 talks | 400+ speakers | 7 stages | 4 days | ~113 hours of content**

EthCC[9] ran March 30 -- April 2, 2026 at the Palais des Festivals in Cannes. This repo contains transcripts of every recorded talk, structured for use with coding agents like [Claude Code](https://claude.ai/claude-code), Cursor, or any LLM-powered tool.

Clone it, point your agent at it, ask anything about the conference.

## Quick Start

```bash
git clone https://github.com/Kropiunig/ethcc9-talks.git
cd ethcc9-talks

# Open with Claude Code
claude

# Then ask:
# "What did Vitalik talk about?"
# "Summarize all the MEV and PBS talks"
# "What's the state of institutional DeFi adoption?"
# "Which talks covered stablecoin regulation under MiCA?"
# "What were the key announcements?"
```

## Highlights

Some of the most notable talks if you're short on time:

**Keynotes & Vision**
- **Vitalik Buterin -- "Real Decentralization"** ([transcript](transcripts/monroe/033-nicolas-consigny-ethereum-foundation-vitalik-buterin-ethereum-foundation.md) | [video](https://www.youtube.com/watch?v=yp2oW6Jw_yE)) -- Walk-away test, insider attack test, trusted computing base. Called out superficial decentralization in L2s.
- **Stani Kulechov -- From Scarcity to Abundance** ([transcript](transcripts/monroe/002-from-scarcity-to-abundance-financing-the-multi-trillion-dollar-infras.md) | [video](https://www.youtube.com/watch?v=5FXnlac2k5s)) -- Multi-trillion dollar infrastructure financing vision from the Aave founder.

**DeFi & AMM Design**
- **Kite Liu + Eric Zhong (Uniswap Labs) -- Continuous Clearing Auctions** ([transcript](transcripts/taylor/007-continuous-clearing-auctions-the-new-standard.md) | [video](https://www.youtube.com/watch?v=45mH-ohWnjg)) -- CCA as the new standard for bootstrapping liquidity. Live on Ethereum, Unichain, Arbitrum, Base.
- **Sergej Kunz (1inch) -- Rethinking AMMs** ([transcript](transcripts/monroe/048-rethinking-amms-why-todays-liquidity-design-wont-work-at-scale.md) | [video](https://www.youtube.com/watch?v=6-8-ZKjUS60)) -- Why today's liquidity design won't work at scale.
- **Stefan Loesch -- Making Arbitrage Work** ([transcript](transcripts/chaplin/010-making-arbitrage-work.md) | [video](https://www.youtube.com/watch?v=m7jIacHiLX0)) -- Practical arbitrage mechanics in DeFi.
- **Corinne Powers -- Stop Using Ranges to Concentrate Liquidity** ([transcript](transcripts/taylor/004-stop-using-ranges-to-concentrate-liquidity-in-a-pool.md) | [video](https://www.youtube.com/watch?v=tkmEPCbdBMY)) -- Concentrated liquidity critique.

**MEV & Block Building**
- **Christoph Schlegel (Flashbots) -- Competition through Spam on L2s** ([transcript](transcripts/monroe/039-competition-through-spam-on-l2s.md) | [video](https://www.youtube.com/watch?v=llZPzwF59lE)) -- L2 spam dynamics and builder competition.
- **Terence Tsao -- From MEV-Boost to ePBS** ([transcript](transcripts/redford/027-from-mev-boost-to-epbs-the-protocolization-of-proposer-builder-separ.md) | [video](https://www.youtube.com/watch?v=0qdciLzKMiM)) -- The protocolization of proposer-builder separation.
- **Krzysztof Gogol -- The Return of Sandwiches** ([transcript](transcripts/taylor/014-the-return-of-sandwiches-mev-and-sequencer-design-on-layer-2s.md) | [video](https://www.youtube.com/watch?v=2asBYTmgR5k)) -- MEV and sequencer design on Layer-2s.
- **Luis Correia (Flashbots) -- Optimising Block Building with Genetic Algorithms** ([transcript](transcripts/hepburn/044-luis-correia-flashbots-optimising-block-building-with-genetic-algorithms.md) | [video](https://www.youtube.com/watch?v=MNA3tAy2-QI))

**Layer 2 & Rollups**
- **Jordi Baylina + Friederike Ernst -- Rollups Broke Ethereum / Introducing EEZ** ([transcript](transcripts/redford/018-rollups-broke-ethereum-but-we-can-fix-it-introd.md) | [video](https://www.youtube.com/watch?v=40LlU8jZAhk)) -- Ethereum Economic Zone: synchronously composable L2s.
- **Emilio Frangella (Aave Labs) -- Aave V4 and Beyond** ([transcript](transcripts/monroe/017-aave-v4-and-beyond-bringing-capital-markets-onchain.md) | [video](https://www.youtube.com/watch?v=8xyae1rLJy8)) -- Hub-and-spoke lending, bringing capital markets onchain.

**Trading & Market Structure**
- **Mariia Keiko (CoW DAO) -- When Theory Meets Mainnet** ([transcript](transcripts/burton/012-when-theory-meets-mainnet-intent-based-trading-at-scale.md) | [video](https://www.youtube.com/watch?v=eAbIST7sf4Q)) -- Intent-based trading at scale.
- **Suki Yang -- High-frequency Trading in Crypto** ([transcript](transcripts/burton/011-high-frequency-trading-in-crypto.md) | [video](https://www.youtube.com/watch?v=EyddgWqM4eE))
- **Alex Cutler (Aerodrome) -- The MetaDEX Thesis** ([transcript](transcripts/redford/004-the-metadex-thesis-rewriting-the-rules-of-defi.md) | [video](https://www.youtube.com/watch?v=KTLH_PqxBfc)) -- Rewriting the rules of DeFi.

**Security**
- **nisedo (Trail of Bits) -- Uniswap v4 Hooks Security Guide** ([transcript](transcripts/kelly/046-uniswap-v4-hooks-a-security-guide-for-builders-and-breakers.md) | [video](https://www.youtube.com/watch?v=F4QjFySPS_0)) -- For builders and breakers.
- **Jonathan Passerat-Palmbach (Flashbots) -- Decrypting Encrypted Mempools** ([transcript](transcripts/redford/043-decrypting-encrypted-mempools-st.md) | [video](https://www.youtube.com/watch?v=Qw_znSZtF94))

See [INDEX.md](INDEX.md) for the full list of all 307 talks.

## Structure

```
transcripts/
  chaplin/    # Main stage -- DeFi Day, research panels
  monroe/     # DeFi, L2s, privacy, keynotes (including Vitalik)
  redford/    # Stablecoins, MEV/PBS, institutional DeFi, rollups
  kelly/      # Euro stablecoins, DAOs, core protocol, post-quantum
  hepburn/    # Regulation, staking, PeerDAS, block building
  burton/     # RWA tokenization, trading, AI agents, ZK proofs
  taylor/     # DeFi security, formal verification, privacy protocols
INDEX.md      # Complete talk list with links
CLAUDE.md     # Agent instructions for navigating this repo
```

Each transcript is a markdown file with YAML frontmatter (title, speaker, organization, stage, YouTube URL).

## How It Was Made

All talks were recorded by [StreamETH](https://streameth.org/) and livestreamed to YouTube across 7 stages. Audio was extracted with [yt-dlp](https://github.com/yt-dlp/yt-dlp) and transcribed using OpenAI's `gpt-4o-mini-transcribe` model, with YouTube auto-captions as fallback. The pipeline script is in [`scripts/transcribe.py`](scripts/transcribe.py).


## Accuracy

These are AI-generated transcripts. They are good but not perfect -- expect occasional errors with proper names, technical terms, or heavy accents. When precision matters, cross-reference with the YouTube recordings linked in each file's frontmatter.

## License

Transcripts are provided under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original talks are the intellectual property of their respective speakers. Video recordings belong to [EthCC](https://ethcc.io/) / [Ethereum France](https://www.ethereum-france.com/).

