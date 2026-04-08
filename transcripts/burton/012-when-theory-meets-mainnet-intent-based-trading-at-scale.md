---
title: "When Theory Meets Mainnet: Intent-Based Trading at Scale"
speaker: "Mariia Keiko"
organization: "CoW DAO"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=eAbIST7sf4Q"
transcription: "youtube-auto-captions"
---

# When Theory Meets Mainnet: Intent-Based Trading at Scale
**Mariia Keiko** (CoW DAO) --- Burton Stage

Hi everyone. Salute. That's all I learn in SP uh sorry in French there. when my French starts and ends I asked how it would be good afternoon in French and the person answer it was so complicated to me so so I said okay I'm going to stick to salute but I would love to learn more being

here in K it's one of my favorite places it's one of my favorite conferences and kudos to all the organizers to make it happen I feel like it really takes lots of efforts and we have such a great people here and lots of things to learn this week and also this is the last session for today and I see the full

room so kudos to all of you for joining us today. All right, let's start it. I'm Maria and I'm representing cow today. Uh we are decentralized autonomous organization of developers, market makers and community members. Our main product is cow protocol with scow swap UI on top of it.

And today I will talk about when theory meets mainet intentbased trading at scale and you might ask why only mainet the answer is pretty straightforward because we have the most volume on the mainet and what I want to the idea of today's presentation is to talk about the reality is do not talk only about

the theory and all the beautiful stuff and so but also what can happen what can go wrong how the UX s work and what how the solver competition works and what are the ways we are solving that and uh bringing that closer to the users and so so raise the awareness and ensure that we are improving and growing and making

this ecosystem a better one. How many of you knows what intentbased trading is? I assume that many many of you all right so I don't need to explain much it's h pretty self-explanatory uh in short intentbas trading means you don't specify how to execute a trade

what you do instead you specify what outcome you want to get and the solvers are the best the figuring out the best way to achieve what you would like to achieve solvers optimize the execution across um multiple dimensions price routing matching or um matching rather than

locking execution into a single path. So what they do they also ensuring they provide you with the best possible surplus with the best possible price protecting from the mess and so it's like ordering a right for for example in the traditional defy you drive yourself um using the exact road

and what we do in 10bas get for example to the airport using the best price the best road the best one for the user And those who are driving that are solvers. They compete to serve you and provide with the best possible solution. Who are the solvers? By the way, I really like the picture. The cow looks

really great. Who are the solvers? How many of you knows my team? That's great, Jacoba. That's great. Who else? Okay, we have quite a few people who knows who are who solvers are. Okay, so here I will explain a bit more and also

open to have any questions in the end of the presentation if you have any. So just keep that in mind. Solvers are independent actors who compete to execute the um users traits in the best possible way. They take your intent, find matches or roads and compete to produce the best solution. And by the

way, anyone can become a solver. The solver can be an individual, it can be a group of people, it can be an institution. And so we do have very clear paths how to become a solver. You need to provide with a bonding. Um if you don't have your own bond we also providing with our bonding pool and you

could have more information about what does it mean and what do you need actually to become the solver. It's pretty straightforward. We also help with the onboarding. At the moment we have 30 plus solvers. We are onboarding more and more solvers. And the great thing uh about that that once solvers uh

start working with us uh they are sticking to that we have had in the history only indeed few solvers who stop working or who start uh contributing less I would say but they are pretty satisfied and we are glad to on board and provide more information to the new possible solver. So if you if any one of

you would like to receive more information, I'm happy to answer any uh questions in the end of this presentation or meet you on oneonone or I also will attach references in the end of the of this presentation with more information how to become the the solver, what do you need and and so on.

And um this is on the right for me you see the traditional batch auction on the left you see the fericcom batch auction that's on the UX side of the transaction how it works in the past we had traditional batch auction starting last

year uh from June if I'm not mistaken we we do have fair combatorial batch auction and why it is better for multiple reasons. So as I said we have 30 plus solvers. We are deployed on 12 chains for now. We also plan to be deployed on more chains in the future. Some of the

chains like for example the mainet is the bus the busiest one. It has the most um volume. It has uh the most competition and so on. What we want to do we want to incentivize the solvers more. We want them to win the exe the executions. if you want them to be profitable and so so the difference

between batch auction and the fericcom motor auction is that in the past and the batch auction you can have only one winning solver and also they were able to submit one bit now what we have in one transaction we can have multiple winning solvers and we they also can submit multiple bits that's a gamecher

we see lots of positive changes since that we also receive lots of positive feedback from the solvers and uh this is one of the solution we found for providing better price for the users first of all because users for us are always the first and also how can we incentivize and how can we motivate to

have more solvers um how can we just ensure that uh this is the fair um competition that we don't have always the same solvers winning um and so on. So how the entire ferom commuter auction works. So first of all it's a very very very complex thing. I can talk about that hours and hours

and there is always something you know uh we could miss and can catch up on that later and so so there are lots of things happening on the yaks and also because that's so complex some um it's um very hard to explain in 20 minutes that's why I'll just focus on some uh

you know more generic uh things so for example when you go to cow swap UI what you do you just submit what um you would like to sell and what you would like to receive that we call the intents. All the intents we are gathering in the order book and that's exactly where the solver competition is happening. So

what's happening we also have um autopilot which uh basically pre select um the the right solution and so and what do we have in that order book we have solvers competing and finding the best possible solution and in the end they submit their solutions and we have multiple winners.

This is the entire again like it's very generic but the entire um order flow how it goes. We have the trading intents. Then they go to the order book. We have solvers who competing to provide the best possible solutions. And the way how they do that they can connect peer-to-peer. That's how where a

coincidence of wants cow comes from. Basically they connect with other person with the other intent who is training the same. or they can connect with the liquidity pool or with the MMS or they can have the ring trades for example some part taken from the uh peer-to-peer some uh part taken from the liquidity

and so in the end we are submitting the the winning solution on chain in one transaction and all the competition is happening offchain. All right. So, fericcom better auction and solver competition are very powerful but it also means all the complexity moves to

the solver layer. So, they are the one who are responsible for providing the best possible price. They are responsible for protecting from the MVS and so solver compete to extract to extract mess to provide the best surplus and pricing for users

and the theory is everything is the exe the execution is predictable. All they may be captured effectively and everything is just great and perfect. What can happen in the reality is that solvers behave unpredictably or some some me vectors may vanish or your order doesn't execute

at all. Solvers play too safe and so the good thing is that for example if your order doesn't execute you're not paying anything for that of course uh for if something happen with the am user is not uh paying that uh that's everything on the solver part. So what we do we always protect the users we always pay

attention to that and uh we always inst incentivize the solvers and look closer to all the things which for example uh should be improved going forward. Solvers operate under time pressure. This is also important to to be aware of. They compete with each other and

somewhat they also have the uncertainty. They don't have the information about the other solvers, what do they submit and so and even in a well-designed system like cow swap, they don't have perfect information and so they don't have infinity time. Each transaction lasts around 8 seconds. So they have to

be pretty fast and since um last years we indeed improve a lot our time to execute and uh they also compete against each other. How do we improve it? So this is something what we are constantly aware of and this is something what we constantly improve that. So the first

thing which we those are just some of that on the background there are many many many things we are working on because it's very complex and the solver competition itself is very complex and we always put lots of efforts to ensure that the users are in the center and they have the best uh possible outcome.

So we introduced the fericcom auction which I have explained to you already. At cow protocol solvers are getting rewarded and what is important to mention is that we are the only one who provides rewards to the solvers and uh you also can get more information the way how we do that and uh for example

even about the surplus and uh who is the first solver the second solver it's quite complex uh but we are very proud of that and we are uh we are very proud that we can incentivize the solvers we can motivate Um and we can make always the solver competition even more fair and so uh we have more diversity. uh

there are considerable ones, AMM, string trades and so the way how they can execute the trades and we constantly improve on our UI UX and solver competition and why is it so important like um we could we could just say everything is great, everything working well but

why we are constantly work uh thinking about that because this is the market where we want to achieve bigger adoption. We want to come closer and to have more users who are not even familiar with that much with the web 3. So we really want to ensure that the the UI works smoothly, the UX works

smoothly, that users then don't need to think about like what to click, how to click and so and that solvers are incentivized enough they indeed provide the best services to our users. All right. So if you would like to learn more about commit auctions, you can check the cap67.

I will also link that in the end of the presentation. We have um in short the way how it works in the order book in the afterpilot. Um once uh solvers receive the intents they submit their bids after in autopilot we f we filter and fair solution uh or the one which are not serving the users ranking them

and then reward the winning solvers right those four steps if we speak about that in short uh solver competition is very complex and constantly evolving and um and progress comes from embracing that complexity not avoiding it. So this is the message which I would like to leave

you today and let's become better every single day and be mindful that there is always something we can improve. What is important is to be aware out of it of of it and also to do one step at a time to ensure that we are making this world a better place that we are making web a better place. So, thank you so much. I'm

Maria and um it was really a pleasure to be here with you today. I'm very happy to talk with you if you would like to to leave you more with the references. you can scan this QR code and um with uh how to become the solver all the CIPs are interested for this um uh topic and um we also have uh open roles and uh

if you are interested in any of our opening roles talk to me because actually I'm the right person I'm leading people department and uh recruitment at KA would be very glad to talk to you at the moment we have three open roles, back end engineer with Rust, visual designer and integration

engineer. We also have the referral program. If you know anyone who might be suitable for our roles, uh refer them and we pay up to 6K USDC for the referral person to the referral person. We also at DAO we have many contributors from the grants. If you see anything could be improved at cow protocol and

you would like to contribute, please um visit this QR code with more information or just our website cow.fi and you will learn more about how to submit the grant and if you would have any questions feel free also to ask the community on the discord. Would be glad to stay in touch. Those are my details uh my social media

and that was a pleasure to be with you here today. Thank you so much. Any questions? >> Thank you, Maria. How do the solvers deal with KYT? So, is there a possibility of freezing the funds? For example, if the uh solver treats us as like a yellow or a red crypto. So, is it

always non-custodial and without any filtering? You mean sir, thank you so much for your question. You mean sorry I just like to you mean phrasing the funds from the solver or from the transactions itself when it's happening? >> No. No. If user sends the transaction

via KY swap, I' I've used your protocol. It's great. >> Yeah. But I don't know. Is there a possibility that some solver will treat my crypto as risky and it will freeze the funds or and will not return it in some case just because the KYT showed something.

>> So so far we didn't have many cases like that. Usually it's always on the side of the user. So there is they receive the notifications but not on the side of the solvers. For example, if we the solvers are protecting the the funds, but it's uh not possible to freeze them from our side.

>> Okay. >> So, you mentioned that there were 30 solvers. I'm curious roughly how is are the sort of solutions distributed? Is it very dominated by a couple of them or very even? >> Great question. Thank you so much for that. Indeed, we do have a couple who

are dominating, but um we also have many creative solvers who are smaller and the way how we want to motivate them to become even more creative and to stick to the market. For example, when we have when we have the new solver, instead of putting them directly on the mainet when where the competition is tough, we are

um putting them into the smaller chains where they can get more profit at first learn how the competition works and they then decide to go to stick to the uh few smaller chains and also to go to the mainet and so so we really want to ensure that we're not only incentivizing the solvers who are dominating the

market but we want to ensure that we have variety of the solutions and variety of solvers who can benefit users can benefit out of it. Yes. >> Hi, thank you for the presentation. Um I was wondering about uh who's responsible for eventually ensuring that a solver

solution lands on a block. So um if I want to submit a an MV transaction, for example, if I'm a searcher and I want to submit an MV uh transaction, I'm responsible for uh bribing or or tipping the block builder appropriately. In this case, let's say I'm a solver and I want and I found a solution to a uh to

a given opportunity. Um who eventually is responsible for making sure the builder is appropriately um uh awarded and that eventually that solution is going to land before the route I found disappears.

Liquidity disappears at a given price or whatever. Okay. Uh thank you so much for the question. It's a complex one. So we do have a mechanism which goes for example autopilot which um which is responsible for filtering the solutions and providing which are

the one the best one um and winning solution for for the users. Also on the other hand we are always keeping an eye on the any possible malicious solvers and that's also the reason why we have the bonding pool which they submit and it's a quite a big one. It's 1 million of of USDC and 1 million and a half of

cow tokens. So it's quite a big and it's it's a very little risk that it can happen and if it's ever happening this is something what we closely keeping an eye on it because we definitely it's not it's not something we we want to have 100%. Okay, this one.

>> Yeah, the last question. >> Thank you. I just wanted to know, do you have stats on how much uh solver can earn a month because I guess it's the best marketing to on board more solvers. >> It's a great question. Uh I believe we do and all of our data is on June. Uh so it's accessible. But if for any by any

chance you don't find the information which you're looking for, you can always write to the discord or you can always write to the telegram group dedicated to solvers and we would be and we would be more than happy to provide you any information because this is a very good one. Thank you. Thank you guys. It was

really a pleasure to be with you here. Enjoy the rest of the conference and enjoy your evening. The first day ended officially.
