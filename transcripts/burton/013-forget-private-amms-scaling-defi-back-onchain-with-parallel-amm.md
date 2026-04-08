---
title: "Forget Private AMMs: Scaling DeFi Back Onchain with Parallel AMM"
speaker: "Xiangru Ma"
organization: "Crystality"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=d4EdjOwdi4o"
transcription: "youtube-auto-captions"
---

# Forget Private AMMs: Scaling DeFi Back Onchain with Parallel AMM
**Xiangru Ma** (Crystality) --- Burton Stage

Okay. Uh, good morning everyone. I'm DTO from the crystality and pred team. I'm super excited to be here. I got limited time so I'm going to like dive straight in. Um, so today I'm going to share the recent uh progress that our team has made on scaling sequential MM via a parallel architecture. So our target is

to scale DeFi back onchain. Let's dive in. So firstly when we talk about constant product MM which is unis swap or the other mm we usually heard uh that is indeed um we we love it and we think it is the great greatest innovation probably happening in the device space

for the past five to six years and uh for the first time traders get to trade without any intermediaries and uh indeed instead they interact with a smart contract via the bonding curve. curve. So every swap moves the reserves along the bonding curve. So the MMA is actually constantly searching for the

newer price and so therefore I would invite you to consider constant product MM in this specific lens that it is indeed an onchain continuous price discovery engine and uh we know for most of the short tail assets like Bitcoin, Ethereum, stable coins

etc. and actually the most majority of their liquidity and trading volume happening firstly on a centralized exchange. So what we have here is indeed a reactive feedback loop. So we have the in external which is the market price happening on the centralized first reach a new fair price and then there will be

the arbitrators who are the informed traders wanting to like capture this price difference for profits and they want to step in and there will be the competitive arbitrary trades happen and then either it's arbitrary or it's normal trades it's just trades so for an AMM the reserve of updates the price

changes and the AMM price actually converges towards the market fair price. Therefore, we want to come down to this conclusion that for mainstream assets, a constant product MM largely function as a passive pricey mechanism and uh the either MEV or arbitrary training activities we we think is one

one of the very important process of correcting the price. We can't eliminate them and we shouldn't. And there's a very important question we ask here is how fast does the AMM price converge to the fair price. And when we talk about fast, there's a dimension of time. So let's look back at sequential mm. Trust

me, we love unis swap. But unis swap does come with a bandwidth constraint by design. say during the high volatility market times there will be huge amounts of transaction actually trying to access the same liquidity pool to give you a concept about how this concentration looks like I got a number here so indeed

the leading 0.17% of unis swap v2 pools process almost 40% of the total swaps that's huge and that's quite concentrated so there are the hot spots on a unis swap It has always been and it will be in the future. So in this case um there will be a single shared asset reserve state

accessed at the same time by huge amounts of transactions. There's one global right lock over there and unis swap just designed in this way all swaps must serialize everything like transactions are executed one by one and then what does it cost? We got this huge volume transactions that intensify the

state contention actually and then the gas fee spikes transactions queue you up and there could be transactions spilled across multiple blocks and there will be therefore there will be an extended steel price time window remaining open for the arbitrators and for the LPS that's terrible news

because we have this concept of loss versus rebalancing as known as LVR are actually it is one form of MEV that exploit more value than all the other ME forms combined. So it is a serious condition and the extended time window just make it worse and this low this lowrisk arbitration window will be

exploited by those arbitrators. They're actually very well positioned to exploit this slow updates and that indeed cause structural cost to the LPs. LP pay the bills. LP pay the bills and arbitrators make the money. So price discovery becomes a very competitive killing in

this case on unis swap. So seeing this bottleneck the market has their own alternative approach as private MM. So what does private MM do is is it stop waiting for price disco discovery on chain. They moves it offchain and actually they have their own what they call pricing prediction

models collecting all the information like they gathering like order flow signals and market data aggregation and uh just push this uh offchain information onchain and then at the end uh smart contract and blockchain only reduced as the settlement layer so you can barely call it mm because they don't

have the the the constant product anymore and then you know there are plenty of benefits we're going to talk about is but is really extremely good using experience for the traders because there's no near zero slippage and it's extremely fast uh and for the market makers they love it because it it is

they it provides extreme capital efficiency for them but no you know I'm going to talk more about the trade-offs the trade-offs area is much bigger than that than that box so for the traders for the trade-offs one we have the the private MM provides an opaque execution they're doing everything offchain and

It's almost like a black box with closed source models that it is imposs impossible to audit it and also there are the hidden order flows probably sent privately to the market makers and there will be censorship mechanism surfacing as operators can actually filter or reject some of the what they call toxic

order flow. So that creating a selective access it may only w some of the orders and to for execution. And then the most important thing the the the worst thing let's say is the frag fragmented and isolated liquidity because liquidity is completely completely offchain. So that liquid this

kind of liquidity is completely isolated and not composable anymore with any other defy building blocks we have in the space that actually make DeFi powerful. So we are asking if private MM is the industry response then the DX aggregators like say Jupiter on Solana

actually are becoming the new centralized exchange probably the new Binance and what's the point of decentralization of blockchain. So the fundamental ask a question we're asking here is can we scale price discovery without leaving the chain we keep everything on chain is it possible to do

that we come up with this solution what we call um parallel mms it's actually um based on a parallel programming model that we have been working on few years and now we implemented it in the parallel mms and to to to have this faster feedback loop onchain so our ideal case the target would be starting

from the same ideal price sale price parallel MM would need much shorter time than sequential MM to converge to the fair price and then uh we we got this reality that our execution speed is two to six times faster than sequential MM which translates to 75% t down in time in per

mispricing half-life and before diving into details I would like to share an inspiration of this parmm design is uh our based on our observation of unis swap v2 the numbers are here actually the majority of transactions make negligible price impact they don't have price impacts to

give it a number over 85% of transactions would make a pi price delta less than like 1,000 so our approach is that we paralyze the transaction of them we route we would route the large transactions to a global pod for the large transaction for the transction that actually have a price impact. And

this one maybe hold probably 80% of the total liquidity. And all the small transactions will be routed to the smaller paws for for parallel transaction that and that each of them may hold only 5% of the total liquidity and we also have that periodical synchronation and on demand rebalancing

to synchronize the liquid assets the reserves of them across all the pods. You may ask a question. You got the you got your liquidity splitted. Does that inter like introduce worse leapage for the traders challenge accepted. We have to redesign the whole algorithm. So we have this algorithm with that if a trans

small transaction is sent to a pod they they we don't quote the local reserve the price is calculated based on the approximate approximate total across all the pods. So are the large transactions. So we have we kind of we we have to keep this pricing with a acceptable range of accuracy in our design. I won't go get

into the details of this like uh equation but you can ask me later. Let's let's let's chat about it. And we have this performance validation here. We got firstly let's look at throughput the execution speed is indeed 1.8 to 5. X uh 6x TPS versus sequential MM and that translates to 70% reduction in

convergence time to the fair price and for the performance of fry the price deviation will remains 1.5% at 90%age when we have four sub pods and that is performance just to to prove that we have built up everything and we have stress tested it and uh we were here last year at ECC introducing the

underlying programming model which is crystallity and now we are here crystallity is fully composable with solitary read and ethereum clients and we are currently running a validator implementing crystallity on testn net and that enables like parallel execution as the execution layer of ethereum so

that's what we do on a on a higher level so what's next we're gonna yeah okay I'm I'm gonna stop here I'm happy to take what whatever questions you may Okay, Joseph feel got a question? >> Sure. >> By sequential AMM, I assume you mean unis swap. Have you compared any of

these metrics to like a hyperlquid? >> Uh, not really. We we we we look at more on like unis swap and constant product mm only. Yeah, we don't look at it order book thing because it's not just comparable to like decentralized order book or whatever order book you are operating. So, so that's why I mentioned

constant product mm like repeatedly in this slides. Yeah. >> Yeah. >> Because that's why hyperlquid is so competitive. >> Yeah, I I I totally agree with you and I think uh the slippage we have right now is is the number is quite close to

sequential mm and that's I think the best we can achieve. But this is the first few steps we we we are just we just built this central building blocks of this parallel mm the architecture. So we are adding more mechanism and probably more um I don't know the extensions to it. So like unis swap uh

the hooks that they have in unis swap v2 making everything better make the numbers better make sleepage even much thinner than what unis swap has and that's our goal. Yeah thanks for the question. Anyone else feel free to chat with me? [applause]
