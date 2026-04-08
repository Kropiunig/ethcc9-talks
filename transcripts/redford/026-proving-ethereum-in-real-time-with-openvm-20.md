---
title: "Proving Ethereum in Real-Time With OpenVM 2.0"
speaker: "Yi Sun"
organization: "Axiom"
stage: "Redford"
youtube: "https://www.youtube.com/watch?v=hhv-csgdsyQ"
transcription: "youtube-auto-captions"
---

# Proving Ethereum in Real-Time With OpenVM 2.0
**Yi Sun** (Axiom) --- Redford Stage

Should I start? >> All right. Hello everyone. I'm here today to tell you about uh OpenVM and its role in proving Ethereum for scaling the L1. So first to set some context um Ethereum has embarked on this road map to scale L1 execution with zero proofs. So to

tell you what that means, the bottleneck in Ethereum execution today is that validators have to re-execute every transaction. And so what that means in particular is that they have to access the database for every storage read or write that a transaction makes. And this all has to happen within the slot time.

And so what that means is that to increase the gas limit, we'd have to require validators to have ever more powerful machines, which risks uh centralizing validation and therefore um the you know trust properties of Ethereum itself. So instead of doing that, Ethereum is embarking on a path to

instead prove execution with a zero launch proof and have validators verify those proofs. um that is something that takes constant time irrespective of the size of the block and therefore can drop the load on validators while allowing the network to scale the gas limit. So this is going to take place over a

series of steps which are laid out on the straw map and to talk through the pathway uh the goal is to have validators progressively uh move into this new way of block validation. Um so the hope is in Hagota validators will verify optional proofs of execution in conjunction with the re-execution that

happens today and then in future forks the re-execution can be completely removed and the gas limit can be increased with validators handling the same load with just verifying zero knowledge proofs of execution. Once that's done, the hope is that the same infrastructure can also be used to

scale rollups by verifying their execution in a native roll-up framework. Now, for all of this to work, we actually have to prove the blocks extremely fast. Um, now there's a buzzword of real-time proving, but what this means is that validators have to receive a zero knowledge proof of block

execution within the slot time. Um so instead of each validator receiving the raw transactions in a block and re-executing them often in less than a second um in the slot time the blocks will be sent from a block builder to a prover. The prover will gossip the resulting proof to all the validators

and then validators will verify that proof essentially instantly. Now to do this we have to be able to prove execution of an Ethereum block in zero knowledge. Now obviously Ethereum execution is quite complex and so the most ergonomic way to actually do this is to use what's called a zero zero

knowledge virtual machine. So this is something that allows developers to generate proofs of ordinary computer programs. And the proof program we're interested in here is the state transition function of Ethereum itself. You might imagine this is very complex and so as a result we need to build

quite a bit of machinery to be able to produce a ZK proof for. Now today I want to talk to you about OpenVM which is the ZKVM that allows us to actually do this. So we built OpenVM as a modular and performant approach to ZKVMs uh prioritizing customization and extensibility. So tell you a little bit

about it. Um, it's built on a novel no CPU architecture for the actual ZK circuits. What that means is that unlike most CK systems that are a bit skumorphic to physical processors, uh, we were able to take out the CPU component of the VM and this allows different operations of the VM to be

plugged in by developers as they need. Um, in particular, it allows OpenVM to have modularity at the ISA level, uh, supporting different types of operations in the ISA. And finally, it has a Rust developer front end, which means that as a developer, you can take any arbitrary Rust program and generate a proof of its

correct execution using OpenVM. So to not bury the lead, we are now able to prove Ethereum in real time with OpenVM 2.0. So on a recent benchmark of 7200 blocks, which is a full day of blocks, we're able to prove Ethereum with a P99 proving time of 8.5 seconds, an average time of 5 seconds, and in the

sample, the highest time was 10.7 seconds um on 16590 GPUs. So you can see the full histogram of proving times on the left. And notably, you know, 10.7 seconds is less than the Ethereum slot time of 12 seconds. Uh so we're definitely getting there on performance while only needing 16 GPUs in the

cluster which should enable users from around the world to participate in proving. Now to give you a sense of the progression here uh a little over a year ago we proved block 21 million in something like 260 seconds and since then we've been able to lower that by over 60x to a little over 3 seconds as

you can see in the graph on the right. Um so this has progressed quite a bit on performance in the last year. Um in addition to approving Ethereum, we also evaluated our VM to prove a standard benchmark workload called Coremark which is used to evaluate embedded CPU performance for physical

processors. Uh since we're proving arbitrary computer instructions, we thought this could be an appropriate benchmark for our ZK system. So in the blue you can see our numbers from about a month ago and in the red these are our most recent benchmarks from our beta release in March. Um so on a single GPU

we're able to prove coremark at about 19 MHz and on a larger cluster of 64 GPUs we can scale up to over 900 MHz. Um so this is actually pretty close to the speed of some processors you might actually use today. uh which we think is very exciting to enable ZK proving of just ordinary computer programs that you

might use in practice. And finally, on the performance side, we were able to power OpenVM with an ahead of time executor, namely something that runs the raw computer programs that OpenVM is proving. And this is a bottleneck in the proving because we're getting to the point where proving is

get close to execution. And for OpenVM, our ahead of time executor actually runs the underlying risk five assembly at close to native speed at around 3.8 GHz. All right. To tell you a little bit about the what's underlying OpenVM 2.0, we introduced a new multilinear proof system called Swirl to power OpenVM 2.0.

So it's based on WR which is a very efficient SASbased multi-linear commitment scheme that enables extremely cheap verification and with swirl we're able to achieve 100 bit provable and postquantum security while keeping the actual zero knowledge proof size under 300 kilobytes and so the proof size here

is very important for participation in the Ethereum gossip network without increasing bandwidth requirements too much and finally because of this cheaper uh cheap verification property we're able to power OpenVM with a very fast recursion um that handles dynamic numbers of proofs. So this is important

in the actual ZK aggregation process. Um and finally uh obviously ZKVMs are quite complex systems. There's a lot of ZK circuits. We have to deal with hardware ISAs. So as a first step towards ensuring a higher degree of assurance that will be necessary for inclusion for use in the Ethereum L1 we work with

nethermind research to actually formally verify the risk 5 front end for openvm in uh the lean theorem checker. So what this means is that we were able to prove formally the mathematical theorem that the implementation of risk 5 in openvm actually matches the official specification of risk 5 from the makers

of risk 5 themselves. Um so this specification is used to typically verify hardware implementations of risk 5 but in this case we use it to verify the zk implementation. Um we were relieved to know that uh during the process of the formalization we didn't find any bugs in our implementation and

we hope to actually expand the scope of formal verification in OpenVM going forward. Okay. So I told you a little bit about the role of ZK in Ethereum's scaling road map and how openVM might play a part. So what's the implication for developers? I think there's broadly two

large takeaways. The first is that this will be a pathway for Ethereum to scale the gas limit on L1. Obviously, scaling gas lowers gas fees, reduces congestion, and critically because the scaling will essentially be tied to the performance of ZK proving, increasing the performance of ZK even further will

directly translate into the ability to scale the gas limit without compromising the security and decentralization properties that are critical to Ethereum. On the application front, um ZK can be used outside of the L1 of course and we think it's really exciting to have

performance ZK at the application level. uh to mention a few possible uh directions can be used to generate validity proofs for rollups to validate the execution of complex um off-chain operations um and finally to add certain privacy and verifiability features for more

institutional use cases. All right, so I'm from Axiom which is a company behind OpenVM. Um so we're working with applications to explore these more application focused use cases of ZK. Um so we help people design applications with the knowledge that ZK is possible, accelerate them with custom

extensions to OpenVM to make ZK even more performant and finally to actually generate the proofs on our API. Um some examples of teams we've been working with are lighter which is um adding EVM support to their verifiable exchange um scroll which is using openVM to actually verify their rollup for the past year

and a similar ZK enabled uh perpetuals exchange on top of hyperl and I okay great so that's my last slide um so you want to learn more about OpenVM, you can check out our docs, our Telegram group, or the code on GitHub. And if you're interested in working with us to

add ZK into your application, you can check out the link on the slides. And I have some time for some questions. So, does anyone have a question? Can you just say a few words on what's what are commitment schemes that you're using and how much it differs from other proving schemes like plongi3 for

instance that is quite popular around stark in general. >> Yeah, it's a great question. So we're using the were polinomial commitment scheme which is a hashbased commitment scheme that's adapted for multilinear polinomials. Uh so plonkey 3 actually recently added support for word in

addition to the previous fry commitment scheme but we're not using the pony3 implementation. So so we wrote our own implementation >> and it's open source. >> Yeah everything is open source MIT Apache 2.0 dual license. I should put that in the slide.

All right, great. So, no more question. Cool. Thanks everyone.
