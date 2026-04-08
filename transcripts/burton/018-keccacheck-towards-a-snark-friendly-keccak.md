---
title: "Keccacheck: towards a SNARK friendly Keccak"
speaker: "Greg Swirski"
organization: "Reilabs"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=h0kg2WB9vEc"
transcription: "youtube-auto-captions"
---

# Keccacheck: towards a SNARK friendly Keccak
**Greg Swirski** (Reilabs) --- Burton Stage

Hi everyone. Uh my name is Greg. I work at Railaps. It's a zero knowledge and formal verification uh research and development company. And today I'm going to uh talk about how we made proving ketchup fast in zero knowledge circuits. Um for context, ketchup is the hash function used by Ethereum. Uh it's quick

to compute but it's famously difficult to prove in zero knowled circuits. And snark is a type of proof system that generates succinct proofs that are cheap to verify on Ethereum. Therefore, they're widely deployed on Ethereum. Uh we call the protocol Kachek uh from Ketchac and Sek. Uh and let me start

with some numbers. Uh this is a comparison against proving ketchup in garch. And the charts are in in log scale that log scale that doesn't really matter. But the key insight here is that um we start winning only if you have at least a dozen catches to prove. Uh so we sort of strike start breaking even at

about 16 to 32 uh catch instances or catch permutations. Uh but at 256 instances we're already 10 times faster than NARC and we just you know continue scaling much much better. Um and on average if you have thousands of catch to prove we're about 1,800 R1cs constraints uh at the current version of

Kachek uh and it actually gets better uh in a future release. So uh the first question is is this even practical like do do we need a proof system where you're proving dozens if not hundreds or thousands of of catch instances and I think the answer is yes. uh if you're doing storage proofs, if

you need to prove anything about Ethereum state, uh then every single fact is going to involve, you know, 20 or 30 uh catch hashes uh to verify Merkel proofs. Um and then if you have more than one fact that you want to prove, then obviously you're going to have more and more. Uh second obvious uh

use case is ZKVMs. they have to calculate a lot of uh catch inside to calculate addresses for mappings and addresses for accounts and all of that. Uh so they also typically deal with hundreds if not thousands of ketchup hashes and then also ZKVMs not necessarily EVM based um are going to

can benefit from this solution. So the way ZKVMs typically work is that you have your program. It can be Ras, it can be some u domain specific uh programming language and then you run run a protocol like a stark uh that's very fast to to your computation. Uh but STS tend to to generate fairly large proofs um in the

order of dozens of kilobytes uh which are still too big to be able to verify in Ethereum. it would take, you know, hundreds of dollars to be able to to if it's even possible to send that to Ethereum. So, Stark proof is not really usable on EVM chains. Uh, you typically need to wrap them into another proof

system, a snark, uh, that's going to produce something that's more Ethereum friendly. Uh, and what the Stark prover is going to do is essentially verify the Stark proof and provide a level of recursion and generate a proof that's fairly tiny and easy to verify on Ethereum. And this snark is something

that needs to do u thousands of of hash computations to be able to verify uh the Stark proof. Uh so because of this uh the way ZK ZKVMs are typically structured you have uh a stark proof and then you have a snark proof and you have to deal with some hashing u on on Merkel tree and

typically projects do something like procidon proidon 2 which is cheap to compute in snark but it's about 10 times slower than ketchup so you end up with additional overhead for stark and what we're trying to do with ketch is if you have enough of those hashes on average it might not be um that expensive to

switch from Poseidon back to uh ketchup but by doing so uh your snark is slightly slower but your stark is ketchup itself is 10 times faster than Poseidon you spend about 40% of the time in mercalization so your stark ends up being four or five times faster by uh switching to a faster hash function uh

so how does the protocol work only have 10 minutes so I'm going to give you a core idea. Um, but the idea is that we use something like GKR where you represent your input data as a multilinear polomial. Your output your hash digest is also a multilinear polomial and then um you layer polomials

that represent uh hash operations. So they that they can be something like XR operation uh beat rotation stuff like that. Um but the problem with GKR is that uh this graph is very dense. So uh typically the way it's phrased is that it's almost looks like a general purpose programming language where you have a

predicate function that's going to tell you which inputs go to which outputs. Um and then each of these little dots is like a gate which may be addition, multiplication or some other binary operation. This GKR protocol is great because this is what allows you to to scale with as you add more instances the

number of variables in these polomials grows logarithmically. Uh so this is what gives us the benefit for scaling. However, the GKR protocol is in the usual formulation is fairly slow. Um and so because we have to do all of that wrapping it and ends up being not worth it because the GKR prover itself is very

slow. So what we did instead for ketch is instead of doing the regular GKR where you go layer by layer you have to propagate all the data you have this constraints on how you structure your computation. Uh we forgotten about all of that and we decided to sort of handwrite polomials for every single

operation that happens in ketchup um to make it super optimized for that one spec specific uh computation. uh we get got rid of the usual constraint of going layer by layer so we can have like a side polomials that that represent some um arbitrary data that we need in the algorithm.

Uh again this is not enough time to go into full details of the protocol but we have a fairly approachable blog post that gives you um a better overview of what's going on inside. Uh inside that blog post you're also going to find uh a link to a white paper uh where we give you all of the polomials involved. There

are like seven different operations in ketchup that are repeated 25 times. Uh so even though the the algorithm has like 200 layers, it's just seven polomials that you need to understand and they're fairly easy to understand. There's nothing nothing magical about them. Uh and then in the blog post

you're also going to find uh a link to GitHub repository where you find the existing implementation. Uh and then we already started working on a version that's even faster uh for larger batch sizes. So I don't know if it you can see but like this is narceta check and this is sort of the new

version. Uh the reason why we're able to get win at bigger batch sizes is because we use weird commitment scheme. Um that gives us high fixed cost but then we can commit faster to really really large instances of the problem. So like the end result is like a curve like this. Um and then we're also looking into Blake

three hashing. Blake itself is faster than ketchup. Uh it's a little more involved. So the polinomials to be written are are much more difficult but it's something that that might be interesting. Um, and then after I submitted my slides, I saw there was a tweet from Justin Taler, who's like a

godfather of GKR, and he was listing all of the ideas to make SAM check, which is the underlying protocol, uh, faster, and I think he mentioned it's like 10 times faster in Jolt after they implemented some check improvements. So, this is another thing, uh, that we might want to, uh, look into.

Thank you. Uh, this is the same blog post, by the way. Um, if you haven't had a chance to scan it before, I don't know if I have time for questions. So, questions. I have time for questions. >> Sorry, you've mentioned that you're using some weird commitment scheme. Can you tell us a little bit more about

that? >> Weird commitments. uh I I cannot I was not involved in the sort of like the second stage of the project but essentially I don't know much about the commitment scheme itself but uh one of the ideas was that uh in the original version we

have to commit to like every beat is its own field element and then with the new version we can commit to sort of like wider words that are like 64 bits uh we itself I'm not entirely sure how it works so uh but I'm happy to get back to you uh within from my colleagues. >> Um it it sounds like you're um what you

have is a a custom arithmetization uh maybe of of Ketchac. I wonder how you envision that integrating into general purpose uh ZKVMs um maybe as a pre-ompile or like some custom. Yeah. >> Yeah. So the way ZKVMs would typically work is that they have pre-ompiles for hash functions for elliptic curve

operations and follow all of that. Uh and they have some sort of like an accelerator uh on the side that does its own proof um for those pre-ompiles. Uh so the way you can integrate catchek is uh you take the GKR part which is the sort of accelerator and then instead of wrapping it into a snark like we did uh

for Ethereum uh verification what you what what you can do is you can like do whatever recursion you're doing in your own uh ZKVM to verify the GKR proof uh that we're producing. Uh a quick followup I guess is um do you have any insights on these custom handwritten polomials like what um what

are you improving on? Um and yeah what's what's this what's the special secret sauce there? >> Yeah there's uh lots of cool little tricks. Uh one is uh in in GKR uh you typically sort of like a have a flat array of your state. Um and that ends up being very wasteful

for ketchup because the state array is 25 words and then sometimes you need to uh carry on 10 auxiliary elements which is ends up being 35. Um but the way GKR is structured you'll have to have 64 sort of words. uh so you know most half of the space is wasted and you pay for that computation. So what we do instead

is we have uh sort of like 25 separate polinomials and then we do random linear combination and that that trick saves us you know half of computation time. Another trick we use is for sor gates. Uh if you represent bits as ones and zeros, uh they're not comm commutative. But if you replace ones and zeros with

minus one and one, you can do regular multiplication and you can like do like you can rearrange your your uh computations to extract some multiplications like before parenthesis. Um, another thing is that like we get to skip like because we do random linear

combination, we don't have to like go level by level, but we can have some things on the side and uh sort it into uh our layers when needed. Um, yeah, I'm sure there were like the blog post list all of the sort of fancy tricks we've used. Uh there's just a lot

of little wins uh that we were able to score for something that I think was I want to say 100 times faster than like a generic uh GKR. Cool. Thank you.
