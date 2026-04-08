---
title: "Programmable Native Bitcoin for Everyday Finance"
speaker: "Fisher Yu"
organization: "Babylon"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=WS8dtdLpcF0"
transcription: "youtube-auto-captions"
---

# Programmable Native Bitcoin for Everyday Finance
**Fisher Yu** (Babylon) --- Burton Stage

Okay. >> Okay. Testing, testing. Uh hello everyone. Um yeah, my name is Fisher. I'm the co-founder of a project called Bobilong. And today uh my topic is uh bring native Bitcoin collector to Ethereum. Okay. Uh very quick question. Is there any Bitcoin hater here? No.

Okay. Good. Then then then we are friends then I'm safe. Okay. So yeah so Bob so Babylon is a bitcoin project and this is our first time entering the ethereum space. So yeah we are very curious to know more uh everyone here. So because we are new so a very quick overview of us. So yeah our project was

founded in year 2022 by professor David Shay from Stanford University and myself. Yeah, both of us are from academia and we are uh recent backed by A6Z, Paradigm, Polychain, uh Easy Labs, all the famous VC you can uh name it. And our current team size is 40. We are fully remote team with 25 nationalities.

And our mission is to make Bitcoin productive in a trustless way. And we are most famous for our trustless bitcoin staking protocol which to date has activated over $10 billion worth of native bitcoin. Yeah. And all the major exchanges and some very prudent international funds are the yeah uh

stakers of our uh protocol. But today I'm not going to talk about bitcoin staking. I'm going to talk about a new protocol we are working on. So I will start. So the opinion here is the the argument here is collateral is the foundation of finance and my argument is bitcoin it's a pristine um collateral.

So what we are working on is to bring native programmable bitcoin as a collector for the ethereum ecosystem. Okay. So start from the first one collector it's the foundation of finance why think about borrowing okay borrowing lending you collect rights uh digital

asset as a secure to borrow money in terms of like option trades per trades you collect rightes some asset to have covered calls or covered put options and then in the insurance industry uh insurance company collect premium okay and but they cannot deploy all the premium for yield. They have to reserve

say at least 50% of the cash they collected as a reserve to be just in case of the uh incident payment. So the reserve asset there it's unusable or they can only be used to buy like treasury bond short-term treasury bond. So very low capital efficiency. So the reserve part of insurance is actually

also can be viewed as a collateral. So collateral is the foundation of finance. Now next I'm going to convince you why Bitcoin is the perfect collateral. So here I have some I have a uh qualitative uh graph here. X-axis is the risk level of the deployment strategy. Yaxis is the yield. Yeah. So we're talking about the

yield to return ratio here. Okay. We first look at stable coin. Stable coin the almost zero risk uh return is roughly like 3 4%. Uh because of the US treasury bond and then uh yeah as you take more risks the yield goes higher. And then when we look at ETH ETH staking it's the almost zero risk option. So

it's uh return it's roughly 2%. Then yeah as you go uh become more aggressive you have higher yield. What about Bitcoin? Bitcoin the safest uh option is Babalon's Bitcoin staking which is roughly like half percent to 1%. much lower compared to the others and also

you can see its trajectory it's lower which means for the same level of risk you take the yield you can generate using a bitcoin it's actually lower why this is because like compared to stable coin okay stable coin has better riskreward ratio because of deeper liquidity on chain and also you have

more use cases right because stable coin it's a currency so any financial applications can use stable coin but bitcoin is not the case indeed only 1% of the bitcoin it's currently used onchain defy 99% offchain so most of the bitcoins are sitting

there idle and counting on appreciation of its price okay so bitcoin is not a productive asset which means it's actually the best collateral for example for insurance case instead of using cash as the reserve. If you can swap it with Bitcoin as the reserve, then the insurance company can have the 100% of

the premium be productive and deployed for yield instead of only 50%. Okay. So, so our uh the goal of Babylon is to bring Bitcoin which is a store of value digital gold idol asset as the collector asset for the Ethereum uh onchain finance ecosystem to unlock the liquidity of all the other assets.

Yeah. So basically for Bitcoin holders the best strategy for them is to collect bitcoin to acquire stable coin and then deploy stable coin for yield. Okay. Not seeking direct Bitcoin yield, low uh high risk, low return. And for DeFi applications, accept Bitcoin as collateral will expand its uh customer

reach. And for um applications such as in insurance that I mentioned, swapping cash reserve with Bitcoin reserve will unlock a lot of liquidity and productivity for the cash res for cash part. Okay. So, Bitcoin collaterized for onchain finance. It's what we do. But there's a challenge.

The problem is called wrapping. Bitcoin chain is not to complete. It is not programmable. So, in order to use Bitcoin on Ethereum chain, there's no like zero knowledge or like client based uh trustless bridge. Okay. So for almost all the solutions you actually have to give your native bitcoin to a rapper or

yeah basically a multisig rapper and they print you a red bitcoin such as WBTC CBTC okay the problem here yeah it's obvious you have counterparty risk if it's not trustless you're basically trusting a multi- gift card issuer is a gift card issuer which is not So yeah, because of this counterparty

risk, the Bitcoin collateral will be at danger. So here I list a few questions which uh constitute a bitcoin collateral risk assessment framework. So I'll yeah quickly go through uh the the the questions you can ask to evaluate the risk associated with the Bitcoin collateral solution from the both the

Bitcoin holder side and also the onchain applica uh DeFi application side. Okay. So we start with uh things that Bitcoin holders care about. First is assured access to to the app. So the the last thing Bitcoin holders want to see is that after they deploy the Bitcoin and the D5 app say no I don't recognize you

I didn't receive it then the Bitcoin got wasted. Okay. Then the next one Bitcoin holders care about is no loss of title to their Bitcoin because in many jurisdictions if you lose your title of Bitcoin by giving it to someone else it triggers capital getting tax and also there will be some uh complex um

compliance and accounting issue as well. Okay. Then also there are some uh questions that both Bitcoin holder and financial finance service providers care about. The most important one is called permissioned disposition which means yeah you have a collateral to be used in a financial service and uh at the end of

the uh term uh the system needs to decide whether the collateral is returned to the bitcoin holder or it's liquidated or seized by a liquidator. Right? So this process this final disposition process should be permissionless. There shouldn't be someone in the middle can press a button

say hey I changed my mind no liquidation no settlement okay so permission disposition is the most important thing that both Bitcoin holder and the financial apps care about then the next one which is closely related is that the disposition rules should be clear and enforceable right it shouldn't be uh

yeah someone changed their mind so hey uh yeah I changed the LTV overnight so that you can not be liquidated. Right? And the next one is unauthorized transfer and rehabilitation. This will make sure the collateral is correctly pledged to serve the precise purpose of that financial service. There's no

hidden reuse of the collateral for some of something else. Right? Okay. Cool. Then there are also some things that uh bitcoin holders don't care about but the financial applications care about. The first one is to make sure each and every single position like the borrowing position is backed by one native bitcoin

right and then also uh for of the bitcoin locked on the bitcoin chain. So basically yeah smart contract uh can program how bitcoin will be collectored and uh disposed at the end. So the the idea behind it is that we use cryptographic translations to translate

the smart contract decisions into something that the bitcoin chain can understand and execute to achieve the full programmability. So it's based on our research from both boblin labs Stanford and Berkeley. Yeah. So that bitcoin locked become programmable collateral for the smart contract. And

yeah, I know that one is very technical. So this is the takeaway. Now with the uh bitcoin collateral vault solution, collaterizing native bitcoin becomes as safe and trustless as collaterizing is no difference. Okay. So yeah, this summer we are going to launch the mainet of our trusted BTC

vote protocol alongside with its first application which is native bitcoinbacked borrowing brought to you by a and yeah and we are also exploring bitcoin yield marketplace uh with the workflow being borrow uh assets using bitcoin and deploy to yield strategy. We are also incubating more use cases of

native Bitcoin collector in option and insurance credit card etc and etc. Yeah, many use cases of native be coin collector. Um yeah that's all. Thank you very much. Do we have time for question or no? No no. Okay.
