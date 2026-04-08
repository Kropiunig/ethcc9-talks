---
title: "DIN - The Reputation, Quality Guarantees, and the Economics of Reliable Agents"
speaker: "E.G."
organization: "Infura/DIN"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=QhYv3wOujCc"
transcription: "youtube-auto-captions"
---

# DIN - The Reputation, Quality Guarantees, and the Economics of Reliable Agents
**E.G.** (Infura/DIN) --- Burton Stage

All right, thanks. Hi everybody. My name's E.J. Galano from the Infura team. I've been working on Infura for close to 10 years now. It'll be 10 years this summer. Um been doing API infrastructure, scaling nodes, primarily serving like MetaMask and any other people that were building

on Web3 over the last few years. And over the last two to three years, I've been focused on building our decentralized protocol, which is called DIN, decentralized infrastructure network. Uh you can think about it as a marketplace protocol for services, and we were starting with RPC and then

expanding beyond. So, that's sort of the the crux of what led us to looking into reputation and reputation-based services and how to solve some of the problems that currently exist with how you discover and trust agentic services, skills, MCP, etc. And that's what I'll be talking about today.

Uh so, when you look at all of the stuff that is typically discussed, whether it's here at EFCC or Devcon, there's a lot of crypto primitives that now exist that didn't exist two years ago, five years ago, that allow us to uh create and ship better products and

product experiences for users. Uh some of those are staking, on-chain reputation, stablecoin payments, and verifiable performance. You can look at some of the things that now exist that are being adopted in institutional sectors, and it wasn't possible before. Maybe it was because of scalability

challenges, and that was solved through having faster blockchains and solutions. And then having readily available supply of stablecoins means we can start using them for other types of payments, and the most interesting for us with agentic payments is like X402 and MPP type standards that I'll get into in a bit.

But all of these printed primitives help us solve some problems with agentic development and user flows, in particular discoverability, uh trust, and uh what was and reliability of these services. Because as anybody can develop a service and stand it up, that's one thing if they're using it for

themselves, but when they're offering it out there for other people to transact with, how do you actually know that this thing is reputable and that it'll actually deliver what you expect? So, in the old models of trust discovery, we uh relied on this type of model, whether it's like SEO and

traditional search, and you trust Google to give you the responses that uh are most likely to solve your problem, or you use curated marketplaces as a way of saying anything that's in this app store is likely not going to like hack my phone and steal everything that's on it, or you're looking at user reviews, like

what's the best uh restaurant here uh to go to for dinner, and you're looking at other people's feedback that you're putting in there. And that's human-based. So, agents don't do that, um or at least they don't really have the mechanisms right now to do that. And you can do things in a way that's uh

more verifiable. When we ask an LLM for something and it gives us a response, all of us kind of like second-guess it. We're like, is this one actually correct, or is this like hallucinating? Uh what is the data that you're using to come to this conclusion or make this um

make this uh what's it called? Uh uh say if it was like building an application and you said pick a data uh API that you want to integrate here, why is it that you chose this one? And it's typically saying something like, well,

just because or a bunch of people on Reddit were talking about it, so it seems reputable. Um more and more services are going to be popping up here and having something that's better than the the human style model is important. So, API services are transitioning to

becoming agentic services. Um when people talk about agentic services, like you typically picture something like autonomous thing that's doing work, but it's starting a lot simpler than that. People are taking their existing APIs or infrastructure, putting MCP in front of it, or now they're just

directly creating skills that you can integrate into Claude or whatever you're using, and call out to these APIs to provision infrastructure, get data, or just interact with all of these different applications. And how do you know which ones to trust or use? There have been vulnerabilities

recently in the supply chain that means like your laptop can get hacked or something if you say, "Oh, this was a really interesting skill. I could use this to quickly do my work." And maybe it worked like that, and then all of a sudden, because it was just a single developer that didn't have any sort of

dependency management control, uh your laptop gets hacked just because you wanted to save a few seconds on the solution that you were trying to vibe code. So, having some sort of curation or reputation is important for these things, and it's going to continue to be important as we transition from APIs,

MCPs, skills into like truly like agentic services. Going back to like real-world like day-to-day, commoditization happens with a lot of different services that are out there. So, we can talk about package delivery and how like you don't care how your package gets delivered. You just

care typically about like cost and ultimately like did it get there? And whether or not you receive your package is the receipt. So, that's easy with physical goods, but with um with something like an API service or an agentic service, what's the receipt? And in this agentic future, where bunches of

people are going to be trading new SaaS services or agentic services and saying, "Oh, I can compete with that thing. I'm going to create the exact same thing and put it out there and offer it with a 10% discount." You're going to see a lot of that. Like we're already seeing a lot of that sort of disrupting the SaaS

ecosystem. So, how are people going to know which ones to trust, or how are those people that are creating like viable like trustworthy services able to prove themselves? So, having a system where they can earn that reputation starts to become uh important.

First and foremost, like AI agents uh want receipts and benefit from having these receipts, having payment for the service that they provided. Initially, like just having uh a payment was sufficient, but like what about the actual like proof of work on the other side of that? So, we started in the work

that we were doing to decentralize Infura, started building a payment channel solution, and the idea was you would sign some request on the client side, we would serve your request on the server side, and that signed receipt bidirectional was the proof that both of us agreed to this price for the payment,

and you had this receipt for any like dispute that needed to happen. That um that was like traditional payment channel, state channel type work from like 2018. Things ended up not going that direction. Uh people chose to scale uh Ethereum and other things in

different ways, but that mechanism still works, and that's effectively what you can do with X402 and MPP, the two new protocols for agentic payment, one from Coinbase and one from Stripe. So, they're going to be uh competing or alternative standards. Like pretty much these are just the first two. Certainly,

there's going to be more. And we're not prescriptive about like which ones we're using in our solution, uh because they both serve our purposes, which is we want to make sure that for any agent or service that's offering uh something to be consumed and paid for, that there's like a bidirectional

agreement and receipt. Uh in terms of the trust aspect of it, it's providing more information to agents to make informed decisions that are data-backed. So, instead of just saying, "Okay, it crawled this webpage and it knows its pricing. It can determine like what it's willing to pay.

It knows your API documentation and can assess that you it can actually do this work." Um what what else does it have besides that? It doesn't have any proof that anybody else actually used this. Um and over time, people are going to stop relying on the trusted brands to deliver services. You're not going to go

to Cloudflare for these things, or you're not going to go to Vercel and say, "Okay, they have what I need." There's going to be a lot more capacity for other things that are going to be offered, and a lot of them can do the work. It just needs to be uh provable, and people have to have some sort of

like reassurance that they can try out this new service, and there going to be uh a lot of new opportunities opened up as a result of that. And so, getting the verifiable performance and having a historical track record of uh delivering services to people is one of the things that uh you get by

building on top of these agentic payment systems. So, we started building something like this specifically focused on Infura's use case, which was RPC. How were we going to um stop just serving traffic from like Infura's team itself? We were starting

to have to deal with like 24 different chains with any one chain like having either a hard fork or network upgrade or vulnerability that we needed to patch and keep up with. We started to diversify who was serving that traffic by having other people in this network that we

were building um run that infrastructure. So, that's what DIN started as is we got a collection of about 50 different providers that all said that they were capable and willing to serve RPC traffic, and we said, "Okay, here's a new network that we're going to be adding." Maybe it was like

most recently we added MegaEth is an example. And everybody says, "Okay, well, we can run Mega ETH." And so, we had some internal tests and quality checks and like verification methods that we had to ensure whenever somebody like stood up a new endpoint that it actually

served Mega ETH traffic. It served it performantly and reliably and it continuously tested it. So, that we could effectively score and have an objective measurement of which providers we would use and why we would use them. It wasn't just well, we recognize this name, so we sent them traffic or uh this

is somebody that offered us uh a discount and promised that they would uh give us an SLA of this amount. Uh everything that we did was data-backed. So, we started to have a way of categorizing this. The The most obvious ones that everyone starts with is like, well, latency and uptime. Has it ever

been down? Like, how quickly does it respond? But, you can do that for any API, but you very quickly have to go deeper in that to have a very specific um qualitative measure for that type of service. So, for RPC, it was things like how quickly does it get the latest

block? Does it stay consistently on that block or does it flip-flop? Um what does that consistency look like in like their caching methods and things if they're doing some sort of like off-chain indexing to improve performance of EVM queries or getting event logs and stuff like that. It It starts to very quickly

become specialized, but the more you specialize in that, the the better that score is that you get out the other end and you're able to differentiate all of these providers on more than just where they were geographically based, which is effectively what affects their latency. Uh and then once we had all of those

different parameters and we ran all of those tests, we put it into a weighted formula that spit out a score. And then we tested that score um continuously over a period of time whenever we were adding a new network and said, "Okay, these are the providers and these are all of their scores and we

can choose do we only want to use like the top three providers or maybe it's only two of them that met uh a certain bar for being able to meet the quality that we wanted to have or it was better to just have as many providers in there as we could. Um it gave us that optionality. And so, we built a custom

router that feeds in this data and makes those routing decisions. You can think about that as how you choose how to route uh API queries to your LLMs. There's projects out there already that allow you to do uh smart routing between different models. Not a lot of people are doing it right now. A lot of people

are Sorry, good? Yeah, just two questions. Um super interesting. Can you just come back to like what you measure exactly? I don't Oh, sure. I don't want to get into the specifics cuz this was very like RPC specific. So, all right. So, freshness

is um often times when people are running blockchain nodes, it'll just stop. Like, the the software isn't super reliable. Maybe it was like too many files open on on the OS or something like that and all of a sudden

it stops and you have to kick it and restart it. Pretty like unglamorous stuff. Um or just like the network itself halts. So, having that data freshness is important for an RPC because if you try to do something like send Infura a swap request and we're doing that swap

calculation off of stale data, your your swap's going to fail, right? Um and then correctness. A lot of people tried to solve the how you scale RPC by just doing some dumb caching. Like, you put CloudFront or something else in front of it and you start caching it, but that sort of like naive caching breaks very

quickly and that uh is what causes that incorrectness in the data. And then speed. Uh somebody can uh offer service that's always consistent, but it's going to be really slow if it's just one node that's serving that. The moment that you try to scale that by having multiple nodes, you

start to have uh more advanced uh systems in front of more advanced routing that's required to be able to route intelligently. And then especially if you start creating custom services to optimize specific types of uh method queries. Sure. Yeah. So, so that's specific to

RPC. If we were doing something, my favorite example is like weather data. Like, what what is it that's going to determine like what's a good quality like weather data API source? And it's going to look different than this. The real-world impact of this is that we were able to scale um how much traffic

was served in MetaMask. Initially, our team was the only one running it. Now, there's over a dozen different providers serving close to 30 different networks for anything um that you use in MetaMask. So, some of the newer ones like I said were um

uh Binance uh Mega ETH Blast L2 was the very first one that we added. Um Sei and Mode and and others that launched recently. So, what we learned from this is that uh providers are always able to undercut each other on price and often times the ones that have the best quality tend to

charge more and people are willing to pay it including us when we were paying other people to serve that traffic. Having a way to prove that you're high quality allows you to charge uh a higher price for your services. Otherwise, people just see your price compared to what this other agent is offering and

say, "I'm going to go with the cheaper one." Uh they're going to find out the hard way that they're not as good as you. So, having a system that allows you to prove that ahead of time helps with customer acquisition to use the the traditional term. And then the scores actually don't just

help the consumer, it also helps the provider because this is almost like a community-driven or uh in our case like also like AI-driven improvement uh parameter that people can use to assess their current quality. Like, how do I compare? How can I compete for this particular service

that I'm offering? And a lot of our providers for the Ethereum RPC ended up using that to improve their services. And then lastly, like gaming the system is always going to uh be something that people try because there's money to be made and so any sort of reputation system that you build here needs to be

resilient with that. Uh going to have to go quickly. I'm a little behind on time, but uh having those domain-specific checks is what I was mentioning. Ours was very RPC specific and if we started serving LLM, we're going to have to create checks

that are very LLM specific. How you gauge different LLM endpoints or models. And then having it be deterministic means that we can actually have a better scoring metric that uh you can use to compare providers. And like I was saying, beyond this, we were just starting with RPC. Our goal

and vision was always to expand beyond to other services, API services. And those API services are now agentic services. You put an MCP in front of it and people are saying it's an agentic service. And that is effectively an an interface, whatever it is in the future. It could be a skill, API, websocket,

like some interface to um an agentic like compute system can be scored on uh a model like this. It's necessary because right now there's only a small amount of like API requests that are generated by agents, but a lot of models out there show that uh or estimates out there show that

agentic-driven traffic is going to like quadruple in just like the next 6 months and it's going to continue to grow as more and more people start adopting agents in their workflows. I'm not sure if you can see Okay, that looks good enough or big enough. So, how

how do you use these scores? This is an example of how we use reputation to provide economic security for RPC where we started with staking. So, any new provider was uh going to have to stake to effectively join this registry. So, staking to join the registry ensures that it's not going to disappear when uh

somebody closes their laptop, right? Like, if somebody creates an agent that's doing something worthwhile for you, but then all of a sudden they say, "Okay, I'm kind of done with that experiment." You can't really trust it and the whole system kind of crumbles. Uh

if you start with having everybody join a registry and either stake or put some sort of bond or guarantee, it doesn't even have to be crypto. Um it allows people to have a reassurance that there's an economic penalty or at least reward for offering that service continuously.

Uh for something like this with our MCP, it looks like uh having a score that's offered for a particular MCP endpoint and people can say, "I want this category of data. There Here are a few MCPs and I want the one that uh serves it at least this level of

quality." And then with that, you're able to build trust-aware agents where now things aren't just blindly making choices or relying on traditional SEO for how it makes its choices. You're able to point it at a registry of information and say, "Find Find the services on here that we

need to build the application that we've been designing and tell me why you picked each service." So, you're able to do something like this query that's right here, which is find that weather MCP RPC that offers an SLA of like over two nines, which isn't too hard, and offers costs below a

certain metric. And you can expand out all of those measures and say, "It also needs to be OFAC compliant. It also needs to be SOC 2 compliant." Like, any sort of tags that can be verified out of band. And this is how that interaction would look. You know, somebody is offering

this API and you get a bunch of different providers saying that they can provide that weather API and then maybe if there's an outage, there's like a slashing or penalty that's issued in the process of how it's assessing the continuous scoring.

Sorry, that's a repeat. And that's our vision for how to build an agentic marketplace is that by having that stake and allowing people to prove that they can serve traffic for given services, they're able to get a premium price for quality and be rewarded for that quality and the lower

quality services sort of get filtered out over the long tail. Or over the long haul. And Sorry, let me just wrap up. The the main thing is right now there were like 7,000 MCP services registered

in recent months and that's grown to like 95,000 and it's going to continue to grow. Whether it's again, whether it's MCP or skills, people are going to optimize how tokens are used, but more and more of these services are popping up as people are trying to offer existing legacy products

to agents for agents to consume and there really is no way to effectively score them right now. So, that's what we're building. That's what DIN is in the agent native marketplace and you can follow us on DIN build on X and we'll share more of what we're designing. Cool. Thanks, everybody.

>> [applause]
