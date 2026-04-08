---
title: "Cooking With GASS: A Developer-Friendly Airdrop Mechanism"
speaker: "Noid"
organization: "Kraken"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=DqOd8ygM9-0"
transcription: "youtube-auto-captions"
---

# Cooking With GASS: A Developer-Friendly Airdrop Mechanism
**Noid** (Kraken) --- Burton Stage

Good. Hello everyone. Thank you for coming. My name is Noid. I work for Kraken, but I'm coming to you on behalf of myself today. So this isn't an official Kraken pitch. I'm coming to you as a builder. I normally work in the security department and I also think in order to

secure things, you really need to understand what developers are doing. And so I'm here today to talk about airdrops. How many of you guys love airdrops? See? Okay, a few. To be honest, I hate them. I really hate them. And so today I'm

hoping to fix all of the problems that we have with the airdrop system. This is an open source project so you can clone it, play around with it. And the idea is to solve some of these problems that I think is makes our industry look a little bit amateurish. And by the way, anything I say, I'm not

meant to be critical of any other project or anything, but it's just sort of how I see it. So, um Oh, no. Okay, perfect. Um so everybody hates them.

Even though you said you love them, I think there's so many problems. And my non-crypto friends are telling me about why are all these people making these terrible things these terrible pull requests on my projects. Why are they asking me for my GitHub handle? Well, it turns out we created a lot of perverse

incentives when we started to reward people for making pull requests on open source projects. It's a great idea, right? It's a great way to prevent people from spamming or making multiple accounts. You want to reward the real people here, right? Well, it turns out that has created a huge problem of

people trying to game the system. And I'm here to solve it with a project called GAS. So, you know, we're on chain, right? We have all of these advantages being on chain, right? We have auditability, we have universality, right? It's interoperability. We have all these

advantages. And I've seen a lot of these projects use things like Google Docs to track which projects we are contributing to. Or even more specifically GitHub of you know, here are the people that are going to receive that reward. I think that's fine if you're in a web 2 world, right? We're web 3. We're supposed to

showcase the power of the blockchain. I think in my opinion, this should be more crypto native. Um so what this actually looks like talking to my non-crypto developer friends, it's also a big hassle. So even if your name is in the Google spreadsheet, you have to do lots of

weird things that, you know, if the goal of an airdrop is to incentivize people to check out your product, to get involved, to do all those things, you have to do a lot of things that are really sketchy from a developer point of view. For example, not to call out StarkNet here, but you have to authorize

this app that no one has ever used. And so my developer friends, they don't really want to do that, right? They don't know what it is, it's not vetted. They don't want to connect their GitHub account that has their life's work on it just to get a token that they're not going to be sure if it

has any value. Same thing too, even after you connect it, many of these airdrop portals are making people go and download a wallet after the fact, right? Remember, these are developers, right? They're technical, they're familiar with these things. But those two things are disconnected, right? They're very

strange for people to say, "Okay, I have to go through all these steps and then download a wallet and then set it up and then do a separate onboarding guide." I think that's really inefficient and we have a ton of tools available to be able to make this really, really nice. And so that's where this project comes

in, GAS. And so GAS stands for the GitHub activity scoring system and the idea is to make this web 2 stuff more on chain. And so basically I I like to think of it as a system because there's a lots of different parts. But really it's not as complicated as I'm making it sound. Basically from the user

perspective, what you do is, let's say you're a project. You would make a landing page, you can sign in with GitHub. And then now thanks to social wallets with Dynamic and Privy, you instantly get a GitHub wallet, right? You don't even have to download a different app. You can sign in with

GitHub, get your wallet right there. Also, we need to be able to quantify those things, right? We need to quantify contributions and not just, "Oh, you've contributed to this." Well, is it good or is it bad? Was it fixing a typo or was it a significant feature? And so now with LLMs, most open source projects are

in GitHub, we should be taking advantage of GitHub actions to push that off-chain data on chain to where we can really use it and make it interoperable with a lot of the things that we need. And so that's kind of the idea here, right? The intention is to onboard people into our

web 3 space using the tools that they already know, are familiar with, and don't take them out of that UX onboarding flow that they know quite well. So again, this is relatively stack agnostic. This is an alpha experiment so to speak. So I'm not offering a token or

shilling my project. I'm not affiliated with anybody here by the way, but this is just an example where we have all these tools in this ecosystem that can really be aligned together to figure out how to make this happen. So Dynamic I mentioned for the smart wallets, but Privy would work the same. Um Base,

right? It's an L2. I'm doing this on Base Sepolia, but this should work on Ethereum, Ink Chain, things like that. GitHub, we talked about GitHub actions and the OAuth. Open Router, if any of you use LLMs, Open Router is awesome. You can spend $10 and get thousands of requests on

different models for free. And so this tool takes advantage of this. You basically have to spend no money to do that. And then a lot of the on-chain things, Forte, forte.io, they have an on-chain oracle product which is basically an API that you can easily push stuff on chain as well as a policy

engine to help you decide what to do with that data once it's on chain. So this stack, you can plug in whatever works for you according to what you like. So, the problems. I kind of addressed some of those problems, but one of the first problems I see is devs are

skeptical, right? They have a trust problem. They think crypto is sketchy. They think it's weird. They think they're going to get hacked. They And can you blame them, right? That's all they see in the headlines. They see scammers, all these sorts of things all over the place. And so how do we solve

that problem? Well, we use embedded social wallets like Dynamic, Privy, things like that to where if you're claiming token rewards for things that you're doing on GitHub, why not connect those two dots in a way that that UX feels native. It should feel like logging in to GitHub like everything

else, right? They don't even know there's blockchain behind it maybe, right? They can understand that a lot better than going to some strange site, downloading some strange wallet, backing up the seed phrase. All those things are good, but we got to dip their toes into it and and sort of convert them

along the way. So the second problem that I see is that, you know, everyone complains about the low effort time when it's airdrop season. No offense to you professional airdrop farmers, you know who you are, but it really becomes a different place when people are coming up with the best

ways to create accounts, game systems, buy accounts on GitHub. And basically we are creating a haven for spam. So much so that other people outside of our industry are really thinking of us as the spammers. And so instead of giving rewards to people just for contributing once, this GitHub action will actually

use the Open Router AI endpoint to review the pull requests and then push these quality scores on chain. Remember, on chain is interoperable. So it doesn't matter if your project is in Rust or in Go or in Python. We're taking that important data, reviewing your contribution, and then pushing your

name, the quality score, when you were last active, and the repo that you contributed to. And then we can query that on chain to actually capture that important data in a way that's interoperable. So, the third problem is unfair rewards, right? We have a lot of things that,

you know, it's not sure. It's unclear, right? Well, you can actually use on-chain policies to do that. They're a composable rules that you can say you need to have 10 contributions or five contributions or 10 different groups to do that. On-chain policies using the Forte rule engine allows you to do that.

If you're not familiar with this product, basically you can create these JSON policies. Um so in this case it's using these quality scores, but imagine this is like a KYC check or is not a sanctioned person or something. Right now we use VPNs, but there's a lot better ways that we can do this on

chain. You define it as JSON and then you can use that on chain to actually control the distribution. The oracle, it's a very simple API. You can push these on chain using that data that we have with a GitHub action. So here's how it works. You make a pull request.

There is a GitHub action that will comment and review it and then push that on chain. And then you can query it and use it in all of these other operations, which is very cool. I'll go through this very quickly in terms of the technical flow, but I wanted to showcase the demo here of what this looks like from the

end user. So the end user to claim, they log in with GitHub. And they immediately get a wallet. And so you can check your eligibility using what we mentioned with the rule engine on chain. We are eligible because our contributions were high quality.

And now we are vetting those things using those on-chain policies to return that this person can get X number of tokens, and now we actually have those tokens sent on base Sepolia. So, if you'd like to get involved, I have a test repo that you can make a pull request today and see how it

scores, check how it is. I'm not promising a token, but if you're an open-source project, a developer, you like the concept, and you want to dig more into that, this is a way that we can do these policies on-chain, where it belongs, and not on Google Drive, Google Docs, GitHub, things like that that

aren't really taking full advantage of the promise of Web3. Thanks, everyone. If you want to contact me, uh Signal and my portrait site. Thank you.
