---
title: "The AI Detection Illusion"
speaker: "Alec Novella"
organization: "Sherlock"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=z1D69OZvGO0"
transcription: "youtube-auto-captions"
---

# The AI Detection Illusion
**Alec Novella** (Sherlock) --- Burton Stage

Hi guys, how you doing? Um, my name is Alec. I work with Sherlock. We're the complete life cycle security company for Web 3. I've been the head of marketing at Sherlock for the past seven months now. So, I've been really focusing on AI auditing, you know, web 3 auditing as a whole and just the complete security

stack. Just a quick about me. Um, I've been in the web 3 space since 2021. Um, I worked at an exchange infrastructure company called Shift Markets before this. Um, I started as an analyst. I was a business analyst. Then I was a marketing analyst and then I

started doing growth marketing and now I'm leading marketing at Sherlock. I helped grow my last company from 2 million ARR to 14 million in three years, which was a big accomplishment. And I'm an avid collector of Pokemon Yu-Gi-Oh cards. So, anyone that has vintage Pokemon or Yu-Gi-Oh, please let

me know and we can connect about that. So, the topic of the talk, the AI detection illusion, why more findings is a terrible go to market metric. Um, I wanted to talk about this because my role at Sherlock has been bringing Sherlock AI to market. Um, we launched in October of 2025

and it's been like a very competitive space between us, Octane, Nethermines, Cantina Spearit just recently launched theirs. So, the space for AI auditing is growing really quickly and I see a lot of deceptive marketing, bad sales behavior. Um, there's some fishy stuff going on. Um, you know, I don't want to

say Sherlock's participating in any of it, but, you know, I see firsthand a lot of what happens in the space. So, we're going to go over the tech, the capability, the problem, and a better approach for assessing AI auditors.

So, first and foremost, what's an audit? I'm sure everyone knows what an audit is here, right? So, it's a manual review of a protocol's code before you launch or a major upgrade. It's usually done by a security team of three to five people over a few days or a few weeks. The goal is to catch vulnerabilities before they

get uh an exploit can happen in production. And it's very slow, it's very expensive, and it's cumbersome. So, you know, every protocol has to have an audit if you're operating on chain. you know, it doesn't matter if it's, you know, a small DEX or a massive yield aggregator like a

protocol teams invest hundreds of thousands of dollars on auditing on average um for every major upgrade. So, it's still a very nent and not the best way of performing security. Um, so what's AI auditing? So this is a new

security paradigm that's actually come up in the past two years and it's a specialized system that actually analyzes the code while it's being written as opposed to right before launch. So it's meant to save time, money, energy, and it helps find issues before they get buried deep in a

protocol's architecture. It does not replace human auditors yet, but it's improving really quickly. And the primary supports are for Solidity, Rust and Go. And the majority of leading protocol teams are adopting this technology. So Ethereum Foundation, a morpho, they're all using these tools

at this point. Um, and the adoption is happening really quickly at this uh at this point now. These are some of the big names in the space. Sherlock AI, you know, um, Nethermind, V12 by Zelic, Octane is, you know, probably the oldest and has the most market presence as of right now.

So, how does AI auditing actually work, right? Typically, it'll connect to a repo or codebase and, you know, an an or a pull request and it'll analyze that code as it's getting adopted into the greater protocol. Typically these tools will do static analysis and LLM reasoning

simultaneously. Um and that LLM reasoning is typically through um a frontier model like Opus, ChatgPT or Gemini and a lot basically I would say the majority of these model of these AI auditors are actually aggregating those frontier models together um then

using an anentic flow to analyze the code of the protocol that's being audited. Um, typically the the end result is usually a set of findings like an audit report that says how many vulnerabilities there are, how to fix it and how to triage basically, right?

And that's the that's the basic flow of it, right? So um static analysis, LM reasoning, raw report, a human triager will look to see if that the triage results are actually accurate and then from there you'll rescan it to see if that actually fixed the issue.

So this is the the thesis of this talk is why more findings is a bad indicator. So, I've seen a lot how, you know, a new tool comes out or a new upgrade for an AI analysis tool comes out and they'll say, "Oh, you know, we found 20 vulnerabilities in this major repo." And

I'm going to tell you why that's faulty. So, raw finding count hides the mix of vulnerabilities. So, a lot of the times if a new tool comes out and they're flexing that they found 50 new vulnerabilities in this major repo, if 46 of them are infos, two of them are mediums, and there's one high, you know,

you're being deceptive with the vulnerability collective. Um, it doesn't really say anything about usefulness. So, it doesn't say how many false positives there were, how many duplicates there were, how much human triaging went into that. Um, and it sets a bad buying framework. So buyers start

judging AI auditors by raw counts instead of how well they understand the code, how they understand the exploit paths, the suggested reviews it provides, and how the the new code changes, how it integrates into the greater protocol. And then this is even more common where

an AI auditor company will say, you know, we found five crits in the latest a upgrade, right? That's a very deceptive tactic that's actually used a lot. Um, you know, severity class is subjective from company to company. You know, how Sherlock assesses a high versus a crit is different than how

Nethermine assesses that from how Zelic assesses that. So, you know, just by even saying you found five crits, there's no universal agreement as to severity class. So, in nature, it's not the most it's not the strongest metric to be touting. The coverage matters as well. So,

something I've seen a lot is that a new tool will come out or a new upgrade for a tool and they'll run it on a codebase that they know is problematic and has really low hanging fruit. So, say it's like an audit contest repo that they know has like 10 highs that are very simple and easy to find. They'll run

their tool on that be like, "Oh, our tool found all 10 of those easy highs, right?" And they're not going to say that they like the coverage or the scope of that audit contest was very simple, but it makes their tool look amazing. So, um then top severity results can be

manufactured to look stronger than they are. I basically just went over that point, but noisy legacy code, pre-exposed vulnerable code. Also, they'll take a human audit. They'll perform a human audit. They'll scope out exactly, you know, what happens in that audit and then they'll they'll rerun

their tool on it and they'll map their tool exactly to how the human actually performed in that audit and just say that their tool found it. So, I know that the majority of companies are doing this. So, what's the downstream effect of more findings and more crits and more highs?

Um, for one, duplicates. So, duplicates are a huge problem for AI auditing solutions. Say there's a tool that runs on your repo and it finds five highs, two crits. A lot of the time if there's not a dduplication process, if there's the same root cause that's actually causing like four of those highs, it's

going to mark each of them individually. And to the AI auditor that's being marketed, it's like, you know, it found all these different vulnerabilities. It's not saying that there's that one root cause that actually was causing everything. False positives are a huge problem, too.

So a lot of the times, you know, it'll say that there's a vulnerability when it's just not true at all. These tools are designed to save engineers time and energy. So when they're actually like investing a ton of time into hunting down false positives, you know, dduping on the on their own, um it's a super

heavy human burden, right? Like if you're going to be spending x amount of dollars per month on an AI auditing tool, um you want to be dealing with as many or as few duplicates as possible. You want to make sure the tool is dduplicating as much as possible and that it's actually saving your

engineers time and energy because that's that's what they're good for. So, when you're actually buying an AI auditing tool, from my perspective, as a, you know, somebody that's seen what works, what doesn't work, I would say if you're going to, if

you're going to put a checklist together, and I put this little fridge magnet here of, you know, buying an AI auditor, the number one indicator I would look at is how many findings survive triaging. So, a lot of the times if you're buying an AI auditor

and they do a demo on your codebase, it's really important to get clarity on did a human triage these results or is this just like the raw results straight from the AI auditor. You know, because the vast majority of time these protocols are going to give you something that's had a lot of human

triaging, a lot of human hours to make it look as good as possible. How many issues collapse after dduplication? If there's still, you know, 20 vulnerabilities, but they're very similar in nature, your engineering team is going to be spending a lot of time just dduping and wasting their time

trying to hunt down what's real and what's not real. So, how well is a tool reason about PRs, upgrades, understand the broader codebase interactions? That one speaks for itself. You know, you want to be you want your tool to get smarter the more that you use it. So I say it's really

important that over time you know it can aggregate the information about your protocol the vulnerabilities it's finding the broader code base it's analyzing and then are the suggested fixes actually useful and accurate. One of the most valuable parts of these tools is

that they give you a suggested new code snippet. You know a suggested new way to fix a vulnerability. If it's wrong four times out of five your team's going to be wasting a lot of their time. That's a lot of the value there. So, when you're buying, really pay attention to the suggested fixed review that they

provide. And does the product reduce reviewer time or does it just shift the burden around? If your engineering team is using one of these tools and they're finding a ton of great stuff, but they're spending four hours dduping, you know, getting rid of false positives,

just making sure that the findings are actually accurate, it might not be worth it. you know, engineers are very expensive. So, um, keep that in mind. The number one indicator is that is it saving your engineering team time and energy. Um, just as a finisher, you know, human

audits still matter. In my opinion, I think, you know, auditing is like 90% human right now and 10% static analysis and AI auditing. I think in the next three to five years it's going to shift probably like 80% AI and static analysis and then human review will be reserved for the really important high stakes

upgrades and code changes. Um but in the current state like you still do need a human audit for high stakes upgrade or release. Um top auditors are not going to get replaced in the next few years but you know the lesser human auditors are definitely going to have some economic

challenges in the coming future. Um model progress moves really quickly. Like I said the majority of these models are using you know frontier models like opus chatgpt. So pay attention to how those upgrades actually get integrated into these tools because it's really important that they they can do that.

And benchmarking matters a lot. You know, I could have spent a lot of time talking about EVM bench which just came out. Um and it's useful useful for testing certain capabilities, but it doesn't answer every buyer question. So I didn't want to focus too much on benchmarking

for this talk. Um and a strong demo is not the same as a strong product. Just be wary, you know, if you're actually getting on a demo, if an AI auditing tool is actually getting right on your codebase. Um, be skeptical. Ask the hard questions. Ask how much human time went into producing

those results. How much triaging and dduping was not automated. Like that's my biggest piece of advice. And that's the talk. So, thank you. Any questions? First one is um why would I buy a tool and why would I not uh develop it myself for example?

>> That's a really good question. So, you know, from Sherlock's perspective, we have a ton of proprietary data from audit contests, private engagements, and that it's very valuable data that we could route those frontier models through and then have an agentic flow to perform the analysis. If you don't have

that proprietary data, you know, you can still get some pretty good results, you know, maybe aggregating frontier models together. But the engineering lift of creating those agents, not having that data filter for a better interpretation, you're going to be limited in how functional it's going to or how it's

going to perform compared to Sherlock AI or Zelic. As far as I understood um those models are generic or something not trained models on uh on let's say u bad code quality data or is it >> they are well they are fine-tuned and

there's ways like you know like if you know Gemini 3 is better at finding certain vulnerability classes or you know that you know Opus 4.6 is better for like agentic orchestration. there's ways of actually it's not like you're just having all of them blast the same code simultaneously with the same

prompt. Um they play different roles. So if you have a lot of of you know if you're a great AI engineer you have proprietary data you understand agentic flows you could build one yourself for sure but it's a big lift. Final question. I think I answered it myself because you talked about um how

much uh human resources went into a review. So this is uh more like um when when you let's say you you test how good your results are, right? That's what you meant. So you have use cases, test them, get results, get faults, and then you say, "Okay, that's what I expected. There's not too much hallucination on it

or any false positives." So that's pro my prompt is good. So in this >> so what's the question exactly? I'm sorry. >> Yeah actually. So this is what you meant with um because you you talked about human reviews >> of uh we should ask the developers of

the software how much time of human review went in and this is this sort of human re review what you were talking about right >> definitely like I said like a lot of the time you know if an AI tool is running on a new repo or new codebase it doesn't have all that context or they don't know

of how well it's going to function um humans are spending a ton of time dduping and a ton of time, you know, collapsing down the amount of issues, making the suggested fixes perfect. So, I know that these companies do this. So, just ask them that and see how transparent they are about that fact

because you know that dduplication then the the how well the tool could do it on its own is very important. So, was there another question? Yeah, I'm curious. So I mean >> so I'm just curious about the other side. I mean the attack surface is also kind of becoming much bigger because uh

I mean the attacker can also use the same tool and uh do you have any idea what uh kind of like criminal hackers use in order to uh find the loopholes and so on? That's a great question. And the the attack side, this is like focused on the defense side. I don't think attackers are going to be using,

you know, Sherlock AI or Octane. You know, maybe they could find a way to clone it and, you know, use it on their own, but attackers will be using AI and they're going to be way more effective at hacking with AI in the coming years. So that's why, you know, still relying just on human auditing is very limiting,

right? Right? It's like you need that extra layer of defense while you're actually developing the code. You, you know, human audit still is essential, but yes, hackers will be using AI. They're going to be making their own advanced AI tools like these ones I just mentioned,

and it's going to be causing the majority of hacks in the future, I believe. Any other questions? >> What about real time analysis? Like imagine there's a contract that's already deployed, it's been pre- audited. Um, and there are actions that

are occurring on the contract that might suggest that a potential vector has surfaced. Um, is there any real-time analysis that you that you guys can do? For example, >> in its current state, no. And that's like that's something we should definitely be building out, you know,

like active analysis like in our current state. It's like when a protocol is actually live like a bug bounty is like basically like our way of like keeping eyes on live code. Um but you know the way we're envisioning Sherlock AI in the future is that like it's not just used during

development or auditing like it'll be used while protocol is live you know with real-time analysis. Um, so that's a great point and that is something that I in my expectations of the future absolutely that the tool is going to be used for live protocols as well. Any other questions?

Thank you guys for your time. I appreciate this. This is fun to put together. Thank you.
