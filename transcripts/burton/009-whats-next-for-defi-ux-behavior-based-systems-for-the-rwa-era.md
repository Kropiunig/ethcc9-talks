---
title: "What’s Next for DeFi UX: Behavior-based Systems for the RWA Era"
speaker: "Yeho Hwang"
organization: "Ondo Finance"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=iERztx7RXeI"
transcription: "youtube-auto-captions"
---

# What’s Next for DeFi UX: Behavior-based Systems for the RWA Era
**Yeho Hwang** (Ondo Finance) --- Burton Stage

Okay, sorry. Oh, okay. Hi. Um, today I'm going to talk about a new framework that I've been working on since late last year. It's called the human orbit model. And I know it might sound a little abstract, but it's really centering a behavior-based system for

end users. And uh, I just with a show of hands, who here is a designer, product design? Nice. Two. Okay. Three. Okay, perfect. Um, any product people, managers, product managers, mostly builders, developers. Okay. Um, what is common among us, I think, is the need

to focus on end users, right? Uh we've often discussed what we're going to build and how we're going to do it, but rarely as a product designer have I paused or um even heard my co-workers previous and current talk about end users in a really deep way. Um understanding why they use the product

and who they really are. Um, by the end of this talk, my hope is that one, you'll understand why architecting DeFi UX is more complex and layered than traditional financial systems. Two, you'll shift from describing users in static formats to understanding them from a behavioral perspective. And

lastly, I hope you that I hope that you'll walk away um thinking about how your users map to your own product ecosystem. So your pro or your users are not byproducts of ideas. It starts with them first. They I guess your products are the result of

understanding them in depth. So I'm hoping that by bringing back the conversation around being user centered, I'm hoping we build a more resilient DeFi UX and product ecosystems, the RWA era. Um, and what I mean by RWAs is

treasury, US treasury debt, commodities, corporate bonds, um, tokenized private credit, etc. So the total val yeah yeah the total value in 2024 was just 1.6 6 billion which is still a really large number but comparatively to the traditional finance sectors they operate with trillions of

dollars right and just a year later in January 2025 we saw that number quintuple and just earlier this year according to rwa.xyz XYZ, that number from 2025 almost quadrupled. So, we're seeing this product market

fit, especially at Ono Finance, which I work at. Sorry, I forgot that introduction. Um, can you tell I'm nervous? Um, yeah, I've seen this exponential growth firsthand. And if you're not familiar with us, we designed institutional-grade

platforms, assets, and infrastructure to to bring financial markets onchain. In early September last year, we released on the global markets a dedicated tokenized stocks and ETFs product and we've seen since become the leading tokenized equities provider with as of last week it was 2.76 billion TVL

including USDY OSG. Um we have over 200 plus tokenized equities and ETFs and about 80% yield coin market share. So in the past two years alone the RWA world we proved that we can put treasuries on chain and we have liquidity yield institutional participation and increasing regulatory

participation. And the more we explore ways to lower barrier of entry for non-cryptonative users because as soon as institutional partners integrate to be more onchain their products will stream down to non-cryptonative users on tradi. So the more we consider designing for them the

more tradeoffs we have to make. And my whole thesis of being a designer is being inclusionary than exclusionary. But the thing about DeFi and web 3 UX in my experience is that there's so many different layers we have to consider while the regulatory frameworks are

still being defined not just in different countries but across the globe. um the design or the users we design and build for are more borderless. So for example, from a US perspective because that's where I come from. Um we might think about 401ks

and designing for that space is very linear. We know historical patterns of user behavior and we can hypothesize on those historical behaviors. Whereas in D5 UX, things change all the time and we're witnessing exponential expansion of RWAs within DI

while having to consider so many layered and different user needs. And that's exactly how I've been thinking about design at Ono Finance. And before I dive in, I wanted to quickly introduce myself. I have over eight years of experience in design, most of which have been in web 3

and this is my second time presenting at ECC um to talk about web3 UX and I just wanted to quickly thank the ETCC team for having me here again. Now that we've established that RWAs definitely have traction, adoption, and regulatory participation,

I wanted to introduce a shift to behavior, oh, sorry, behavior-based user profiles. When I practiced this in my hotel room last night, I sounded great, but with like eyes staring at me, I'm a little frazzled. Um, but before I dive in, who here has heard of personas? Okay, so a fair amount out of those

people who have used them this month, this year. Okay, popcorn. Um, what do you think of personas so far? experience. >> Nice. Thank you for sharing. >> Oh,

>> I think people have seen this often um especially with the use of personas. Sometimes we say meet Alice the crypto native investor based in XYZ. They typically show in personas uh an identifier. So who she is, her needs and goals in terms of what she

wants to achieve and uh her pain points, what's getting in her way of achieving that. And it also goes into sometimes the tech stack of her either tech proficiency, web 3 proficiency, or a list of apps related to your product or service that

she might be already using. But Alice's ability to buy tokenized bonds or stocks is directly dictated by her environmental context, too. her local laws, access to on-ramp, financial literacy. So, what I have been feeling the past few years missing in personas are the

environmental contexts, functional versus intrinsic motivations, answering not just what she wants to do, but deeply why she does that. It also lacks emotive and behavioral influences as well as her relation to other users in your product ecosystem

and how they and the other people in her life that might be changing her behavior or thoughts over time. So in short, personas are portraits and they show who someone is at a moment in time, resulting in a very static summary and a single point of artifact

that usually doesn't get updated over time has been my experience. we often used power user um and I would often question okay what does that mean in relation to the specific feature I'm building and why would they find this feature relevant in their already increasing

amount of stacks. So that's why I started wondering where is Alice in her DeFi journey compared to other users in your product life cycle and how does her specific needs, motivations and pain points map to any specific one of your products or features.

This meant for me a shift from personas to profiles. And I know you might be wondering, isn't that just a renaming of one word to another? I'll show you why that's not correct. Um, profiles for me are deeper. They record how someone behaves, adapts, and influences other people in their

lives over a period of time. It results in a more dynamic and longitudinal artifact that the team can always reference a more holistic understanding because their profiles are defined in behaviors, motivations, and contexts they operate under. It really allows your users to be human

first. Um, I often find that again they might become the byproducts of your ideas. Your product is the result of your users and understanding them deeply. Profiles also allow the team to operate with layered data. Oh, it's not synced.

Oh, it wasn't synced correctly. But the essence is that we need to start designing solutions based on behaviors and not just static characteristics. And especially in this age of automation, templates and convenience, what differentiates your product is the depth and understanding you have of your

end users. So in short, as you see in this iceberg, the top 10% is what we can see with our visible eyes. core identities, demographic information. Whereas the bottom 90% that we often miss is the why of why are their choices rooted in XYZ motivations.

How is their environment, whether that's temporary or permanent, influencing them to make certain choices? And this isn't a prescriptive method at all. But for me, as I was thinking about this shift from static descriptions to more in-depth descriptions,

I started thinking about what could exist at the top of the iceberg, our core identities and behavioral patterns that are visible to the eyes. Whereas again the environmental context and motivational drivers are often deeply ingrained in a person and needs to be investigated more deeply.

So, as you can see on the right, they all influence each other because try to think of the last time you bought into a product or service like Coinbase versus MetaMask or walking versus driving somewhere or riding public transportation. Why? What influenced you to make that decision? And how has

choosing that product or service changed your lifestyle over time? And uh you might be thinking this still feels a little abstract. This seems like it's a new idea. How does this work in practice? And where do I start? Do I just rename my existing personas to profiles? Um I

don't recommend doing that. And you might be wondering, will this work for my team? Is this relevant for my dad? Maybe you work with a team of three or 10 or you might be coming from a larger organization. That's why in tandem with um user profiles, I defined something called

human orbit model to help teams map your profiles to a dynamic ecosystem with each orbit defining um your profiles based on time to value horizons and product relevance. Before I dive in, um, let me start with an admiration of our solar system. When there are two suns

in the solar systems, which is impossible. If there were two suns, our earth would essentially be uninhabitable. I'm not an astrophysicist, but we have something to learn from the way that the solar systems architected. So I started thinking with the gravitational push and

pulls with these different orbits, can we think of a way to exemplify our product ecosystems? Because that's true for companies too. As you just saw, if your product has two hero products or two hero features, then your users are going to be confused. There's a saying in UX where if you

design for everyone, you design for no one. So without a concentrated effort to understand where your users sit in your product ecosystem, what products they benefit from, are deeply engaged in. This confus confusion might happen. That means maybe delayed engagement of your users to your

product, drop offs, etc. So as you can see if there can be one hero product to maintain a concentrated top of funnel to conversion to ret retention cycles to um secondary and tertiary features to support conversion and distribution efforts

and users don't always buy in from the beginning especially if your product is new. I started to think about having a better way to account for all of the users in a product ecosystem while considering business goals. So who are your users and how do they relate to your products or services?

There comes a point in product growth where you feel the pain of competing priorities or resource allocation. Um teams might be working in silos on separate work streams but may have layered uh features and they need to be more in contact. You might be wondering where do you hire?

Which features are table stakes and which ones are nice to haves? So, we need a better system to allow us to map user profiles in a way that helps with road mapping, alignment, prioritization, and resource allocation and more. Sorry,

it's not syncing. Um, so all of these things, road mapping, alignment, prioritization, all of them deeply are ingrained with how much you understand your users. And I keep saying how much you understand your users because I'm not asking for a label. I'm not asking for

who are your users. I don't want to hear I think they're cryptonative. They're power users. I want to know how they feel when they interact with your product. I want to know why they found your product, how they found it. So again, this whole model was inspired by the

solar system. At a maximum, I'm thinking about three orbits that your user user profiles can be mapped to. I say three because humans best operate in threes. Memorization often happens in threes as well. And I think more than three orbits may end up making products or features more granular than they

should be, especially when you're first starting out. And again, it's inspired by the solar system where planets take time to orbit around their distance and gravitational push and pulls between each profile to your hero product. At the core

is where your hero product sits. It helps answer what product value do we have today. So the user profiles in this center orbit map to a loyal customer base. They benefit a lot from a hero product. They're deeply engaged, value aligned, and have shorter shortest time to value

horizon. They are more influential in helping define shorter term roadmap decisions because they're more deeply aligned with your hero product. The secondary orbit is helping answer which next immediate distribution channels you invest in after your hero

product has released or has achieved product market fit. So these secondary user profiles benefit from some parts of the product but not all. They enjoy the product but are not necessarily loyal to it yet and have a little bit of

longer time to value horizon than the core orbit. They help define the next step post product market fit or post release. And then thirdly, the expansion layer that that orbit is furthest away from your hero product, meaning they answer

how else you can expand and where else. because they're more tertiary user profiles. They aren't exactly loyal to any specific part of your company or product, but they're curious enough to find you and interact with your

platform. And um these user profiles in my belief are the best to interact with when wanting to understand how you might innovate further. What other strategies do you look into? So, as you can see, because they're not siloed in different

work streams or parallel efforts, and because they're mapped in accordance to a specific orbit with the expectation that they might shift around based on their changed behaviors and priorities. They're no longer fixed to a characteristic. They're live contextual people with

intrinsic motivations that fuel their choices of why they want to interact with your product. This fluidity, in my belief, allows us to redefine product iterations based on behavioral archetypes and not static personas. I have nothing against personas. It's more of my

oh it's more of my um experience having designed in this space and wanting to shift the conversation a little bit to understand users more deeply. Um again this fluidity allows us to one and then two identify further distribution

opportunities by observing how users go from one orbit to the next while allowing you to leave room for hypotheses formation and experimentation. And thirdly, this fluidity in the orbit model allows teams to expand responsibly by understanding cultural contexts,

environmental contexts, and user behavior and user knowledge built over time. So, you might be wondering, how do I actually put this to use? Um, is it just a framework I'm going to forget in a month? I hope you don't because I want to piece everything together with you

and talk about practical applications for teams based on your team size. And this isn't a one-sizefits-all solution, but it's a recommendation. Let's start with a small team with one product or service. You might be a team of one or five or 10. You might be operating under the

context of wanting to deliver first and help define user definitions later. Your priority might be speed over perfection. You want to validate and release first. Um my recommendation here is to just focus on what your hero product is that sits in the core orbit and just one user

profile. No more than that. So it might look like starting with one user profile to help define your product, building for the short term with the northstar understanding that there may be further orbits beyond the core orbit testing to inform how your user profile

gets reiterated on you. The screen went dark a little bit. Um, you might be uh scale up with a product market fit. Oh, so your context might be that your product has launched with success. So, congratulations.

Your priority here is to stabilize your product, decrease any tech debt, design debt, and start to capture more market share. My recommendation for teams of this context is to continue refining your core orbit and if you don't have one, define it and house your hero product

under it and define a couple user profiles that benefit from your product so far and look ahead to what distribution orbit might look like. So this might look like aligning on a shared language of how to call your user profiles, refining your core orbit and how your

profiles are mapped in accordance to the hero product. Identifying what might map to distribution channels through the distribution orbit. operationalizing this practice to derisk expansion because once you have a PMF product with scale up behavior, I know just how much

you move with speed and efficiency. So in by operationalizing a shared language and this model, I'm hoping that it helps the team derisk any assumptions you might be designing with. And uh I recommend implementing the orbit model in road mapping. And if you do, let me know. I'm on

LinkedIn, Telegram. I want to hear about how you're using this framework. And as always, you should always continue validating and refining your understanding of your users. Anyone from medium plus-sized companies like 500 plus people?

Oh, nice. Where are you coming from? >> Oh, okay. Hi. Why are you here? I'm just kidding. Um well in this context design product research teams might have established processes and the priority here might be decreasing delivery disruption

as much as possible. And my recommendation here is to try pilot programs in smaller pods to measure return on investment of switching to this model and this deeper understanding of your users. Measuring internal sentiment of how this is working for them.

So this might look like identifying lowcost high impact pods where let's say you've perfected your onboarding flow. So they're they've stabilized, they're looking at new features. They might be a lowcost high impact pot because users are still streaming in but breaking that

funnel might be a little bit lower cost depending on the situation. um versus at the conversion path of um trading for example. pilot this program for one to two quarters to understand what ROI means for you of switching from using personas to profiles

and understand internal sentiment because not everyone might like the shift um when you have established processes in place and understand you might have more than one orbital group and if this gains traction amongst smaller pods. Think about rolling it out in smaller

groups. So my answer is it depends in how you want to implement this framework on your teams. It really varies on product maturity, appetite for user research on your team. there can be just like one person on the

team that champions user research or wanting to be more deeply connected to your users. So it just takes one person and ato I think there were people who came before me that championed users um thankfully and then more and more we started to think more about how we

define users with deeper segmentation and uh it also varies on your willingness to do. I can talk about this new framework all I want and my passion for users all I want today but if other people don't have the willingness to do and implement this framework then it doesn't have traction right um so all

I ask is that you be an experimentter a scientist and create room in your product development cycle to be relentlessly curious about your users so in some we've witnessed We've witnessed exponential growth of tokenized assets accelerated by institutional adoption and regulatory

participation. And because of this growth, we need to evolve how we manage DeFi UX with the changing times. That's why I started working on user profiles at Onondo. And uh it really I really want us to shift from a static understanding of our users no longer power users.

What makes them a power user? Um are there any like deeply ingrained belief systems that they carry that still have them operate as a power user? And last we lastly we covered the human orbit model, a new framework that I came up with to map user profiles in

accordance to a product ecosystem. I'm hoping that this allows teams to no longer work in silos or compete for prioritization. And uh I'm hoping that this orbital system instead of parallel systems help teams see how each of your work benefit the

larger solar system essentially. So as builders in this fastch changing ecosystem, I really believe that it's our responsibility to design with the richer understanding of who each end user is. Because as a designer, I've also been very misled by

my own assumptions of what I think our users do, why they do it. They have thoughts that keep them up at night. They have thoughts that empower them to use your product. They have habits they don't want to replace and habits they're willing to change. They have financial anxieties and

financial power. So users are not a monolith. They're a very diverse group of people. They're exactly like us and in a way they are us. So all I'm asking here is that we know how layered their choices are because our own choices are layered complex.

So my closing thought here is in 2024 as we've seen earlier in this talk when I was much more nervous. Um in 2024 if we say we were building a telescope to see the potential of RWAS with the gaining traction in 2025 we launched the first probes and just earlier this year we're

building user centered systems for scalable products with product market fit with our WAS. So with over I think I saw a larger number. I made this deck over a few weeks ago. So at that time it was 26 billion in onchain value that never sleeps. Um the question isn't whether

tokenization will happen but whether you are creating solutions for the right user profiles and the right orbital placements. So I'll leave with a question. of what your gravitational pull looks like for your end users to your hero product.

And um again, I want to drive home the point that your users are not byproducts of ideas. It really starts with them first. Um because you could design the most elegant solution and it might end up in the wrong audience. And I think what I'm missing in this

year's thesis is AI agents and agentic trading and how they map to a certain orbit. So I might be back talking about that next. Um I think that's it. Thank you. >> Am I over time? No, it's Well, well,

well.
