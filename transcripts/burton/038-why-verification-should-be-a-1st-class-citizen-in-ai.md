---
title: "Why Verification Should be a 1st Class Citizen in AI"
speaker: "Jake Salerno"
organization: "0g.ai"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=2F9A0KsG7iI"
transcription: "youtube-auto-captions"
---

# Why Verification Should be a 1st Class Citizen in AI
**Jake Salerno** (0g.ai) --- Burton Stage

Good afternoon everyone. Thanks for taking the time out of your beautiful con afternoon to learn more about decentralized AI and what zero G is building within that space. I'm uh Jake Seno, the VP of go to market at Zeroravity Labs. And for the next 20 minutes, I'd like to talk about

something the AI industry is getting wrong and what we're doing about it and solving on the fly for it. So every time that you use an AI model today, you're making a trust assumption and it's centralized. You're trusting the provider won't look at your data. And it's open source. If the picture is

even worse, you know, this year reaches researchers found over 30,000 exposed instances of OpenClaw and that's the fastest growing AI project in history. And API keys, private keys, customer data, all in the open. And so that's obviously an open claw problem. Um, it's a category problem. And the entire AI

industry runs on these trust assumptions and we send our most sensitive data to the models and hope for the best, right? So there's no verification layer anywhere and that's what we're here to change. So, when you use uh centralized AI, you're trusting someone else's server

with your data and you're trusting their privacy policy and you're also trusting they won't change the terms and conditions tomorrow. Again, that's a trust assumption. In crypto, we learned a long time ago, don't trust, verify. And I think that's a a hot topic that many of you OGs may um have recalled

from the first ECC, right? AI needs to learn the same lesson in my opinion at least and verification should be uh you know proactively addressed and integrated should not be an afterthought and it should be the design. So this is zero. We're building the blockchain for AI

agents. But what does that mean? AI agents need four things. Something to store their data in memory. compute for reasoning and inference and then high-speed data availability and a chain for settlement. So zero G puts all four in one stack. The true meat and potatoes every AI action is verified on

chain. And who is this for, right? Is it for you? Is it for me? Is it for B2B, B TOC? We're figuring that out with our go to market strategy and our ICP analysis. But if you're building AI agents, we give you identity, payments, verified execution, you're a developer adding AI to your application, whether it's um a

DAP or off-chain, ReVM compatible, solidity, and hard hat work out of the box. And if you're an infrastructure provider, we have 57 validators including NT, Domico, Coinbase Cloud, Deutsch Telecom, Tier Ones, all running that infrastructure. And this is all live. Every bit of this stack since uh

September 2025. Uh 28 million blocks, 300 plus projects building, 325 million raised. This is not a pitch deck. Um this is what we're running right now. And it's the reason uh that we're really aggressively going to market here at ECC and in general. Um and it matters right now because

verification is finally possible at scale. And I'd love to show you how. So the first pillar of verification is compute. We call it sealed inference. And here's how it works. You know, your your model runs inside a trusted execution environment, a hardware enclave. Your data goes in encrypted.

And then the output comes out cry uh cryptographically signed where the model is thinking no one can read your data, not the server operator, not us. Um and this is not encryption at rest. This is privacy during computation and hardware enforced not policy enforced. Um the difference matters because a privacy

policy can change uh with a term of service update but hardware guarantees don't and this is live. It's not coming soon. It's live on mainet today. There's a lot of great projects building with it. So the second pillar here is identity and agents are becoming economic actors.

Um funny I was at ETH Denver and I surveyed the the audience and I said how many of you in the audience have used a bot or an agent and just about every hand went up and then I said how many of you connected that agent to your hot wallet and just about every hand went down because that's a pretty big trust

assumption right I personally would be very scared to do that. that we've seen some companies come out with solutions with like rate limiting where you can connect it and it only lets you transfer so much. But agents are truly becoming economic economic actors because they can't open bank accounts. And of course,

I'm sure you guys have heard with the AI track. That's where the agentic settlement layers come. That's where that true kind of blockchain use case fits in so well. Agents can send value on chain. Uh so they're trading, they're executing transactions, making decisions with real money. A16Z called it uh

number one trend crypto this year. Coinbase built the X42 for machine toachine payments. But here's the thing, an agent with no verified identity is just anonymous code having money and you can't hold it accountable. You can't audit it and you can't trust it. So that's why we built ERC7857

and it's an Ethereum standard authored by Zerog and it's launching later this month. It uh makes agents legible. Ownership, who controls this agent? Providence, what's the track record of this agent? Uh actions, what is it doing right now? All verified on chain. And identity is what turns anonymous code

into trustworthy economic participants. And that's what we'll be calling agentic ID. So that third pillar is training. Uh Jensen Hang just validated decentralized AI training on the All-In podcast. Um this category is real. The question is how do you verify it? And Dilox 107B is

our answer. Uh it's 107 billion parameters and it's the largest decentralized training run ever. Uh 357 times more communication efficient than standard distributing power. Um, Bit Tensor trained a 72 billion parameter model with incentive alignment, which is great. Um, miners are economically

motivated to be honest there. Uh, we used TE verification, trusted execution environment verification. The hardware physically prevents dishonesty and both approaches work, but only one give you a cryptographic proof that was, you know, done in the training uh, with this being correct. That's the difference between

hoping the incentives hold and knowing the math checks out. So, Dill Cox is of course live and one of those big pieces of breakthroughs of research that we were able to achieve with Zurgy. And of course, the slide I want you to remember verified compute, verified identity, verified training. Three pillars, one

architecture and every layer has cryptographic proof. This is not a feature list. This is a design philosophy and every other platform asks you to trust. ZeroG lets you verify and that's what it means to make verification a first class citizen. Uh, hence the title of my talk, not an

add-on, not a bolt-on, not an upgrade, the foundation. So, we're not here to present a roadmap. We are launching a new product every week uh through April, which is exciting. um especially kicking things off here at this wonderful conference. Sealed inference is live. Dilox is

published. Uh ghast AI launches tomorrow which you know follow along the journey for that launch announcement. Then uh zero studio we're building something something called company in a box which is really exciting. Uh where all the seues of agents are fine-tuned and trained on the best in the world and

they manage your company for you. You could be hands off, text to prompt, company in a box. Uh, and of course more is coming on the DeFi side. We've got blue chip DI launching because the liquidity layer for AI agents matter. So, we have a lot of those different DeFi core primitives going live, whether

they are the existing big players or some of the newer um, evolutions of that core stack with more AI enablement uh, text to trade if you must. But if you're a builder, there's never been a better time to start. And here's what you can do. do this week. I actually just walked over from the Carlton. That's why I'm a

bit sweaty and I'm also wearing a sweater and it's sunny. So, I made that mistake. But you don't need to make any more mistakes today like I did because you could go to the zero coding event at the Carlton and it's packed. People with non-technical backgrounds are shipping production grade environments text to

prompt with zero g low code no code builder. Um, so right after the talk, it's downstairs at the Carlton if you're interested. There's food, there's drinks, but it's hand hands-on building with zero G tools. And tomorrow we have a builder's villa. It's open all day. So come talk to our engineers, ask hard

questions, get office hours. And from Thursday, uh, ETH Global, the hackathon, um, you know, ZeroG has one of the largest bunny bounties with $25,000, uh, set aside to a couple different categories, uh, that are important to us to see builders activating on ZeroG. So, there's this QR code that I see that

many of you are scanning at the moment that takes you to all of our events. Scan it, pick what works best for you or what you want to see uh, kind of built with the ETH Global stuff. Please feel free to show up and I'll be there myself as a judge. But I do want to leave you with this. Ver verification is not a

feature, it's the design. And I really hope to leave you with that. Happy to answer any questions that you may have off to the side here so we stay on track. But I do appreciate your time and look forward to building with you. Thank you.
