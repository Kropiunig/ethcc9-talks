---
title: "CryptoCPU"
speaker: "Slobodan Lukovic"
organization: "Ponos Technology"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=mYVG0_VACWg"
transcription: "youtube-auto-captions"
---

# CryptoCPU
**Slobodan Lukovic** (Ponos Technology) --- Burton Stage

Wrong lights, actually. Okay, thanks. So, good morning. Thank you for coming. Last day, first session, not so easy, right? And special thanks for to Wolfgang for amazing introduction actually to my presentation. We're speaking about quantum computing and quantum threat.

And actually I'm going to speak about other way around how where somebody sees actually a problem, other guy sees opportunity. And that's actually a chance for us to uh introduce some protection methods. And actually

we're not introducing protection methods, we're introducing solution how those protection methods that Wolfgang mentioned being very expensive can be actually cheap, fast, and affordable. That's where exactly where Crypto CPU is coming into play plays. It's our

custom dedicated hardware solution, cheap actually, that Bonus Technologies is developing as a solution for acceleration of various cryptographic primitives that are actually core of post-quantum cryptography. So, yeah, we've all seen that

we're all following the Ethereum develop evolution and roadmap. And it's actually mostly there are many assumptions that it will be strongly based on different kind of zero-knowledge computations and

consensus level layer. Also, on the other side, it might be possible to move from EVM towards RISC-V, that's another possible trend. And definitely entire stack has to be post-quantum resistance resistant. That brings us to the fact that this all this kind of computations will

be quite costly and also increase latency as uh there's post-quantum cryptography requires actually much, much more two orders of magnitude actually more computation resources than regular cryptography.

What Crypto CPU actually brings in this landscape? So, first of all, it's a RISC-V based platform that is extended in two directions. One direction is extension of different We'll see it later on in greater details, but we actually stand instructions

instruction set to to support different kind of specific arithmetic field operations. And on the other side, on the other dimension, it stands it extends in a number of coprocessors that are performing parallelization and pipelining of critical functionalities like hashing

entities and so on. Essentially, it is focused on enabling fast and and affordable post-quantum computation uh focused on zero-knowledge proving. We'll see how it uh is done later on. And but also can be used also for instance for Solana

validation outside Ethereum. And also it's compatible with modern fully homomorphic encryption methods. What's the essential idea of this one is that usually ASICs are considered as some devices that are sitting somewhere in a corner and very difficult to be

used because they're difficult to be programmed, requires some kind of firmware, and so on. That's why actually we rely on um It's not working. Okay. That's why we rely on RISC-V architecture because it's very flexible and it's uh

Yeah, I can go here. That's why we rely on RISC-V architecture because in that case you don't need a dedicated compiler. You can use a extend and optimize extend existing compiler, regular compiler, so that programming interface towards developers

remains the same, meaning that they can program in high any high high-level language without caring about any kind of details underlying implementation in hardware. That's one level of compatibility. Another level of compatibility lays actually exactly here

because we consider this chip will be packed in a board that will be through PCI each interface connected with interact with the rest of the world, which practic in practical terms means that server or or

data servers operators can just plug in this card directly into their racks without any kind need of further integration, which means that practically an entire stack it's fully compatible what what is out there. And that's huge advantage of this

architecture of this solution because of it's based on RISC-V architecture. Practically, it's going to be a multi-core CPU setup. And having few standard RISC-V cores, few cores that we will see later will be in charge of native execution of native witness generation, that is the first

part of zero-knowledge proofs. And then, on the other side, through a number of extended vectorized instructions, meaning prime field operations plus this set of special function units or coprocessors, if you wish, it will be able to support both end-to-end execution of zero-knowledge

in a very, very accelerated way. Uh I would just like to give you A lot of people is asking us about why not GPUs and what's the difference how it differs from GPUs. So, just give you a few um

insights on that. Um For instance, when it comes to zero-knowledge proof protocol is composed of two parts, so-called front end or if you wish witness generation, that is usually based on RISC-V instruction set architecture instructions. And it practically GPU

must completely emulate execution of witness generation. On the other side, we can make a dedicated RISC-V core that will natively execute this part of zero-knowledge protocol. That's one of huge advantages compared to GPU when it comes to first or front end part of a ZK prover. On the other side,

GPUs are natively focused on matrix multiplications through tensor cores, and they are actually they leave only, I think, even less than 5% of of their resources for integer multiplications. On the other side, Crypto CPU entire instruction set and complete computation

architecture is actually we with special vector instructions and coprocessors is actually built to execute these special complex operations that we find in cryptography. And finally, very which is very, very important is that GPU are usually composed of thousands of

parallel units with limited memory assigned. And then, of course, you have a part of this limited memory that is assigned, you have problems of interconnections usually because you have to move huge amount data around. Uh and then usually they use network on chip and stuff like that.

For for shared high-throughput memory. On the other side, uh we actually through Crypto CPU are not achieving these huge optimizations and latency cut by means of parallelizations, but by means of specialized computation methods.

So, what are actual benefits of this? It means that we we we we provide end-to-end acceleration with no migration cost. It it's crucially important in this case. Um then, for instance, results that we have obtained so far, I have to say that so far we have

implemented most of this entire flow in FPGAs. And we achieve, for instance, we we can we managed to cut latency of Solana validation by 50% and cost of almost 80% because this kind of specialized hardware solutions, even in FPGAs,

consume less than GPUs is exactly because of their inefficiency when it comes to utilization of resources, available resources. Uh yeah, on the other side, in the next generation, when we hopefully tape out the chip itself, the OPEX would be something like 100 times

lower and CAPEX we expect to be 10 times lower compared to GPUs. Practically, finally, it enables easy programming and very, very flexible deployment is as that I mentioned, it can be plugged in in any kind of server, can be also used standalone device, and so on.

What does it mean in wider zero-knowledge proof uh uh context? Basically, essentially, it cuts uh latency, it cuts uh costs, and improves improves throughput. Enabling, on the other side, huge number

of real-time use cases because the idea, I mean, now we are real-time is a little bit tricky, what's real-time? In Ethereum, real-time is practically 10 or 12 seconds, what what is block finality. But many applications require it to be much lower than that, right? So, there are That's why

among the other things L2s exist. Um yeah, it it boosts decentralization, which is very, very important because all, for instance, all these kind of validators in this this case could be completely decentralized, everybody could afford $200 to buy this kind of device and and

become practically full fully Ethereum node because, as I mentioned, we have RISC-V processor inside. And if eventually EVMs moves to RISC-V, we will be able to support not only consensus, but also execution layer of Ethereum with this single device. Yeah, finally, of course, it improves

censorship resistance and crucially, I mean, it was not it's it was here, but [snorts] I think this importance of the fact that it's PQ enable is actually growing. Why PQ and what does it mean PQ in our case is actually that we are collaborating with Zcash

and Zcash is supposed to be post-quantum resistance with if I remember well 128 bits of security. So, let me just check how much time I have. Yeah, so this is there is essentially an initiative by Justin Drake himself to make a server

for FPGA-based server for home proving project, a small kind of initiative between Ethereum Foundation, Zcash and and Bonus. And yeah, we are open for somebody else to join, of course. So, the idea is that this is current situation that we have. So, we in order to make

real-time proving or 10 seconds below 10 seconds proving Ethereum block, we practically need at least 16 GPUs, which means a kind of huge results in huge energy consumption and it's of course huge would be huge burden in terms of either capex or opex for for any kind of provers that would

like to run it. Our idea is to achieve below 10 seconds proof target to to have something like four to five times cost energy consumption reduction by this FPGA server compared to GPU server. And

actually the idea is to to finalize this project by the end of the year. The idea is actually to to replace entire this GPU farm with four to eight FPGAs. And for us this is a very nice demonstrator on the path towards ASIC. If we manage to prove that FPGA is able

to provide exactly the same level of computation and speed as GPU farms with five time with few times less, let's say expense on energy consumption, it means that for instance, if once put in ASIC, everything will go at least 10 times below because just frequency in which ASICs are operating

are usually 10 times higher than those of um FPGAs. Yeah, so this is a small recap. Basically, what we currently have, we have implementation in U55C board, but there is a next generation of

V80, which has double resources, but much more importantly, it has next generation of PCI interface, which in practical terms means that this kind of bottleneck is removed. Uh so, currently, we are faster than RTX 3090, which is commonly used in in in proving servers at the moment and

yeah, so and we have entire Zcash backend on FPGA already implemented. So, practically, we need to finalize this complete end-to-end uh uh proving protocol. The most likely, to be very honest, this will be based on some combination of

currently the witness generation should be done on a CPU host, while everything else will be done in in FPGAs. So, that would be a kind of common configuration of the server. And yeah, finally, the idea is to suppress RTX 5090 on

different kind of ZKP workloads and yeah, to have single card 10 sub-10 seconds Ethereum block proving. Oh, okay. Just a second. Oh, there is there was some gap. I think one slide is not shown, but anyway, we anyway, we don't have much time. So, yeah, the idea with this home proving

server project is to showcase, to demonstrate um possibilities of custom hardware approach in first phase with on GPUs on sorry, on FPGAs and then later on by tape out in ASIC. So, this is supposed to be really

ultimate solution for scaling ZKPs and in practical terms, it can be analogically compared with Bitcoin miners in in in we may call it ZKP miner and for whom it can be useful, practically for all infra providers, meaning large servers like uh

I don't know, Galaxy for instance, can be used for different kind of on-prem deployments for enterprise use or whatever. And finally, it will be it will enable standalone home users to Ethereum proving directly in in their homes for very affordable price

because uh given the given this I may tell you that currently uh to prove Ethereum uh block in real time, the consumption of GPU servers is around 10 kilowatts. With FPGAs, we hope to bring it down to two to three kilowatts and in this case would be 200 to 300 watts, which is a

kind of bulb consumption. So, that's that's the road map that we hope to achieve with this chip. Uh thank you and I would be happy to take any questions. >> [applause] [cheering] >> Uh thanks. Uh nice talk. Um

I'm just wondering about what kinds of different kinds of ZK systems you actually would support. So, like hash-based versus elliptic curve or different kinds of primes. Are there restrictions there or Well, there are always restrictions, yes.

>> [laughter] >> It's but we are focused on hash-based commit commitment schemes like Fry for instance. I may tell you some numbers. Our Poseidon implementation, as far I remember well, in Goldilocks field

makes 83 million hashes hashes per second. Uh so, we are mostly based on Fry commitment schemes. We have implemented completely Plonky2 solutions. That is a core of Zcash current existing Zcash and also Plonky3 solutions. Uh when it comes to arithmetic fields,

we are widely compatible with those mostly used. Marson, Goldilocks, Baby Bear are fully supported for different kind of for different set of instructions. That's one thing. Another thing, yeah, in general, all Fry-based or if you wish Stark-based provers are supported. And

all those that are having actually risk five ISA generation is a base for witness generation. There are currently, I think, only only one major ZK prover that is a kind of popular is excluded from this. Most of other are actually covered. Um as

just on essentially, uh the the the point is that as long as those arithmetic operations are uh base for different kind of computation or whatever cryptographic primitive that is supposed to be computed, we are supporting that.

That's why for instance, we can support also signature verification or which is a kind of hashing. I think it's SHA-256 that are basis for Solana validation. So, it's actually a portion of the chip, not full chip, but portion of chip that might be used there still being more much more efficient for this kind of

purpose than anything else. That's the idea. Okay, thank you very much and yeah.
