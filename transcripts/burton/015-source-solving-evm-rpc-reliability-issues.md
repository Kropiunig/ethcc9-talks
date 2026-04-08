---
title: "source)) - Solving EVM RPC Reliability Issues"
speaker: "Kasra Khosravi (Goldsky (and also erpc open"
organization: ""
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=DMFvsvPZAec"
transcription: "youtube-auto-captions"
---

# source)) - Solving EVM RPC Reliability Issues
**Kasra Khosravi (Goldsky (and also erpc open** --- Burton Stage

Morning, morning. Uh I hope you guys had an amazing Easter experience so far. Um my name is Castro. I am one of the core builders and contributors of ERPC, which is an EVM RPC proxy tool. RPC built for two totally open source under the team of Goldsky and a ton of

web 3 important projects including Circle, Euler, Moonwell, Morpho, a ton of other teams are using it in production today. The main topic of today is solving EVM RPC reliability issues. But it's important to take a step back and understand how does the stack basically

looks like. And it's important to understand there is a big difference between the web 2 and web 3 world when it comes to basically data because in the web 2 world, um if you're building like a finance app or anything, you don't start from day

one with a ton of data. You start small and then as you grow, your data solutions also need to evolve. Uh but in the web 3 world, the story is totally different because uh let's say from day one whether you're building a wallet, dapp, or something, if you're also really small,

you need to handle a ton of data from raw data, which is like RPC or also transformed data. So, we just need to be way more basically sophisticated when it comes to like all the data solutions. Uh and the way we basically ask the blockchain for the data is through a standard which we call a RPC, right? So,

uh a DeFi app just sends a lot of eth call requests, uh let's say indexer sends a lot of eth get logs requests, a wallet sends get balance requests, and basically through JSON RPC, we ask the blockchain about those data. Uh but there's a lot of inconsistency when it comes to different providers.

So, those basically applications send the request to what we call upstream layers. Upstream layers are your like best spoke RPC providers like Ankr, QuickNode, and Alchemy. And uh there's an inherent problem at this layer because um each one of those RPC providers are working with a ton of

infra. Like, you know, you have your AWS, Cloudflare, you know, they have outages. Uh sometimes like RPC provider is in one region and your let's say your customer dapps is in I don't know US and the provider is in Europe, there's added

latency, there's outages, there is uh node crashes, all those things. So, basically, uh there's a lot of fragile points that can happen and the kind of the rippling effect is your users gets impacted. Uh um they cannot see something on their wallet or the basically dapp freezes.

So, there's a lot of basically issues. And uh as I mentioned, there are multiple infra layer uh points, but one of the main ones is what we call like a execution client, right? So, these are like geth, rest, besu, nethermind, all those things. Uh and also they have issues as well

because again to maintain them, you need to have devops expertise. There could be like logic issues uh inside the code. So, we had actually issue maybe like few months ago that one of the these clients, I'm not going to name, uh but had a issue with the log index in the get log. So,

uh basically any RPC provider who was running that version was giving wrong get logs to their uh users. And it's so subtle that they don't know until it happens. So, again, um a lot of a lot of uh issues basically.

And that's where kind of ERPC comes in. ERPC is like a let's say a captain that sits on top of your RPC stack ship and I'm pretty sure all the people in this room, if you're doing anything meaningful in production, you need like you need to be on multiple chains, you need to be like running multiple RPC

providers. Um Um so, basically, ERPC has all the EVM context about that and make sure that kind of every single RPC request goes to like the most optimal node. You can optimize it for latency, you can optimize it for data integrity, you can save cost through caching.

I'm going to give you few examples. So, for example, imagine you have multiple RPC providers. One of them goes down. No problem. RPC has automatic failover. What if one of them is a slow? We have hedging mechanism. We send parallel requests to multiple nodes and whoever gives you the response fastest, we're

going to accept that. What if there is a RPC provider that kind of gives you wrong results? We have consensus So, for example, if three out of four nodes agree on the result, then only then we're going to kind of accept that result. So, again, a lot of these kind of

built-in EVM context and knowledge to make sure that um your RPC stack is reliable. And I like in the past one or two year, I have probably talked to 100 different teams when it comes to RPCs and funny enough, a lot of teams build something in-house for this um and a question they

ask is like, why can't I kind of put a like traditional LB solution on top of my RPC stack like Nginx or Envoy? >> [snorts] >> And the simple answer is you need to have EVM knowledge baked into this uh flow because uh in the RPC world, it's not about a node is up or down, it's

about like the health check is way more complicated. Like, how far away is it from the tip of the chain? Uh let's say how what is the latency, like all those things. Or for example, it's not about simply like a round robin between multiple nodes because again, a node can be like faulty and it kind of

keep keep giving you wrong results. So, you need to have like method and finality ever kind of, you know, uh all those things basically built into your proxy service. So, now I'm going to give you few production examples that again, based on talking to different 100 different

teams, these are like the common issues that happen. And I'm going to tell you like how ERPC basically helps with uh those issues. Uh so, a common issue is that your uh basically RPC provider goes down, your indexer stops working, your front end kind of, you know, hangs. And then

your devops person needs to wake up at 3:00 a.m. in the morning and kind of patches that. Uh with ERPC, no problem. It just it happens, the retry happens automatically, zero downtime, there's no kind of any need for manual integration. Um and it's also important like with

ERPC, we give you all the knobs. So, for example, if you run ERPC without any like manual config, it just works out of the box because we have made a lot of same defaults, but you have all the knobs basically to uh kind of tune it based on your environment. So, for example, if latency is more important to

you, you can configure it. Or for example, if data quality is more important to you, you can configure it. So, in this example, for example, imagine an upstream has an issue and it could be maybe a transient issue, so it can recover. So, we have the upstream level basically retry, so you're going

to retry that upstream up to two times with this amount of delay. And ERPC also has some knowledge that for example, if the issue is uh non-retryable at upstream level, for example, the data is wrong. So, basically, there's no point of retrying it. Then we go to the network level, which is like your

mainnet or base um and imagine you configure like four times um retry. And then if all the attempts fail, then only then we're going to uh return the error back to the user. So, again, much more robust when it comes to and sometimes you don't even know that issue happened because ERPC kind of handles it

automatically. Another common issue, probably this is the most important slide, is so subtle. Some RPC providers give you wrong results. Empty get logs, incorrect get logs, missing transaction. We actually have an internal dashboard that literally at every minute that we're

talking now, major RPC providers are giving wrong results. Uh so, the way ERPC handles it is through like a consensus mechanism, right? So, you like a cross-check between multiple nodes. And again, it it can be really elaborate, but for example, imagine you

send a get block by number request and three upstream gives you like this result with this hash, but upstream for example three gives you a different hash, right? And then because you have defined a three out of four threshold, you're going to accept this result because

three of them agreed. And then you're going to mark that upstream as a misbehavior. You're going to punish it. If it happens more than enough, you're going to cordon it. And then you can put this like misbehavior somewhere in S3 or something, so you can go back and look

at it. And um sometimes also like this um there's custom like fields in different RPC responses based on different clients. So, um it's like it's not there's no point of comparing that. For example, you can basically ignore those

fields. So, this just makes the like data quality, data integrity way, way more robust. Uh we actually use it in production with billions of billions of requests. And a lot of teams also including uh Circle is also using it. Another problem is a slow responses,

right? So, imagine 5% of your requests uh actually so sometimes get block by number is really fast, but eth call or transaction or debug are really slow. Uh and again, ERPC has the EVM knowledge, right? So, you um can you see that for example, eth call for your request keeps uh you know, hanging

and then, you know, the front end not work and all those things. So, we have a lot of built-in mechanism in ERPC for like make your RPC uh responses faster. But one of the most important one is what we call a hedge mechanism. So, imagine you send a get block by number request and then uh for example,

you can configure like if it's slower than 100 ms or 50 ms. Or also if you want to define it like more dynamically, like if it's slower than P95 latency of all my metrics, uh then I'm going to send X number of parallel requests and whoever gives me

the response fastest, I'm going to accept that and cancel all the other response requests in flight. So, it just makes your RPC response way, way faster. You don't have to wait for a slow RPC to kind of come back to you with a response. Um another one is really common for

indexers, so they send a lot of get log requests to kind of get the events on blockchain, but a lot of providers have like limits on their let's say nodes. Uh with ERPC, we have automatic, you know, um range splitting. So, imagine you send a 20K eth get logs request, uh the two providers each one have like a 10K

limit. Uh if without ERPC, you need to manually kind of like this information inside your let's say indexer or back end. Um but with ERPC, like this kind of uh 20K would be broken down into like two 10K ranges and then we get like all the logs from them and then kind of merge them

together in the end. So, you get the response without even kind of knowing about it. The most This one I'm really proud of because this is like the most important what makes ERPC basically different than any other, you know, LB solution, traditional LB solution, is we have a

dynamic scoring mechanism in ERPC, right? So for example, imagine at every point in time, you know, anchor quick note Alchemy, whoever it is, they have a profile. They have this amount of error rate, this amount of, you know, block head lag, misbehaviors, all those things.

Without ERPC, you need to kind of, you know, round robin like this one. I'm going to go to this and then the next request, I don't know who is it going to go to. But with ERPC, you can actually configure this. You can say, "Okay, for example, latency is super important for me. I need really fast responses. So I'm

going to give it like a really high weight. But for example, I don't know, like error rate is not that important. So I'm going to give it a lower weight." And based on this profile, every node, every RPC provider is going to get a score dynamically every second. And then based on that, let's say the lion's

share of the request goes to like the most optimal node and, you know, vice versa. So this one makes makes basically like every single RPC request goes to the best node basically, which is very, very useful. Shameless plug, all these kind of things

that we I talked about and probably a thousand more is built into our also enterprise product. So you can run ERPC fully open source, bring your own RPC node, but we have kind of customized all these, you know, different data quality, latency, all these issues into our Go Sky Edge RPC

product. We also have our own custom node solution. So we have like a It's not a traditional like a node basically. So it's super fast when it comes to tip of the chain and historical data. We have multi-region. So when a RPC request we're going to route it to like the

closest server or edge node closest to your user. So feel free to use it or talk to me about it if you like. That's it. Thank you so much. Any questions? >> [snorts] >> If I have a a doubt managing 15 networks, do I need

to run 15 ERPC instances or can I only use one to route to the right networks by chain ID? Single ERPC. You can also run it We have also like a shared state. So imagine you have multiple pods like each one of them share like the latest blocks. So you don't need to do that. Then you define all those networks

basically inside ERPC and just works out of the box. You can also use caching to save RPC cost as well. And then the other one is good for the next
