---
title: "The road to post-quantum Ethereum"
speaker: "Wolfgang Vitale"
organization: "Bitcoin Suisse AG"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=bEUxvjstYZk"
transcription: "youtube-auto-captions"
---

# The road to post-quantum Ethereum
**Wolfgang Vitale** (Bitcoin Suisse AG) --- Burton Stage

Oh, does this work? Yes. All right, you're live. And uh first of all, I want to clarify this is a broad introductory overview. You will not find super advanced topics, but I want to cover everything in 20 minutes that I can on quantum computing, what it means for Ethereum, and what Ethereum is going

to do about it. So, let's go and let's start from quantum computing. The first thing and the only thing maybe I want to say is that I want to make very, very quantum computing is not like a more powerful or faster version of classical computing, it's a completely different thing. And why is it completely

different? Because it's working with a fundamentally different unit of information. We're not working with bits that can have two values well defined zero and one, we're working with qubits. So, they have two basic states, they can be in superposition on a single qubit, you can put more qubits in entanglement,

you can work with interference. Completely different properties, it's a completely different beast, completely different mathematical objects. This means that you can do completely different algorithms. So, certain algorithms for certain problems, they provide exponential speed ups, and this

is what we care about. It is not a general purpose machine, but it's something that you use for specific algorithms that are only possible with this new different mathematical objects. Now, the problem is that yes, if you can actually fabricate these things, so so you don't work with mathematical

objects, but you actually fabricate devices that behave as qubits, and I mean logical qubits and qubits that have reliable you can do reliable fine control of their properties, of their relative phase, of their amplitude. You can put them in entanglement, you can do that for an

extended amount of time. If you can do all that, then you can do these algorithms in practice. That's huge, but that's also a big if, because quantum computing is real, but the challenges are also real. By the way, what do I mean quantum computing is real? This is not science fiction, this is not it's

based on quantum physics that we know, it works very well, it describes very well reality. It's a really good model, predictive model. Also, this is not just theory, because quantum effects are actually used in devices that we see everywhere. So, this is we know how to use quantum physics and quantum

mechanics, it's not just theory. Also, from the quantum information theory point of view, nobody can tell you in a really convincing and definitive way, this will not work. So, in theory, quantum computing works. The question is, can we actually fabricate this stuff?

And this is difficult, the challenges are real. So, some people will tell you, for instance, atom is the perfect is nature's perfect qubit. I mean, it's good, but it's not perfect. We are not anywhere there. We are not working with mathematical objects, we are working with physical qubits with

non-idealities. And the proof, if you want that we don't know how to fabricate qubits for real, is that you can still see so many different completely different technologies and ways to fabricate qubits. We have trapped ions, we have superconducting circuits, or at least based on superconducting circuits.

We have neutral atoms, we have photons. Completely different. Now, what will be the best way for a specific application to fabricate qubits, we will see. But for sure, all these physical qubits still have a lot of non-idealities, they operate in noise. Noise means loss of coherence, loss of coherence means loss

of relative phase, no control, suddenly nothing works. And it's not like we didn't try. We actually tried a lot to use physical qubits. We were in the so-called era of noisy intermediate scale quantum computing. We tried for years to make it work, to find application for which we

can cope, you know, with the physical error rate. But it turns out that was a cope, and we are moving on to the fault tolerant quantum computing era, moving on from physical to logical qubits. So, what does it mean? Instead of having one device, or anyway, one item, one object representing one computational qubit,

you put together many of these physical qubits, you apply quantum error correction code depending on the connectivity between the physical qubits, and suddenly you get this other object that is a logical qubit that when treated as a whole has logical error rate that can go below the physical

error rate of the underlying physical qubit. All this to say that even if we cannot reach extremely low physical error rates, by using quantum error correction, we can bring down the logical error rate. And suddenly we can do we can apply these algorithms for an extended amount of time, and we can do

really interesting stuff. Or yeah, worrying stuff. Let's let's see. So, yes, uh the second chapter, quantum threat. Why are we even talking about it? Why are we here talking about quantum computing? There is a risk. And uh yes, you will probably you know

that the the main risk, as I said, there are some only some few things you can do with quantum computing like with actual exponential speed up. Unfortunately, one of these is breaking public key cryptography. So, ECDSA gone, RSA gone, if you can apply Shor's algorithm at the scale that is relevant to the security

properties of these signature schemes. So, public key cryptography is gone, cryptocurrency should care about it, and anyone who relies on public key cryptography should care about it, which is pretty much everybody. So, if you can do this Shor's algorithm, then you cannot rely anymore on these digital

signature schemes, meaning that the signatures can be forged. You can't trust anyone. But the question at this point is, what do you need and what kind of computer you need to run Shor's algorithm? Yes, a quantum computer, but how powerful? And that's uh something that you know, is

changing over the years, because it's not like there is only one implementation of Shor's algorithm. Shor's algorithm tells you how to do it, but then you actually have to implement it with logical qubit circuits. And over the year, people find better and better ways, smarter ways, more

efficient ways to reduce the required resources to run the Shor's algorithm at the scale that is relevant to us. That's a so-called cryptographically relevant quantum computer, CRQC or Croc, as you like to say. So, we have seen over the years the number of There are at least two metrics

that we should pay attention to. There are many more, but to simplify, and that's what also what Google did, there is this nice chart. You have two axes. On one axis, you have the number of logical qubits. So, the lower the better, of course. And the other is the number of Toffoli gates

that in a first approximation is how long this computation in time needs to be. So, this is also the shorter the better. And this is improving over the years. We see orders of magnitude reduction, and we are not done with algorithmic improvements. I did this slide before the Google paper, then I

had to update it, and I wrote we are not done. Yeah, we were not done, and we're still not done, by the way, because they also tell you we didn't apply yet AI optimizations, so we'll see this thing can accelerate. But AI is not going to magically give you physical qubits that work perfectly, by the way. So, just

saying. Now, these are two important metrics, there are more, another important metric, but really those are the two most important one, number of logical qubits and the logical error rate for two-gate logical qubits. Still, you want to know how many

physical qubits you need to fabricate, because you need to actually do this thing, it's not just an algorithm or a paper, for a given logical qubit. So, depending on the it really depends. Depending on the technology, depending on the connectivity that you have between the

physical qubits, depending on what you want to correct, depending on the required logical error rate that you need, you can need like 100 physical qubits for one logical qubit, or 1,000, or 10. It really it really depends. What I want to urge is to not to mix results from different technologies and picking

the best results and the best specific metrics for one technology, putting them together with another technology, and then draw an exponential curve and say, "Okay, we are doomed in 2 years." That's not how it works. So, please focus on the specific technologies. All right, but just to give another

example of how these things go fast, these first two results you can actually really compare, is the same assumption, same architecture, same people, and we had a reduction of physical qubits. This was to break RSA, not ECDSA, but it still Shor's algorithm, from 20 million to 1 million physical qubits from 2020

to 2025. We had a more recent paper who also made the news and said only 100K physical qubits, but there are completely different assumptions on the connectivity of the physical qubits. Also, the computation would take 1 month with a very, very optimistic uh clock cycle. So, you should check uh what they

actually say in the papers. Now, we talked about the risk. Now, let's talk about timelines, and I mean predictions, like when will that happen? We know how powerful this quantum computer needs to be, but by when will we actually get it? Of course, nobody knows the future, but I want to give some data points and what

people are saying. So, first of all, we should know we shouldn't ignore that there is a minority view, it's a minority view, but it's there. There is some skepticism on whether we will ever, ever be able to have any quantum computer like at scale, hundreds, if not thousands of logical

qubits at an extremely low error rate that by the way is like 1 e to the minus 12, 1 e to the minus 15. There is skepticism based on the nature of noise. Now, there is a big rabbit hole here, there are other also more exotic views on this will never happen, but this is a minority view, and honestly, we

shouldn't uh rely on this. The risk is real. So, uh the other data points we have is NIST. NIST actually mandated uh post-quantum cryptography by 2035. We need to migrate. If you want to be compliant, you need to migrate. ECDSA disallowed by 2035. No way around it.

So, you would you wouldn't be compliant. In the same document on post-quantum cryptography standard and the migration, they also provide some standardized post-quantum crypto based on uh yeah, lattice space cryptography or hash based cryptography. The signatures are much larger, as you will see, but yes, there

is a path there is a mandatory path towards migration. Why post-quantum? Because these are not affected by Shor's or any other quantum algorithm or any other classical algorithm that we know. You cannot break these forms of digital signature schemes. There is even Sphinx based.

Then, what do we know? Industrial roadmaps. And of course, you should take industrial roadmaps with a huge grain of salt, you know, but uh still, I also want to say that some companies were actually pretty good in almost respecting their milestones. Others were completely wild and super aggressive.

So, you can do your own research on this, but yeah. I did, and from my understanding, I see two main milestones pretty much centered around 2029, 3 years from now, 2032, 6 years from now. And the first is many of these companies project to be able to reach hundreds of logical qubits at a rate of 1 to the

10 to the minus 8. That's definitely not enough to run a Shor's algorithm to break ECDSA for what we know today. But, still, I guess this is when it really gets undeniable. And it's if you don't do anything when this happen, then panic really. It's time to panic, and you don't want to reach that state.

2032 is when we reach thousands of logical qubits and the logical error rate low enough to actually have crocs. That's the projection. It's good to know. It's still in the actual road maps. Then we have DARPA with their quantum benchmarking initiative, QBI. So, they

were They had this task to actually go to the companies that cooperate and want to be part of this plan for the government to understand if there is actually a chance to have an industrially relevant quantum computer by 2023. Uh 2033.

And what does he mean industrially relevant? Not extremely clear, but they also talk about crypto cryptoanalytics and relevance to digital signature algorithm, running Shor's algorithm. So, you know. And what changed since basically end of last year is that they

become more confident on their prediction. And this was recent, March 2026. The new managing director of DARPA is saying that it's more likely than not that we get an industrially useful quantum computer by 2033. And this is new. All right. Let's talk about the current

status, because these are the predictions. And you know, we cannot do road maps. The companies can do road maps. DARPA has an opinion, but at the end of the day, what do we have today? Like can we run Shor's algorithm? What can we do? And uh experimental progress on Shor not

much. Honestly, um many of these results are debated. How much they're legit, how much they're cherry-picked or pre-processed, post-processed, optimized to get the results that you want. World record is probably just still 15. But, this doesn't matter much. I just want to put it out there. This is true. It's We

don't have a lot of progress on actually using Shor's on quantum computing, on physical quantum computing. But, again, you don't want to wait for seeing this exponential starting. So, but this is true. I mean, people need to know.

Then, that's true, but the building blocks are real. That's my main thesis. That's what I want to say. The current status is that we do have the building blocks. There is no reason to believe this never happens, in my opinion. So, why do I say the building blocks are real? The logical qubits are real. We

have more companies. So, not only Google, more companies have proven that you can apply quantum error correction codes. There are also improvements on new algorithms for correction, and you can bring down the error rate from the single physical qubit to one logical qubit. So, this kind of works.

And then, and what scalability is still a huge, huge question, because you have to do this at scale. Interconnects are also real, and this is big, because, you know, we are reducing the number of physical qubits, but we will not have all physical qubits on a single chip. You will find You will need

a way to connect different chips and to, you know, connect logical qubits from one place to another. And this is an example from So, I go on to my liking because, most likely, for any technology, in the end, interconnects will be based on photonics. So, they do have here an optical fiber cable, and

they have an interconnect with an error rate of less than 1%, which is actually super bad. You know, it's You need 1 to the e to the minus 15, 12. But, at least it's there, and the building blocks are there, and we It's time to start working on scalability. And yes, the gap to be closed is still

huge. Where we are is yes, less than less than 100 logical qubits. But, again, you shouldn't focus too much on the number of logical qubits, because you want to know also the logical error rate, if they actually do correction or only detection, if they do post-selection.

So, yeah. The thing is, we are extremely early. This gap is huge, you know. It has been reduced, but it's still huge, really huge. And maybe the the big step will be to start showing real scalability at the logical level with the computation at the logical level. But,

yes, the building blocks are there. And this was also the conclusion by Scott Aaronson at the end of last year. He was saying that all the key building blocks are in place, and the only questions that are left are a huge question about time, money, engineering, and willpower. That's a lot.

Now, let's talk about Ethereum. And the thing is, why do we care? Because Ethereum relies a lot on elliptic curve cryptography at all layers of the stack. Everything is broken. So, yeah, everything must be replaced. But, you shouldn't feel like sad about it or oh, no, the doom is coming. It's not just

protecting ourselves from the doom, but it's also improving Ethereum. It's an opportunity to rewrite certain parts of Ethereum in a way that is so much better than what we had. So, it's an opportunity to remove all the technical debts, right? So, all the layers rely on elliptic

curve cryptography. They must be replaced. We do have a road map, post-quantum road map at the website pq.ethereum.org, very nice. We do also have the same road map in the larger straw map of Ethereum. And the target is to reach hash-based post-quantum L1 by 2029. This is very aggressive, but I

feel like we need to be aggressive. It's not like we have huge margins. So, I I really like to see this. Let's look more in detail at consensus. So, what breaks in consensus? BLS signatures. BLS signatures are used by validators to vote on their view of the chain. This is where consensus happens.

And if this is broken, it means anyone can impersonate validators and forge attestations. So, absolute disaster. Of course, BLS must be replaced. And that's really a bit of a pity, because BLS is very nice. It's beautiful. Not only is a small signature, but also when you put many of them together, and you need to

do that, because you have to see how the validators vote in aggregate. So, when you aggregate all these signatures and you have one aggregated signature, it's still as small as the original signatures, which is amazing. And we need to aggregate. Why? Because we have uh

huge amounts of validators. We went over 1 million, and yeah. It's going down now because of consolidation, but still huge. We need to aggregate. The problem is that we do have a replacement in theory for post-quantum cryptography. It has been standardized by NIST. But, the signatures are huge, and they're not

well suited to aggregation. So, what are we going to do instead? We don't aggregate the signatures. We prove the signatures and the aggregate signatures and the aggregate the proofs. That's the strategy at consensus level. Next, for execution. So, execution, yes, the problem is very clear. EOAs have a

hard-coded way to spend to verify spending conditions. There is only one way, that is to sign with the ECDSA. And that's really, really bad, because this is going to be broken. So, there's no way around that. This must go. This must change, because if someone can extract your private key from your public key,

and that happens as soon as you send a transaction, your public key is exposed, well, bye-bye to your funds. So, this has to go, and it's time to move on from EOAs. It's time to move to account abstraction, but for real, you know, native account abstraction and such. And then, at that point, you can change. You

can do have algorithmic agility. You can change the spending conditions. Put whatever verification logic you want, and you may very well put post-quantum cryptography. Now, post-quantum cryptography is expensive in terms of signature size, in terms of gas cost. So, if you actually

want to verify post-quantum crypto using account abstraction, you will probably need some pre-compiles. And we are looking also at lattice-based cryptography. But, what will probably happen in the long term is that we'll use proof aggregation also in this case. It just makes sense.

And there is also a question about lost coins, because this migration will not just happen. You require the users to move to non-vulnerable accounts. And there is a question about abandoned ether. Like, there is some There are some EOAs for which nobody owns the private key, so

they cannot be upgraded by the user. So, there will be a highly potentially controversial question on what to do with these abandoned coins. But, relatively good news is that we're not talking about 10%, 15% of the ether supply, but some estimates, because it's an estimate, pointed at 0.1% of ether

supply. And maybe we can take the loss here. Maybe. So, what can we actually do today? That's also an important point. There is a trick. I mean, this was very smart. This is a e-research post by Matteo Riva Labs. And you know, you can use account abstraction today to implement automatic

rotation of ECDSA keys. So, as soon as you spend your with the ECDSA, the spending conditions are updated to the next key. So, someone can try to steal the private key from the just-spent public key, but nice try, it's useless, because you just rotated to the next key. So, that works. It's not the

perfect, final-state solution, but it works until we have proof aggregation. And if, you know, if crocs start working tomorrow, like we actually have cryptographically relevant quantum computer tomorrow, because, you know, China was building a secret to this huge quantum computer, and it started

operating tomorrow, Vitalik had this idea to use snow proof of knowledge of seed, because, you know, the ECDSA keys are get are extract are derived from hashing the seed. And hash functions are not broken. It's just a quadratic speedup. And so, you know, you can just prove that you own the seed, and then

you unlock the funds. Why unlock? Because, in case of emergency, you disable ECDSA, because you cannot spend them. Otherwise, the magic, you know, the the suddenly revealed quantum computer will steal everything if if fast enough. And uh this is not just an idea, this is

getting implemented by the team at Neverlocal, so things are moving, you know. And that's the message. There is no time to panic, but there is also no time to relax. And Idiom clearly is not relaxing, it's taking very seriously this, which is awesome, you know, in my opinion. All right, I'm done. Thank you.

And uh yeah, if you have any question or want more details, >> [applause] >> please. [cheering]
