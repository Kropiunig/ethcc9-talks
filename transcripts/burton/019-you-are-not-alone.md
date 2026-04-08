---
title: "You are not alone"
speaker: "Tümay Tuzcu"
organization: "Cambrian"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=dFnESUbFKk4"
transcription: "youtube-auto-captions"
---

# You are not alone
**Tümay Tuzcu** (Cambrian) --- Burton Stage

hearing me. Uh I'm the principal engineer at Cambrian. uh the next 10 minutes I will be trying to explain what we like from Ethereum and then the thing that's like like is a very tiny design choice in the EVM and that exposure turns into a multi-billion dollar ecosystem

but uh I believe the potential of that tiny design choice uh is not realized yet there's a huge gap and we call with the intelligence gap. So at Cambrian we are be trying to solve that problem the intelligence gap. Uh I believe I can click this right. So I will start by the idea the tiny VM

choice. So uh the control theory like basically explains what is observability says that if you can uh get the most of the system state uh out of its outputs actually it is called observability. So I believe uh didn't just do the execution part optimizing the execution part actually it's it's also optimized

the uh exposure. So what is it is basically we have some very low-level op codes called logs okay log zero to log four uh which is based for the solid events it's like whenever you do a swap whenever you change a liquidity actually you uh emit an event in the so contracts but it makes it so easy that easily

other part uh other other parts like indexers analytics aggregators ers can easily watch it and collect the data. There is another uh example uh I'm not saying that Solana is bad but the the there's a difference because actually if you want to have that state like how much swap has done what is the state of

the liquid pool you need to go really in deep you need to find out the instructions uh there are some specialized log strings even I have seen zk compressed uh data states inside the solana so you need to go deeper and it's not easy to integrate. So that difference really matters

because when the integration is easy, the other ecosystems can uh basically do what you cannot do by yourself. Okay. So there's the proof of it by the way with the numbers. So probably most of you know unis swap v3. Uh basically unis swap built the liquidity pool idea if you ask me like

it's the greatest thing that's done in EVM. The idea is you basically lock some tokens and people come and do the swap but it seems like basic but unis swap also designed their exposure really well their state really well. So others can came in and build what is not built

inside the unis swap system and one of them is which I worked for a very few weeks is an aggregator odos uh they just watch the state know which liquidity pools have enough liquidity to do the swap and create a I'm from an industrial uh engineering background create a really great solution to traveling

salesman problem actually you you try to find the best path Okay. Uh usually if you go for other aggregators they have one hope or two hope by hope I mean you go for one liquid pool to another then you finish the swap but uh due to the exposure of the liquid

pools or has the capability to do it like 10 or 12 times and it generated $40 billion volume in the first year over unis swap. So as you see this observability bring in a huge exposure and that exposure turn into a huge volume but there is a problem there's a but in it why because this data which we

call event data is not enough for generating intelligence by intelligence your protocol cannot decide on it. Why? Because it needs historic data. like whenever you want to have intelligence like analytics it's nearly impossible to execute it. So it creates a huge gap if you ask me we call it like basically

intelligence gap. So I will try to explain it in in a very simple example. So in the left side you see that someone borrowed 10 each. Okay. So this data can be used by liquid pools. Okay. But whenever you want have something like is the market safe to do some let's say another uh lending or

thing based on the idea you can't do it because why if you want to do it on chain you will spend thousands of gas basically you will lost in it it will kill it and if you want to go of chain which is oracles yeah now you lost the trust idea because the oracles you're basically looking for an AWS as lambda

or a centralized database. So in Cambrian we really want to solve this problem. Uh we have been working for a year. Uh so I will try to explain what we have finished. I feel like everybody's liking animations. So the idea is like we don't want to introduce a new oracle. Basically we want to

reinvent the stack as much as we can. I'm coming from like I'm an industry engineer but I've worked for more than two decades on databases how quorums work how uh you have a cluster of data so we understood that we need to have something called verifiable data network so each node is like collecting the

intelligence the data and agree on that they have the same data this is the basic idea a blockchain has so we introduce that trust back to the inter the to the analytics. So the next thing is we understood that the the idea about certainty the trust is differ from application to application. If you are

doing swaps in few dollars or let's say your volume is small you don't need to run all the network like thousands of nodes to get get into a quorum for that for a number. You basically request let's say two or three is more than enough. This creates a cost efficiency. So it is not like you ask the network a

data and then we basically charge you thousands. You can easily say oh okay I'm happy with two or three or I'm happy with like we also introduce slashing saying that okay uh I want to run this uh I I can I don't want to say query I don't want to say uh data I basically it's intelligence I want to have this

intelligence uh by slashing for example the next thing is uh it is not here but the idea is we understood that like the protocols is not just onchain, they have off-chain components uh like web UIs, agents, even they have their own rest APIs. So we bring in the standard API the web to the old but also it helps you

to get fast data from the system without chrome and lastly uh at day zero we understood that we shouldn't be doing anything for the let's say uh developers to learn everything inside this network the how to create this pipeline So we try to

uh achieve this with agents. So the next two minutes I'm going to show this as a demo that I recorded. Uh so this is WS code with cloud. So I asked it to implement a full under lending protocol. The problem about underco lending protocol is like you

basically you have uh less collateral for the same amount of money that is borrowed and you you need to create some risk calculation out of it based on whatever you have. And funny enough actually if you ask like this it will create the uh risk calculation based on the amount you borrow which is like

overcolaterized. So it's useless. It's static. like 80 not 80 percentage of the LTV or something. So I come up with another idea. Wow, it goes really fast. Uh I come up with a new formula which is called pulse which is based on historic data. Uh I need to look at this. It's based on I I'm not the risk actor.

So it's based on frequency, severity, velocity and concentration. So I ask it to be implemented Cambrian. So the agent our Cambrian agent which is which can understand the formulation and generate a pipeline data pipeline for it and create the required changes inside the protocol. Uh the last one is like as you

see the quorum like especially when you implement this is initially implemented by one. So I wanted to have at least two data nodes to execute this query or data or intelligence. So it updates and finished it. This is the language we try to build. Uh that is that can extract that information.

Uh and finally actually I want to bind this to the web UI. A user can get in and do the lending. So this is the output. The result we we basically copied from morpho. Sorry for that morpho guys. So whenever you connect your wallet actually as you see the pulse risk

calculation is directly there. Uh yeah so this is the end. Uh and lastly thank you uh the idea about you are not alone. uh we want to show you that the exposure you create in your protocols can turn into a multi-billion dollar projects. So you

are not alone. Please design with structure uh and keep in mind that that exposure will help you gather more growth. And the next one is uh till now the intelligence part is missing in onchain execution. So you're not alone. We basically bring it with Cambrian. Thank you. That's it.

Wow. Any questions? Probably there will be any questions. Yeah. Um, does it work? Oh, okay. Uh, yeah. Thank you for the presentation. I actually uh wanted to ask uh what do you think of verifiable logs ERC which seems

to be achieving pretty much the same goal uh just on the like base layer of the network. Uh so verifiable looks is like basically while I was working graph actually I have seen them uh it is some part of it basically but when you build over it that's the most important part you need

to execute it you need to calculate the numbers out of that log even you you keep it in your protocol the problem here is if you calculate a huge average weighted average have you ever seen the numbers Actually let's say let's go for a unis swap USDC uh BTC pool okay it's like millions so

even calculated per lock will cost too much uh another idea is sometimes you can't do the m1 plus state that is something like for example summation is something like this so you got the sum till now so then the n could introduce another sum okay you can optimize this uh gas but

you can't optimize uh weighted average or standard deviation and also the intelligence about like this like usually you also introduce some external factors. This is not just EVM events. This is something like states uh instructions and maybe an exchange rate uh that you trust in your protocol. So

you need to introduce it. Yeah, it will also act like an oracle. So I hope it answers your question. Uh probably the missing key while I was when I gave back this to chat GPT or Gemini like if you are an investor or a developer what would be your question is the blackbox. I didn't explain this. The

blackbox is like basically we materialize the data. The difference is you usually when you go for an oracle they will execute the query which will create a huge delay the summation the average so we materialize it per block that is the idea so your data will be always available it is not based on your

query is it's not based on your request that's it thank Thank you.
