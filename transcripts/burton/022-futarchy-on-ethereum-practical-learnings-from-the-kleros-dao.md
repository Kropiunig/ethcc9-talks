---
title: "Futarchy on Ethereum: Practical Learnings from the Kleros DAO"
speaker: "0xAlex"
organization: "Kleros"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=0-OR1OZF27g"
transcription: "youtube-auto-captions"
---

# Futarchy on Ethereum: Practical Learnings from the Kleros DAO
**0xAlex** (Kleros) --- Burton Stage

because you have to talk after. >> Okay. Yeah, >> go. >> Hi all. Yeah, it's working. Perfect. Uh so I am Alex. I'm integration lead at Claros. Claros is a decentralized dispute resolution protocol. And uh today I'm going to talk about Futarchy

on Ethereum. Um I'm going to d deep dive into the concept of futarchy and I'm going also to share some practical learnings about what we have experimented uh with the claros da. So let's get into it. First of all, futarch key is an old concept. It was introduced more than 25

years ago in 2000 by Robinson. Robin Ansor is a professor in George Mason University and he introduced this concept of futarchy with this paper called basically futarchy vote values but bet beliefs. In this paper Robinson described a new form of government. In this government basically you have the

democratic process that is like any big democracy with elected representatives. This is the vote values part. It's still really important to keep in mind that free turkey is not prediction market on everything. The vote value part is really important to give the long-term vision and the big goals. But in order

to implement basically uh this policy and achieve specific goals, the how part is done by market traders and this is the bet beliefs that is leveraging prediction markets and conditional markets. So let's dive into it with a theoretical example uh of government as it was

described by uh Robin Hansson is in his paper. So the votes part you have as I said the elect the some representatives that were elected and they try to basically maximize the wealth of uh their nation and uh they choose a metric they choose what metric they choose GDP per capita why do they choose this

metric because usually it's a good approximation of the wealth of a country and also one thing point that is really important to keep in mind when it comes to fit is you want to have a metric trick that is easily measurable and that is really clear to measure. So they took GDP per capita

but the and then they put uh this meme there because usually when you ask people what they want it's not a big uh issue. Everybody wants the same thing basically wealth happiness. However when you ask people how do you get this basically uh you have different answer. Some are less tax some say more tax some

say sacrifice a goat. And this is where in this part where futarchy plays a role in this how to get those. So basically in this one uh you have one proposal one proposal of policy that could be to create a UBI universal basic income. You know some people are proponents some people are opponent and

there could be they have some debate in order to basically run to to do futarchy on this you will basically ask these questions uh into a conditional market what will be the impact on GDP per capita if we create a UBI and basically you create a conditional

market and in this condition conditional market some traders are going to trade and it's basically a way to fork the current reality into you have the real the reality where this proposal pass and in this example for instance the GDP will be 48,000 per capita and you have the reality where this proposal fail and

in this example for instance it's 46k per capita I took this uh this number as an average basically it's the current French GDP per capita and uh basically what happened in the paper described by Rob Rubenson done is you let the trading the markets trade and at the end you choose basically so

you implement the proposal if the past price is above the fail price. So in this case the markets are telling us that if you create a new BI the basically GDP per capita will be higher so you implement the policy. So it's fully futarchic basically uh um process. So this was the theory. This was u tried

in some companies basically never at the government level from from my from my knowledge and uh for a long time uh yes it was just experiment but with crypto basically uh and the power of basically uh yeah open and trustless trustlessness we saw uh new experiments and more successful ones and uh one very

successful one when it comes to futarchy is about metad Metadau basically is a process that is is a project uh built on Solana and uh it was it's a project that got a quite a success leveraging fut in order to fund raise and it's interesting because even media like bankless that is quite

Ethereum align and pro Ethereum invites uh metad in order to talk about futarchy and during this podcast one of the podcaster Ryan he basically asked Yeah, this is super cool. Do we have something similar on Ethereum? And our treasurer Juan basically answer him and say yes, we already have things going on on

Ethereum. We have basically uh Futurki for Dows in Nosis DA for instance, but we also have Futurki in Velora DAO that is the Paris swap DA that that has rebrand recently and also in Claros and I will I will go a bit more in details about about Claros one. All of these Dows are doing futarchy thanks to a

project that is called Futarchy. Uh and Robin Hansen is the chief scientist of this project. It's using basically seir as a infrastructure layer for prediction market and claros at it as its oracle. So let's better understand what is it. So I put it in the title. It might look a bit complicated uh but at the end it's

quite simple. So for Dows we are talking about price based advisory filter key. So I will explain a bit more in details why. So first of all price based why is it price based? Because the metrics we are taking is the token price. Why the token price? Because it's again easily to measure. You can um basically uh it's

also reflecting most of the time uh the strength of a project. If you have a token of a project, you want the price to go up but you also want the project to succeed. Uh it's like the the the token has some specific um tokconomics and the more the project is used the higher the price goes usually. uh so

it's a good metric it's a good proxy and then proposal if you are a bit into Dows we know you know that we have some proposal it's called improvement proposal in the case of claros it's clear improvement proposal for example here it's the 86 I don't go in the details of this specific proposal

but just to to illustrate the thing and we do exactly the same theme thing we run a conditional market what will be the impact on PNK price if we pass this specific proposal and in this case basically we are going to take to to trade on the uh the traders are trading and you get a price

a yes PNK price if the proposal pass and you get a no PNK price if the proposal fail and the big as you can see here the yes price is above the fail price and the big difference here is that's why we talk about advisory filter key it's the fact that it's not passing directly

based on the market price but it's based it's part is the proposal pass or fail based on the snapshot vote and that's a way to basically as it say advisory it's just here to give extra information to the voter and at the end the one that keep the power are the token holder uh and they still can vote in the snapshots

and here is two screenshots illustrating this so you on the right you can see basically the screenshot from fki where you have the yes price trading above the no price and you can see the snapshot from Clios where the vote basically uh was casted by the holders of the token. So let's go now a bit into more details

about the learnings uh from Claros DA. So the three learnings uh that we that we got so the first one is about providing governance signals. So in ClariS we saw different kind of proposal. We saw a good proposal let's say according to Futarch. Uh in this proposal it was about to change

basically some rules about the jurors incentive program. Um yeah this proposal was a bit complex. There were a lot of debate. As you can see the community was split. Two3 of the community was for one third was against and for some basically token holder that don't have the time to go in all the debates and and all the

complexity what they could do they could just have gone into free. look at the impact price the estimate price impact on PNK and see that in this case for instance it was 14% positive on the opposite side we saw also some example of bad proposal we had this proposal for instance to ask for funding

in order to have like to do some research the topic was a bit vague it was not very clear and in this case for instance we saw some futarch key market uh showing a negative price impact for PNK the interesting point Here is we can start to see in the snapshot some voters

and using using basically fi markets as a rational to justify their vote. Then we went further than this. That's the first level of doing governance signal. We went further by basically implementing some safeguard for sensitive proposals. This proposal was passed in the

governance uh basically of Claros and this proposal futarch based governance rule for PNK minting. So minting a new token of a project usually is quite sensitive. Why? Because you are diluting basically uh the the the value of the existing token. So for any proposal that is asking the DAO to mint extra token um

there is an extra rule you need to win the snapshot vase space vote sorry so snapshot vote but you will also need to win the fki market so it's two conditions the only way basically to win it is two condition if you only that's what showing here if you only win one condition your proposal is blocked is

rejected and we saw this with a proposal of a minting a minting proposal that happened in Clios. Uh basically we saw that uh there was a lot of trading on those markets as you can see here. Uh because why? Because you have you had some people that were basically uh

conditionally selling their PNK. They were saying if this proposal pass I want to be out and by doing this basically they were maintaining the no PNK price above the yes PNK price as you can see here. uh so yeah this is an extra mechanism in order to protect basically uh for specific sensitive proposals.

The last point is about integrating with governance tool. We learned that basically the voters are used to some specific tools like snapshot for instance that's why we integrate with snapshot in order to have directly the price uh of those markets integrated in the plug-in. So most of the voter they

don't go in details in the forum they just look at the snapshot uh proposal and here they have directly this extra information from the um fut market that are there and also recently there was this delegate futarchist that is a delegate where you can basically uh delegate your your PNK uh

and what you know is this delegate is going to vote according to futi signals so it's The good way basically to deal with one of the big problem in Dows that is voter apathy. Most of the time you know we we we you delegate your token to a specific delegate and the guy sometime doesn't vote or there are some problems.

Uh in this case you're sure that this delegate is going to vote uh for maximizing the price of the underlying token. So there are these three mains concrete learning we learned from the past basically and now if we look a bit more at the future where we are going and

what we want to do uh we launch uh recently a new platform that is close clearos foresight basically and it's a platform that is leveraging an ID from Vitalik that is the distilled human judgment concept uh so it's an idea from 2025 you can have a look in his article AI as a engine human as a steering

wheel. I don't have the time here to go too much into details. Uh but thanks to this platform you will be able to do uh this human judgment. Uh that's why Vitalik recently retweet one of our post introducing this uh platform. The things to keep in mind is this platform could be used for a lot of different use

cases. One of the use cases that you can leverage this platform for it's KPI based futarchy. If you remember from the beginning, you need a specific metric. The specific metric was yeah the token price. But when you think about it, when you are a DA for instance, you want to grow an ecosystem. In order to grow this

ecosystem, you want uh for instance, if you are a defi DA, you want to maximize the TVL uh that uh one specific project uh will achieve if you give him a grant. And that's perfectly what you need for for basically a prediction um sorry for for futarchy and for KPS KPI based futur. Uh

so basically you ask the question uh if this project get a grant what will be CVL and thanks to this platform we will be able to do things like this and if you stay tuned you will see some example uh coming from us in the future. So thank you for your attentions. Uh yeah, I I hope it's clear a bit more

about uh what is future key and how it can be used for your DA uh with like some concrete examples of what we can do now and also what we could do in the future. So, thank you all and if you have questions, let me know.
