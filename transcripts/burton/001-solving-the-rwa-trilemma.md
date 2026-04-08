---
title: "Solving The RWA Trilemma"
speaker: "Jonathan Han"
organization: "Euler Labs"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=rKh6D-JmfLM"
transcription: "youtube-auto-captions"
---

# Solving The RWA Trilemma
**Jonathan Han** (Euler Labs) --- Burton Stage

Hey, good morning everyone. >> Yeah, thanks for coming. Um hopefully everyone have a good morning. Um I just arrived yesterday from New York. Um I'm Jonathan, CEO at Oiler Labs. Um thanks for tuning in and uh today we're going to spend a little bit time talking about um how Oiler is helping um creating

utility to the RW markets but also solving a few bottlenecks uh from the technical implementation of a lot of RW assets as they enter onto the blockchain. Um, and uh, I think I'm going to give a little presentation um, for about 20 minutes, but I leave some time at the end for questions, but um,

feel free to ask questions at the end of each each slide. I want it to be a little bit more interactive instead of me just talking non-stop for uh, 20 minutes. Yeah. So, um, yeah. So, a little bit about myself. Uh, I'm Jonathan. Um, I joined crypto full-time in 2020. Um, initially was um,

oh, there's a lot of seats. Uh, feel free to jump in. Yeah, I joined crypto full-time uh, in 2020 to uh, in the venture capital world. Uh, I worked in traditional finance before that. I saw huge opportunities of the the convergence of DeFi and TRFI and uh, finally seeing that uh, convergence

really happening in the last couple years. it's really accelerating uh and working in DeFi boring lending space has been super rewarding and humbling at the same time uh kind of see that come to realization and I think this year is really going to be uh infliction year for a lending and um we've been talking

to all the asset issuers about some very exciting uh new assets that's coming on chain uh that allows user get access to a lot of different asset classes that they're not able to in the traditional way uh but DeFi is a huge unlock talk uh to really uh open access to users on a lot of different investment

opportunities uh and financial tools uh for them to really uh realize their financial goals uh leveraging all DeFi that can offer um and Oiler is definitely part of that. Um and uh assuming you guys already probably heard about oiler already but yeah on on the high level we are a borrow lending

primitives um being in the space since 2020 um and um we're yeah we're working uh we're working accelerating with uh institutions this year but has been working very diligently and actively with DeFi native users uh for the last four or five years. Um and uh to start

off um there are a couple of bottlenecks to allow uh auto assets to come on chain. Uh there are a few uh like these are the three main ones but there are many others. I can kind of dive into a few uh in the later slides. Um but some of the key ones are risk isolation um composibility and compliance. Most of

the lending options right now can do two um but not all three of them. So risk isolation means um there's no shared exposure across different vaults and markets. So if one vault get hacked uh or there's some incidents with the collaterals uh the risk is not uh contentious to other markets. Um this is

super relevant to because each other assets behaves behaves very independently sometimes uh especially the private credit markets. Each private credit is structured very uh independently and there is a lot of uh isoteric risk associated with each assets. So having the modular risk

isolation module really unlocks the safety and uh helps with scaling scaling acceleration of the adoption of RW assets to um to retails and institutions. Um composibility I think this is something you guys already are pretty familiar with. Um this allows capital efficiency, cross collater

collaterization and really allow RWA to be integrated with a broader DeFi ecosystem. Uh so if Fidelity issues a ETF on chain with through tokenization um and you wanted to move that effectively on chain um and through composibility um you can borrow against that assets within using various stable

coins and uh that means yeah that means really taps into the the full scope of DeFi and for compliance uh this is uh a unique requirement for RWA because a lot of these assets in different juris jurisdiction does require different compliance requirements. Um so for example uh we recently launched a

partnership with um securitize. Um a user can get uh actual ownership of the underlying assets um through their they call a digital security token DS token. uh but this does require uh a very specific set of KYC KYB gating and uh sanction screening regulatory permissioning uh and the elegant

solution that oiler has built is to allow that at the smart contract level instead of uh adding 10 different add-on tools uh just to um to to make it work right so we can really allow it in a very elegant fashion at the smart contract level so these are the three big categories I will probably spend a

little bit more time on um some of it is really unique to the RWA space. Um um this is related to um the risk isolation. Um as you guys know um in D5 borrow lending there are two popular modu uh architecture design. One is the shared pool architecture and other one is modular. So Orler is more on the

modular side. So on the shared uh pool architecture the advantage of that is very highly efficient. Um but if one of the market is compromised it means uh massive implementation to the entire protocol. Um uh at order we believe risk isolation is really key uh to protect users and also protect anybody that's

involved in the state uh in the ecosystem. So if one pull is impacted uh through the collateral or through smart contract hacks um it's not impacted to the to the broader ecosystem. So the damage is very much contained. Um this really this is really already very highly relevant to DeFi. As you guys

know there are a lot of uh very famous hacks uh throughout the years um that risk isolation is really key but with RWA introduced a new layer of complexity uh especially with a couple of uniqueness that RW asset has. One is for example the nav delays. Uh one example is um the Apollo private credit uh fund.

Uh so it's uh the Apollo private credit fund is very popular. It's being talked about very frequently with institutions al also retails as a key examples of how RWA assets can come on chain. How top tier uh institutions are thinking about crypto. Um but the challenges that come is uh a few things. One is the nav delay

meaning that how these assets are marked to market. Uh in D5 we're very used to uh autonomic settlements. Um things can just settle within seconds. Um but TRFI moves in a much slower pace. Um these private credit funds are settled um on T+1, T+ 3 or even longer meaning that if you purchase the fund uh it will settle

days later uh that to to confirm that you have the ownership of the fund. So this really creates a lot of issues on DeFi because we need to value the uh the the the real-time value of the the collaterals in real time so that we can issue loans based on the value of your collaterals. Um so and also uh with the

Apollo fund it has a redemption period of 3 months. uh meaning that if you miss a certain redemption period, if you wanted to withdraw and get out of your position, it can take up to three months, which is uh a huge problem in DeFi. So there are a lot of uh issues like that with unlocking autolay assets

onto DeFi and that we are solving, not just us, there are a couple other protocols that allows uh marketplaces where we can solve the nav delay issue. Um and some of the other product protocols are like uh thinking about creating market uh creating a free market for um for the settlements for

also uh the redemption period. Um so there are a few other projects that we're talking to um and also for liquidation as well uh to really solve different pieces to allow a defy similar experience uh with these limitations that we are dealing with on the audly assets especially on the fund side. Um

so this is just on the the shared pool. Um yeah I think uh I already touched on a lot of these uh but to uh in summary I think to allow what audibly really needs to allow a very smooth user experience we need isolated market uh because these assets does move very idiosyncratically.

We need to make sure uh user are protected at the vault level. Uh two is compliance informed uh enforced. So this mostly related to uh institutions cuz they wanted to be super compliant. Uh they wanted to make sure they feel comfortable enter into DeFi. So having compliance measurements and tools at the

smart contract level is very key to on board these institutions especially with RA because they already hold a lot of these assets uh so they can come on chain use collaterals and borrow against uh with stable coins and other blue chip assets. Um risk measurement by domain experts. This is what I mean by risk

curators. Uh this is widely adopted by Orler and Moro modular lending protocols like this. And um it doesn't make sense for um for somebody that's not very well in traditional finance risk measurement to run a DeFi vault risk um to risk parameters. So weer work with a few top tier risk curators in the space to set

risk parameters. This includes supply borrow caps, loan to value ratios uh and all these other uh risk parameters that orders allow um these managers to uh control the risk which I can expand a little bit beyond because you need a deep understanding of each RW assets and the risk associated with those assets to

protect the user. Right? So their role is to make sure um we're not lending out too much money um and but we're maximizing the capital efficiency in the vault. Uh four is um we uh we have to allow cross collateralization at a contained scale. So this is a uniqueness to oilers architecture. uh we don't just

do super isolated modular pools but we can customize is uh these modular pools to create multiple cross collar collateralization uh in a more safe and controlled way. Um the fifth one is permissionless deployment. So we're still defy we're open access so people can uh list assets

um in a still in a permissionless manner. Um I don't think it makes sense to submit a government's proposal for people be like, "Oh, hey, should we open a market on the Fidelity uh three-year Treasury versus the Franklin Templeton 10 years treasury." So this will create a lot of delay um and create a lot of

like unnecessary process uh for users to decide uh especially retail users who are not like tracking these on a day-to-day basis. So we will have a permissionless deployment working closely with curators to open these markets as we think as we see market demands and uh risk assessments.

Uh any questions so far? Yeah. >> Question. >> Yeah. >> So you addressed a lot of the issues. >> Hi. Uh you addressed a lot of the issues and you had a point with regards to NAV delay. So uh you talked a lot about

price discovery and how you uh see that but like whenever we're talking about RWAs and we want to bring uh uh DeFi native experience to the RWAs like would you uh expand on the uh NAV delay thing like how do you address that so that it is reduced?

>> Yeah. Yeah. Yeah. So >> sorry if it's a previous point but >> no yeah this is actually a key point um cuz a lot of people are so I work in traditional finance but whenever I talk to people who hasn't worked on traditional finance they're a little bit confused about how these private bonds

and private credits are uh priced in real time. So for example a lot of these private credits funds they issue loans to small businesses. Um right now a lot of it is issue to AI companies to build data centers and to fund these RWA uh R&D efforts right so uh small and midsize enterprises they are most of the

the borrowers in these private credit funds and the issuers of these private credit funds they aggregate these loans together and issue a fund and sell it to interested um uh investors at a higher interest rate than the treasury that you can market. So the the delay on the valuation of these funds meaning that

the healthiness of these small to midsize businesses are not a public traded right. So their initial performance is not uh is not super liquid. So there's a lot of delay in information in terms of how healthy are these private credits are doing. So sometimes if you discover something

that's drastic, these private credit funds can get discounted significantly. So the value of your collateral if you use tokenized version of those private credit on chain can get slashed like 30 40%. If they get downgraded by some credit uh risk uh rating agencies. Um so that's what we call the uh the nav delay

and also the sentiments. Meaning that if all of a sudden um the rating got downgraded um we will face a lot of um utilization pressure on the borrow uh on the on the lending market because the value of the collater suddenly dropped and we're reaching a high utilization ratio uh on the lending

vault right so it creates a lot of uh stress that way. Yeah. Uh so so there are we're thinking about ways to kind of smooth the curve and also getting ahead of the game. But yeah, this is a this is a top hot topic right now about uh onboarding uh private credit to lending markets. Yeah. So

>> uh I have a question into the similar direction. I mean what you're talking about the NAV delay, it's true for all markets on the weekend. So how do you deal with like you can't liquidate 20 billion worth of gold over the weekend? Like it's it's it's it's an issue for for every asset that's not

traded 24/7, right? >> Yeah. So the liquidation is uh one of the key discussion topics that's why the modular lending uh design work makes sense right so because each assets uh to liquidate uh in a graceful manner you need uh you need to work with uh large liquidity pools of organic trading

volumes of these assets so that when liquidation happens um you um the the collaterals can be offloaded in a more uh graceful way meaning that there's not huge discounts when we're trying to uh when the liquidation partner try to sell these assets to offload them, right? Um and with the liquidity nature of these

private credit funds, uh sometimes these can be u user cannot uh offload these assets in definitely not seconds, sometimes with hours or even days of delay. Right? So to open these markets we have to make sure so at from the lending protocol side we have to make sure there are liquidity partners that

has uh they can liquidate uh at a certain uh volume on a daily on a daily basis right so this is the active conversation we're having with the curator with the liquidation partner to make sure we can offload these assets if we cannot we usually tend to delay the the market launches. Yeah. So

yeah, this is just to give you guys a sense like we're solving a lot of the new problems that's coming onto DeFi because this is not what we're used to. We used to open like Bitcoin ease markets and these can be settled in seconds but with these financial instruments they move at a different

speed with different measures that but to really fully unleash unleash their potential I think there are a lot of innovation that's currently happening. Yeah. Uh I think I already talked about a lot of these. Yeah. This this is give you guys some example of the recent uh partnership we have with securitize uh

with a couple of uh credit private credit and treasury bond assets. We're also discussing with them on the tokenized equity uh to tokenized stock index uh products. Uh so with securitizer can actually uh get the direct ownership of underlying assets through their

tokenization strategies. Um but if you guys look at other tokenization platform like centrifuge like uh they use sometimes use different legal rappers um you get different legal uh ownerships of the assets. Uh with securitize you do get the direct ownerships but that means uh more severe um u regulatory gating

KYC KYB um and a lot of lending markets cannot allow that right now. We're one of the few that's able to implement a lot of these uh capabilities on the left hand side uh through at the smart contract level. Um um this is a point on the cross collaterization. So we do isolate the

risk at the vault level but from the users perspective on the your users's account level we do allow uh cross collaterization. This is oiler's uh unique advantages on capital efficiency does come in play. So if you do hold tokenized equities, you do hold tokenized treasuries or bonds um you can

borrow USDC against a portfolio of your assets and these we have the smart smart routing of different assets at different pools but we do connect them through the Ethereum vault connector. Uh we have a white paper on that happy to share with you guys later on how that works. Basically, we route these assets to

different isolated pools. But from the users's experience perspective, um you can borrow USDC with your portfolio without try without trying to do this uh manually through 10 different different markets. So this is where the cross collateralization can work. Um this is a little bit a little bit about the

curation model. I think a lot of people are not super familiar with this point. Uh you you guys can think about curator as your asset manager. So in Trafi um you can think about like JP Morgan or um Franklin Templeton or um uh or Apollo they are they they are sort of the trady risk creator and some of them are

actually coming on to DeFi. Apollo just announced they're being active risk creator on D5 as well. So they are managing the risk of these vaults. Uh so we are the infrastructure builder. We provide the bike uh we provide the the behind the wall behind the wall piping. um uh on these vaults, but the one

that's actually setting risk parameters on each assets that does a lot of diligence on how risky a certain collateral is are conducted by these uh creators. And us at Oiler, we wanted to make sure the risk curators that we partner with really understand how DeFi works, how traditional finance works and

they set the right risk control measurements so that the user's interests are protected at all time. So um some of the risk creators that's active on Oiler are um uh on the bottom right hand side uh Santo, KPK, uh Concrete, K3 and a few others. I'm actively talking to um a few others

including Apollo, Bitwise and you guys will see more traditional institutional grade uh risk curators coming on chain because they really see their expertise from traditional finance can translate into DeFi and they're getting themsel educated on how DeFi can work and we're helping with that education process and

with more higher higher quality risk manager and curators onto the space I think this will really unlock a a lot of the the new audibly assets coming on chain uh with people who actually understand them and set the right um set the right guide rail so user feel safer uh that way. So in the future um user

can freely select which risk curator they trust and deploy their assets just with uh at the curator level. So we will have a few options for user at each assets each RWA and user can select oh I trust Apollo or I trust Centura because they really do a lot of dig diligence on these markets. They have a good track

record never have any incidents. So user have full uh freedom on select which uh risk creator they trust with their money. Yeah. Uh another uh another example I wanted to show you is another type of RWA that's coming on chain that is tokenized equity. Uh this is very exciting because

um especially um with uh user outside of the USA, they sometimes wanted to get exposure to UX stocks and once they get the UX stocks exposure, they wanted to um borrow against them. Um so that's what we've been talking to a lot of institutions and retails on this point. So we launched with Ono Finance uh on

the S&P 500 index, NASDAQ and Tesla. uh we're on boarding more individual stocks and indices that can expand beyond US stock market that can go to um Japanese stock market, European stock market and uh Hong Kong, right? So there are a couple of other options that we're um unlocking and bringing them on chain.

This is another example of how we can open up access to user across the world um to allow them to get exposure to different different financial instruments and borrow against them through the lending protocol design. Yeah. Yeah. And uh I do wanted to kind of show

you how this can work. So to allow tokenized equities on chain a few partners has to involved here. So uh at the bottom uh row you can see on finance they tokenized the stock put the legal wrapper on top uh with the NAV uh tracking uh framework as well. Then chain link help us with the risk oracle.

Um currently these tokenized stock markets are 245. Uh we're working with chlink to unlock 247 as well. We're doing a lot of testing on the weekend trading uh because the the data is a little bit thinner on the weekends because try does close, crypto doesn't. Uh so this is another key

differentiation uh with the stock market. Um that's different from the bonds. Uh Santo is currently being selected as the risk curator uh to uh to run these the risk um management of the vault on the day-to-day basis and Oiler provides the underlying isolated vault infrastructure.

Uh so what does it enables right so um so defy boring lending really ena enables um a few of key categories of uh assets to coming on chain we used to only be dealing with ERC20 tokens uh now we can deal with tokenized treasury that can includes cash and cash equivalent treasury bonds uh you uh stable coins

tokenized equities u and private credit uh but also while we are bringing all these different asset classes is on chain. Uh we build it in a per we can build it in a permission or permissionless way. Permission mostly for institutions. Uh and also to allow permissionless deployment meaning that

we keep the platform open. Any asset issuers can list their assets with us and uh it just has to be uh approved and um uh and go through the diligence process with our risk creators. Yeah. And you guys probably already know like RW assets is growing super fast and we're super excited about our

opportunities here. So, uh, yeah. Do you want to leave some time for questions? Yeah. >> Thanks a lot for the talk. Very, very instructive. Um, what other asset classes do you see going on chain after credit lending? in um tokenized equities.

>> Yeah. Uh we're talking about uh so tokenized equity is a big category. We're doing a ton of diligence uh on tok on private credit. There are a lot of issues that I already talk about. Um right now with the microeconomic environment, we are being extremely careful with private credits uh because

these assets can get uh downgraded um as the as you guys keep following the the news, right? Um but we are allowing shorter duration like um like daily settlements uh bond structure. So these are marktomarket on way more highly frequent level. So that's way more DeFi friendly for us to unlock next. Another

type of asset class we're thinking about is commodities. Uh this can include gold um precious metals to start with but other type of commodities as well. Um but I think we're going to start with some precious metals first because the we um there are already a lot of tokenized gold on DeFi on crypto and

we're unlocking that part of first uh but we we are constantly talking uh we're constantly monitoring other type of assets. Yeah, working with major uh tokenization platforms like Centrifuge Ono and all those folks. Yeah. So yeah. Hey, thanks um thanks for a great talk. Uh I just wanted also to ask you what's

your view and how you going to be uh handling the extended liquidity fragmentation because on Trefy the liquidity is fragmented and here we add another layer of fragmentation with different uh uh tokenization issuers and uh that kind of creates another set of you know complexity.

>> Yeah. So this is the this is the unique uh design of order that that can unlock right. So if we can isolate the risk by meaning like if we wanted to open the private credit markets we don't want it to connect with other vaults that we have cuz it's it's permission or we think it's too high risk we can do that

but for example the tokenized equity market um you can hold multiple different types of token tokenized equity like the indexes or the Tesla stocks we're on boarding a lot of individual stocks and you can have a portfolio of these to stock uh assets, but you if you just want to borrow for

USDC or PYUSD, um the it's highly capital efficient that way. Like we allow accepting multiple assets from the same categories um to to kind of uh allow users to borrow the same type of stable coins that way. So multiassets collateral is currently live on oiler. uh we're

thinking about working with some large institutions on uh on other capital efficient designs uh to to allow users to tap into that. Yeah. So >> I mean different organizers like you know for example on the Xbox >> Yeah. So that's currently under discussion because we're thinking about

uh launching X stocks as well like uh that you mentioned. Um once the market is live, we will talk with both of them be like hey if you're if the underlying stock is the same like can we make it more capital efficient. So this is this there has to be a a coordination between the the the price oracle provider and

also the risk curators right we have the tools to connect these markets together but we do want to make sure uh the underlying standards are the same the price fee speed are the same so there's no like discrepancies across different markets. Yeah. So >> like two-part question with regards to

scaling. So uh you mentioned the ono uh solution and their wrapper the RC20s and so that you don't get the underlying asset. Do you do you see those kind of uh structures as not really quick in terms of scaling and the second part is uh with regards to new categories is there a way or like any vision uh for

the real estate or commercial real estate uh solutions that can be done? >> Uh what's your second question? the real estate. So is there a possibility of like tokenized real estate to like bringing Git on chain or if something can >> Yeah. Yeah. I think we've actually been

talking about real estates for a very long time. Um these these assets actually face a lot of the same limitations with uh tokenized bonds. Sometimes even worse because uh the marktom market is very slow. Um and um some we are talking about like we're talking to some REITs uh issuers because

they have more um kind of markettomarket data on a daily basis uh from traditional finance. One of the highlight I do want to mention is figure markets. I'm not sure if you're familiar. Uh they issue a heliloc loan. Basically, if you are real estate owners, they issue a loan to you and

they have a co um kind of credit facilities to aggregate these loans together and um use them as a a credit facility and a private credit kind of structure that we're actually talking to Figure Markets. They are just publicly listed in the US and they've been building uh kind of real estate flavored

loans on crypto natively for many years. I'm very happy to work with them. Actually, I'm talking to one of the on stage at the other summit tomorrow. So, if you guys are going like definitely uh tune in, but I can share the high level afterwards on Oilers's Twitter. Yeah. So, yeah.

>> Okay. Um, hi, great talk by the way. I just met a couple a couple of things, but anyways, my question is sort of related to his question about liquid liquidity fragmentation, right? Um I'm curious how the settlement works if you have to like move borrowed values value across chains. So I don't know if

that's something you can talk about. >> Yeah. >> Yeah. So a lot of the liquidity currently is on Ethereum main chain. uh we are working with a couple of um uh L2s and um layer zeros uh protocols like that to make sure crosschain uh capital efficiency is being solved. Uh actually

there's a lot of encouraging conversation with layer zero right now especially with their their announcements with the zero chain. uh we're designing some custom solutions leveraging their crosschain solutions but right now a lot of the liquidities is on Ethereum main chain uh we launched

um the tokenized equity and and a few other like markets currently on the main chain but yeah we're in active discussion with a lot of L2s because they they do want to on board a lot of RA but they are still a little bit early I would say those conversations and initially I do think there are some

level of uh liquidity fragmentation um But I think Ethereum will always be I think a huge liquidity hub for us and yeah actively talking to u kind of interoperability protocols to solve that. Yeah. So yeah uh hi Jonathan thank you very much for

your presentation. Uh I got a question about the potential systemic risk uh of bringing onchain instruments. uh I mean traditional onchain credit instrument onchain uh we've seen that with uh the issue with resolve of having a hard hardcoded oracle on the on the protocols

>> and uh my question would be about the fact that we could have potential risk in borrowing I mean allowing people to borrow against illquid assets >> because onchain uh traditional credit instrument out onchain don't have marktomarket price and they are basically

hardcoded with uh redemption oracle I don't know the time frame on which the the update is made but uh couldn't we have any systemic risk about this matter given also we don't have any secondary liquid markets to for protocols to liquidate those assets so it could incur bad depth at the protocol level Yeah. So

a good good question. I think um the current solution is we're actively looking working closely with risk creator to access how we can gracefully liquidate or how can we gracefully have um frequent marktomarket data on these assets. Uh working with some other protocols like 3F uh if you heard about

them um who who is actively solving a lot of the issues that you're talking about. So I would say the approach right now is if you if we don't feel like that we have enough liquidities with our liquidation partner to offload these assets in volumes we would delay the market launches for now until like we

have other tools to have a active marketplaces to on board multiple uh market makers and hedge funds who actively organically trade these assets that can offload them in a in a free market way. Right. So right now, yeah, there's a lot of limitation like like you mentioned, especially with some of

these longer duration private credit bonds. Uh right now we are delaying them. We're talking to a lot of these bonds that's already tokenized. They wanted to launch with us. Um but we feel like to protect users interest um we have to yeah we have to kind of delay the launch for a lot of these. Um but

yeah, definitely stay tuned. We are focusing a little bit on the shorter duration uh markets that have less of those issues that you talked about. Um but we're also working very actively with other protocols. So hopefully we can have a country solution very soon. Uh also micro microeconomic environments

hopefully improve a little bit too. Yeah. So all right I think we're at time but yeah thanks for your question. Yeah and uh I will be around this area so if you have other questions just come find me. All right. Thank you. Yeah.
