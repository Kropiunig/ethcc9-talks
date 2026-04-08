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
- [Vitalik Buterin -- "Real Decentralization"](transcripts/monroe/033-nicolas-consigny-ethereum-foundation-vitalik-buterin-ethereum-foundation.md) -- Walk-away test, insider attack test, trusted computing base. Called out superficial decentralization in L2s.
- [Stani Kulechov -- From Scarcity to Abundance](transcripts/monroe/002-from-scarcity-to-abundance-financing-the-multi-trillion-dollar-infras.md) -- Multi-trillion dollar infrastructure financing vision from the Aave founder.

**DeFi & AMM Design**
- [Kite Liu + Eric Zhong (Uniswap Labs) -- Continuous Clearing Auctions](transcripts/taylor/007-continuous-clearing-auctions-the-new-standard.md) -- CCA as the new standard for bootstrapping liquidity. Live on Ethereum, Unichain, Arbitrum, Base.
- [Sergej Kunz (1inch) -- Rethinking AMMs](transcripts/monroe/048-rethinking-amms-why-todays-liquidity-design-wont-work-at-scale.md) -- Why today's liquidity design won't work at scale.
- [Stefan Loesch -- Making Arbitrage Work](transcripts/chaplin/010-making-arbitrage-work.md) -- Practical arbitrage mechanics in DeFi.
- [Corinne Powers -- Stop Using Ranges to Concentrate Liquidity](transcripts/taylor/004-stop-using-ranges-to-concentrate-liquidity-in-a-pool.md) -- Concentrated liquidity critique.

**MEV & Block Building**
- [Christoph Schlegel (Flashbots) -- Competition through Spam on L2s](transcripts/monroe/039-competition-through-spam-on-l2s.md) -- L2 spam dynamics and builder competition.
- [Terence Tsao -- From MEV-Boost to ePBS](transcripts/redford/027-from-mev-boost-to-epbs-the-protocolization-of-proposer-builder-separ.md) -- The protocolization of proposer-builder separation.
- [Krzysztof Gogol -- The Return of Sandwiches](transcripts/taylor/014-the-return-of-sandwiches-mev-and-sequencer-design-on-layer-2s.md) -- MEV and sequencer design on Layer-2s.
- [Luis Correia (Flashbots) -- Optimising Block Building with Genetic Algorithms](transcripts/hepburn/044-luis-correia-flashbots-optimising-block-building-with-genetic-algorithms.md)

**Layer 2 & Rollups**
- [Jordi Baylina + Friederike Ernst -- Rollups Broke Ethereum / Introducing EEZ](transcripts/redford/018-rollups-broke-ethereum-but-we-can-fix-it-introd.md) -- Ethereum Economic Zone: synchronously composable L2s.
- [Emilio Frangella (Aave Labs) -- Aave V4 and Beyond](transcripts/monroe/017-aave-v4-and-beyond-bringing-capital-markets-onchain.md) -- Hub-and-spoke lending, bringing capital markets onchain.

**Trading & Market Structure**
- [Mariia Keiko (CoW DAO) -- When Theory Meets Mainnet](transcripts/burton/012-when-theory-meets-mainnet-intent-based-trading-at-scale.md) -- Intent-based trading at scale.
- [Suki Yang -- High-frequency Trading in Crypto](transcripts/burton/011-high-frequency-trading-in-crypto.md)
- [Alex Cutler (Aerodrome) -- The MetaDEX Thesis](transcripts/redford/004-the-metadex-thesis-rewriting-the-rules-of-defi.md) -- Rewriting the rules of DeFi.

**Security**
- [nisedo (Trail of Bits) -- Uniswap v4 Hooks Security Guide](transcripts/kelly/046-uniswap-v4-hooks-a-security-guide-for-builders-and-breakers.md) -- For builders and breakers.
- [Jonathan Passerat-Palmbach (Flashbots) -- Decrypting Encrypted Mempools](transcripts/redford/043-decrypting-encrypted-mempools-st.md)

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

Total transcription cost: ~$20.

## Accuracy

These are AI-generated transcripts. They are good but not perfect -- expect occasional errors with proper names, technical terms, or heavy accents. When precision matters, cross-reference with the YouTube recordings linked in each file's frontmatter.

## License

Transcripts are provided under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original talks are the intellectual property of their respective speakers. Video recordings belong to [EthCC](https://ethcc.io/) / [Ethereum France](https://www.ethereum-france.com/).

