---
title: "Pico Prism 2.0: Real-Time zk Proving at Scale"
speaker: "Alan Li"
organization: "Brevis"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=z-W4mcYZg1Y"
transcription: "youtube-auto-captions"
---

# Pico Prism 2.0: Real-Time zk Proving at Scale
**Alan Li** (Brevis) --- Burton Stage

This is the >> Okay, >> cool. Um uh thank you very much for staying through. Uh this is Alan from Previs. I'm going to talk about our recent updates on our uh ZK engine called PLE. Uh specifically, we are going to be

releasing the second version of Pico Prism. Uh it's going to be proving the real-time ZK at scale. Uh we all know that blockchains are world computers but it cannot run faster than a single server and it is extremely expensive and the reason behind it is that we have this consensus issues. So

consensus today is built on simple recomputing. So what I mean by that is that for example here is the computation I want to prove uh prove the validity of this computation and here's the Alice above representing like two nodes or even more. Um now Alice want to do the computation and then show uh show every

node that this computation is correct. So she spend some computation power and get a results and then now say okay this is the computation I have done that here's the result and everyone should believe in it. But how come that Bob believes in it? How do I how do they know that if it is real? They do this

they do this kind of the so-called verification by recomputing. So essentially he spends the same amount of computing power and then do the same thing right and then after that he is kind of convinced that okay this is the correct he has verified this is the correct computation. So essentially here

the consensus is achieved by the verification and the verification is achieved by recomputing. So imagine that only if you have like only one node doing the swap then it is fine because you're just doing this computation one time but there are millions of nodes online uh so that you're going to be

doing this exactly the same computation time after time up to like a million times if if not more. So this is very wasteful and then what we propose uh for solving this kind of problem is the so-called verifiable computing which is closely related to zero knowledge proofs. So instead of Alice be uh doing

the computation of the original computation uh she will actually do the proofs besides the execution of the original program which is now is the simple multiplication. So here the proof is actually saying that okay I'm proving this program which is the multiplication and here's the input 142 and 121 and

here is the result. He is packing all of these things into a zero knowledge proof and then he can she can do the computation offline offchain whatever whatever computing power she is using. Of course this will cost more than simply computing the original one. So we have like more computing used but the

thing is like once she sends this to the Bob [snorts] and the Bob do the verification he is somehow convinced that this is the correct execution of the original uh original program. So this is called verifiable computing. Uh the good thing about it is that Baba is only spending a very tiny amount of uh

computing computational power here to do the verification. So essentially what happens here is that originally the computation is C is just equals the verification but now we are decoupling the verification from the computation. So essentially we can do computing computing somewhere and then do the do

the verification somewhere else. And the good thing about it is that we just do the computing for one time and then verify it a million times. The thing is that the cost of the verification is just so slow so so so small. There are many other benefits that we could bring. Uh for example, uh the privacy and this

one is also uh good is that uh originally we only have this multiplication as a simple program. But uh the pro the program or the order computing could be very complicated like inference of a large language model. So this as you can imagine involves multiple GPU machines to do like several

seconds or like minutes of do doing the inference. So doing doing this recomputation is almost impossible. But now with this uh uh but but now with this uh verifiable computing we can just prove that this LLM with this specific input is having this output and then what good is about is about about the

proof is that verifying the proof no matter the what the original computation power computation workload is it is they cost exactly the same computation. So it's still very tiny right it's it's like a constant thing there. So that is to say that whatever computation thing we have computation workloads we have we

are paying the same uh amount of computation for verification on chain. So this allows us to scale the the the the computation on chain almost infinitely. There's also something else like privacy benefits for example this is still that something that we want to prove but then

um Alice is saying that okay we are hiding hiding some part of the of the inputs say that we don't have this 142 uh we have only 121 and the proof is actually showing that there is some input [clears throat] that I multiply it with the 121 and here's the results so now things becomes

totally different from the original scenario where we do the recmp computation because now we don't have the input there's no way to do the recomputation to do the verification but now uh with the zero knowledge proofs we are able to do that what does it bring it brings us the privacy benefits we

don't have to uh show everything to the to the other nodes we can hide something as a privacy thing so that even even if we hide something they can still verify that this is true okay so so many benefits uh bring us to the conclusion for a prediction such that by the year of say 2035 or even 2030 to be more

aggressive 99% of the computation for blockchain applications is going to happen offchain and verified by ZK proof however there's a drawback because ZK is very complicated uh so I'm not sure like how many of you have uh handwritten some circuit ZK circuits before anyone yeah it is very complicated and here is just

a very simple snapshot of uh of our engineers writing Halo 2 to prove a Fibonacci uh Fibonacci computation like two pages hundreds of lines of code very complicated you have to understand Halo 2 you have to understand Zika knowledge uh zero knowledge proofs and you have to write this code out and it's also very

hard to audit right I guess like many of you have already gone through this process before um basically two solutions towards this kind of thing first one is the ZK co-processor what is ZK processor It is essentially a set of handwritten uh circuits specifically for a specific set

of applications. For example, there's a zero knowledge zero notch machine learning which is specified for machine learning applications. There's also data availability availability applications. So DA thing uh so we can write a specific set of circuits for that. It is blazingly fast but is limited

generalization because every time you have a new application you have to write a new set of set of circuits and it's very hard to audit every single time. It is tedious to develop. Another solution is called the ZKVM. Um as you can tell from the from the from the name it is a virtual machine. What we are essentially

doing is to write a plain code whatever code like Python, Rust, Go or anything else. we compile it to say risk of five a specific set of like instruction set and by op code by op code we translate it or compile it into a zk circuit. So it brings us a high flexibility because basically anything that you write you

can directly compile it into a zk circuit and then do the proof and it is very easy to develop but it there has the performance overhead here. So yeah there's many challenges here I just to mention a few uh basically every u like currently many of the zikkm existing or zik co processors a one size

fs all solution will be inher inherently limited all right so that's why we proposed a pico uh starting from last year um I think the last year at the same time uh like this year uh exactly one year ago we proposed the first version of pico on CPU it is very flexible and future proof

Uh it has has the modular architecture with interchangeable pruning backends and custom customizable pruning workflows. Um it is it is very performant. Uh it brings the modularity to a new level where we have the so-called both function level and application level co-processors or

pre-ompiles. for functional uh functional level co-processor like pre-ompiles we have all kinds of cryptographic primitives or computations written in specific chips or pre-ompile chips um for application level zk co-processors pico is able to connect with any other uh handwritten zkircase

like zkl or zk uh data availability uh we have shown that it is possible where the pico is working as the glue and co-processor is working as a specific speific circuits that is very efficient for specific applications. It is very developer friendly. Of course, you're just writing applications

with the language that you are most familiar with. Yep. So, Pico requires you zero ZK development experience, right? So, now you just this is the same thing that you could be could be could be proved by Pico to generate a ZK proof and now you only write like less than 20 lines of

code in plain Rust. So it brings a huge benefit for us that to develop um maybe not us but also our AI agents. So Pico democratizes Zikin technologies. So it is encapsulating all the complicated computations behind the scene so that you can just call it by some simple SDKs and then you get a ZK

proof out of it. Here is a showcase of our uh our new application that is built on upon pico called brevis. Uh the motivation of that is that um nowadays you can see that many images videos are generated by AI. We cannot basically tell or even AI cannot basically tell which one is AI generated or not. Right?

So um but it is possible that we using we use the zk proofs to prove that which of the images or videos are actually directly from the from the raw devices or have gone through uh some legal edits. Uh here is the some video that I can show you. >> In the age of AI seeing is no longer

believing. A photo used to mean proof. Now it means doubt. Using AI to detect AI is an arms race you never win. Don't ask if it looks real. Ask if it can prove where it came from. Introducing Brevis Vera reality attested. RVIS Vera starts with a signed

hardwarebacked capture. It then proves the edit path itself with zero knowledge proofs. Now you or anyone can verify that what you are seeing is real. Rivvice Vera, we show you the proof. All right, this is the marketing material. But what basically [laughter]

happens behind the scene is that uh modern cameras and many smartphones have this so-called signature uh related to the thing that they generated uh at the moment of the capture. So you take a take a photo of your small smartphone and some of the smartphone like Pixel is having this standard called the C2PA. it

has a signature that is actually proving that this image is directly from the device. Right? So this is a thing but second thing is that there some many many of the times we want to do some addits like just the cropping doing rotations changing the brightness all these kind of things. Um yeah, some of

them may change the content of the of the of the image, but we can still prove that we have just written out a Rust package out of it. Uh stating that all the things all the edits uh done by Rust applied to certain kind of image that is generated by these smartphones or modern cameras are valid. Right? So basically

we have the zk proof that okay this image this input image has gone through a certain number of addis legal addis and this is the output image. This is one thing that we could prove. Second thing is that this input image is something directly from the device. By combining these two proofs together to

get one proof, we can after we verify it, we can know that okay this is a this is a image and this image is not generated from air by AI but it's generated from some devices although it come gone through some some kind of addis but it's still something real instead of just something from the same

air. Okay. What is fascinating about it uh from us is that um as I have mentioned that you you basically have have no idea you don't have to have any idea like what happens behind the scene but you just use it by calling some SDK the other thing is that it's very AI friendly uh

we have made it try to we try to make it so AI native so that AI just reads the whole thing and then trust try to wire wire everything into the vehicle so that with just one week of work we just we just develop deliver the PC of priv right so building ZK apps has never been such easy

okay so this is uh uh the application that we have built recently and we have trying to make it a serious production right now um there's also another series of series of application where we'll try to prove uh prove that Ethereum mainet blocks uh execution uh in real time uh I think it's about five to six months ago

we will release the picop prism 1.0 uh to prove the ethereum blocks with accessible and consumer grade hardware. All the things I have just mentioned is done on uh some oh I think this is whatever this is something that is outdated but anyway so yeah so uh we

have uh yeah anyway so um uh originally we are doing this kind of proving on the CPU but turns out that there are many uh computations that is very heavy and could be shifted to GPU that's exactly what we did for the prism uh picle prism 1.0 zero. Uh we basically uh use 64 GPUs distributed on eight machines and each

of machine is handing a part of the proof of the original sub block original blocks for at the time at each of the block has the gas limit of 45 million gas and then we divide them into seven sublocks and for and distribute them into onto each machine. Each machine is handling one sublock and there are seven

sublocks here. after after computation we have seven proofs and then there's a machine there called aggregator that tries to combine all these seven subroofs here uh into one. So it is essentially divide and conquer uh thing using subblocks and each blocks is divided into seven parallel thing and

can be uh can be proved in parallel right and here's the results uh we are happy to announce at the time that we are able we are actually one of the first to do this kind of proving uh to prove that 99.6% 6% of the Ethereum blocks uh is able to be proved under 12 seconds with 64 GPUs, right? And the 12

seconds is just the Ethereum Ethereum mainet block generation time. And on average is actually even better is like less than seven seconds. So on average within second 7 seconds we are able to prove the Ethereum blocks. This is not not enough of course because 64 GPUs although it compares although it's it's

nothing compared to current AI applications which uses like tens of thousands of GPUs but is still something that individual or individuals cannot afford. It is not good for the decentralization. So following the Ethereum uh Ethereum foundation's uh uh criteria for doing this real-time

proving uh we have just reduced the computation power required to do the real-time proving uh from 64 GPUs to 16 GPUs which is just the 16 25% of the original computation power that we want to use and then the the [clears throat] whole architecture has been rewritten instead of doing this sublock thing uh

divide and conquer thing uh what we did is that we have two machines each of them having a GPUs and then we have a global. So the global is essentially working as a task board uh which is indicating that which chunk or which task has not been done and these tasks could be fetched by each of the machine

and we have to we try to maximize the data locality such that if machine A has the corresponding proof then doing the recursion uh it is better happening on machine A as well and the same so as machine B. There's also some other optimization like ahead of time comput compiling compilation where because

originally the emulation is kind of interpreter based so it's very slow but now we are just compiling it into native rust and then do the do the execution on top of that so it's just becomes becomes super fast so with that we are maximizing the parallelism um there are also some other things I think I'm kind

of running out of time but I just want to mention some of the few um the CUDA code optimization because it turns out that we are able to uh greatly uh greatly increase the efficiency of the CUDA code uh by doing many kind of very small um uh optimizations. For example, here uh doing the fry open thing uh we

have this mongari batch inverse which requires you to have like multiple um reciprocal computation for uh individual values. But what we did here is that we do them first by uh multiplying every every single denominator to get a huge multiplication and then after that we use this product to recover the each of

the reciprocals. So in that way we are only just doing one reciprocal with multiple modifications but the thing is that doing a multiplication is just so much cheaper compared to the reciprocals. There's also a shift from the instruction set that we are supporting from 32 bits to 64 bits. It

means more chips to us. Uh something more related, but this means fewer cycles. So, it's basically a trade-off between the efficiency and the effectiveness. Um yeah, so it's a trade-off on efficiencies. Um but we found a small sweet spot such that we can achieve the best efficiency on top

of them. uh we are also doing formal verification with nether mines. So this is on the way. So this is the result. Um it's not only about like using 1/4 of the of the computation power to do the proving but it's also like compared to what we originally have which is gas limit of 45 million. Now we have 60

million right maybe next year we'll have like a 120. Um but the thing is that the the workload is also kind of increasing. So using the original 64 GPUs we will have the average running time pruning time for uh Ethereum blocks uh nowadays for more than 8 seconds but now we just only having the uh 6.6 seconds and what

is more is that we are proving more than 99% of blocks under 12 seconds as well. So in total it would be more than 10x of acceleration compared to what we have uh uh using 64 GPUs. All right, finally uh Pico uh Prism 2.0 will be able to prove arbitrarily large workloads because as you can imagine

this uh thisuler global scheduleuler and the worker architecture is could be could be embarrassingly parallelized. So any kind of workloads could be distributed upon that. Um Pico Prism 2.0 is soon to be open source maybe next month or some sometime later u but is pretty soon. Uh Pico itself is fully

audited and ready to be used in production. So finally uh welcome to use Pico and build with us. Thank you. [applause] >> Uh yeah, thank you. Um nice talk. Um could you just clarify what a subblock is? Is that a is that a chunk of risk 5 instructions or what is that exactly?

>> Oh yeah. uh the original Ethereum block is a whole block with tens of different transactions, right? And then the sub block what I mean here is that we are we are dividing these transaction into uh some some smaller blocks and the sending this for example originally we have like a hundred transactions. uh we have maybe

we can just pack 20 of them as one sublock which is is essentially a part of the original whole block and then send them to the one machine and the rest of 10 uh to the other machine or something like that. We are capping them capping the gas limit to be one over seven of the whole total gas gas limit

and then yeah do the parallelization there. >> So do you you actually do that before um before it goes into the risk 5. So you're actually splitting the transactions at the kind of like Ethereum block level before you even go into.

>> Yes. Yes. Yeah. Exactly. We are actually doing that uh to to prepare the corresponding input. So basically we have eight inputs. Seven for different sublocks and one for aggregation. But originally directly proving the whole block we just require one input. >> Thank you.

>> Yep. >> Thank you very much. Hey, hey, hey.
