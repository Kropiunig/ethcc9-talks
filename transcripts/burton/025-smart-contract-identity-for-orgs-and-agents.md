---
title: "Smart contract identity for orgs and agents"
speaker: "Nischal Sharma"
organization: "Enscribe"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=-L5zE16FFvk"
transcription: "youtube-auto-captions"
---

# Smart contract identity for orgs and agents
**Nischal Sharma** (Enscribe) --- Burton Stage

Hello. Uh hey everyone. So I am Nishel, co-founder of Inscribe and today I will demo what we build with the Inscribe and what we are releasing next. So we started inscribe with the problem what we all face that's the hex address in the ethereum UI right we all scale like even if it's a new user or an exper

experienced web3 user we all see this hex addresses everywhere and we are when we are interacting with smart contract we fear them like how many of you have this fear like I do yeah quite a lot right so uh people do name their wallets but smart contract naming is less than 2% % which is like very very very low.

So what uh solutions we have right now people go to blockchain explorers or set the nickname for the contracts but these solutions are centralized right. What if every wallet every contract can have a name which through which you can you know trust the domain via the ENS. So let's suppose you are interacting with

the registar on ENS and you see this name v10.registar register.eth then you can instantly you know trust this because it belongs to ensi safely interact with it. So we uh had this contract naming season with enso and we distributed over 4.5k of ENS token to the developers and

protocols to you know spread awareness and even start an initiative and adoption of smart contract naming. So it is still going on. you can go to inscribe and name some contracts. So uh during this time of smart contract naming season we uh understood like naming is not enough like we need to

have some metadata attached to the names so we can understand more about the contract. So right now when I'm a user right and I try to find audits or even like you know which this content belongs to it's really hard for me it's like fragmented over the website scattered over the website and GitHub what if you

have all this data on chain at a single platform and even like at wallets or blockchain explorers. So you can see okay this contract belongs to uh inscribe and these are the socials avatar what are the technical details like category the license dogs do dogs and you can also have security audits

directly there. So I think this will make all our lives very easy and people will you know start um interacting with smart contracts freely and we also have APIs so you can directly integrate into your product. Okay. So, uh the naming ENS naming and metadata can be hierarchical just like a

mirror to DNS. So, what you can do is you can import your DNS on ENS like here we have web3 project.org and we can import it and we can set a hierarchal at different levels like 2LDD, 3LD and 4 LD. Let's suppose we start with 2LD and you can have your project or brand information. Then you can branch out in

three LDS for your products or services like different um app wallet categories and you can set those metadata in this and then at the sub levels you can also do onchain versioning which vital was talking about in devcon right like you can have okay there's a v1 app then the v2 version two and you can also attach

the release artifacts and audits directly into this. So uh projects are embracing this onchain identity and these are some of the projects we are working with. uh some has already announced and some are in progress but currently the challenge still is a

lot of users are using um ENS just for individual identity right and orgs and teams are not fully utilizing the ENS the full capabilities of ENS to have a protocol identity like you won't see many organization which are you know storing all their information on ENS on onchain

So we uh developed this next evolution of nscribe where these orgs and team can easily manage their onchain identity and which is also accessible to your agents and visible to your users. So some of the features uh like shared workspace for your manage for managing names then you can track all your activity then you

have batched operations multi multisig support then ability to add org contract and even agent metadata then you have API and CLI access for agents and lastly we are also introducing smart account and smart session support. So I'll just go to the uh demo.

So this is a current uh app where you can name all your contracts easily. Just need to uh paste your address and you can create a new name. It will create a subname or you can use an existing one and you can choose L2 chains and just name your contract. Also if you want to bash name your contract that is

also possible. You can upload the CSV with all the contracts and names and you can batch name your contract and then if you want to deploy new contract with a name that is also possible in a single transaction. So this was our uh current version of enscribe and here also if you want to find the smart contract metadata

or even want to see the heral view of contract. So this is the smart contact man I I was showing before. Here this is the primary name and you can find socials of project avatar and then technical details and also uh the contact AI source um sourceify. Yeah uh this this is basically via sourcify.

Then you have contract. Okay this is too fast. Okay let's uh go uh uh this is the the hierarchical view where you can see you know the text records are set at different level. like some of the brand assets are here and others are at different level and you can see it uh easily. Okay. So this is our uh the new

uh UI which we are going to release uh very soon and here you can create new orgs. So okay so I will just try to I have uh recorded this. So I'm trying to create a new org maybe ECC demo and you can u add your members here directly invite them

and to set up the orc you have like five steps. So first uh we are we will be releasing on mainet soon and the second step is selecting an LD. So I have many uh but yeah I will be selecting ECC demo here. You can also import your DNS on the ENS via this. Then you have manager mode. Uh so

basically there are three managers mode like first is safe multisig where we will sign and you will also sign and then um we can make the transactions. The second is inscribe where uh all the transactions are gasless and we are also about to bring uh inscribe smart sessions. So you don't

need to sign anything. it is also going to be a gasless thing. So uh okay so once we have this organization set up you need to give a manager access of your 2LD. This is not the ownership of your 2LD it's just a [clears throat] manager access. So we can create

subnames under your org. So once this is done you don't you can even um like uh unplug your wallet because after this we don't need wallet all things is going to be gasless and everything will be controlled by the enscribe which is also safe. Okay. So now I have already set up a

organization which I will show here. So if you see uh I have some wallets and contracts already preloaded and I can also add I'm also going to add a new uh address here. So I have like many uh yeah demo addresses. Okay. So it detects contract automatically. And once we have this uh

this is the name management view where you can see all your name space like this is ecc and there's a new subname wallets and we have a w1 and I'm going to create a new subname directly and if you see uh I'm not signing anything it's as easy like just uh you know editing a um you can say a

cv and here I can also add metadata directly So suppose like uh this subname is for contracts and you can stage your changes and al similarly uh there's a contract one under the contracts and I'm just setting a address.

So once uh all the changes are staged we can review the changes like what are the changes here. So right now I'm creating two subnames and these are the record changes. And after this I just need to confirm and execute. Okay. Just give me a second.

Yeah. Once we hit the execute, you can see uh the pending transactions and completed transactions. uh which are um in the background. And here you can also manage your organization. If you want to add more members or you want to revoke access to from someone, you can do from here.

And then uh you can change the manager access from inscribe contract to other uh inscribe contract to other manager access like safe and else. And this is the API keys. So this is very useful if you want if you have AI agents like you can create an API key uh let's say I'm I think yeah inscribe

agent and you can set the expiry and what are the scope you want like if you want to give a subname creation and not record editing records you can do that and okay so what I will be doing is yeah this is the details of your contract of your uh organization.

So okay. So what I'm doing here is you just need three environment variables like the inscribe API key, the uh org ID and then the URL. Once you have this, this is a demo AI agent which I'm showing. So it's basically you can have more complex AI agents

built for you. But here uh this is the environ environment variable file with three environments and this is the skill file which you need to install in your AI agent. Once this is done uh like this this is a demo uh this is demo stuff but yeah you can have some complex uh you know AI agents which can directly read

your um website or whenever you have a new contract deployed it can you know create a subname. So what here I'm doing is create a subname conto uh in cipoleia. So it will directly use the skill and uh create a new subname. So let it complete. Uh yeah. So if you see uh it was created

successfully and this is the transaction hash for it. And if you realize right u there's no signing of transactions and yeah you can see it's done. Okay. Uh let's okay so u this product is still in beta and what we are doing currently is you know uh asking teams and projects to

join an early access where you can uh collaborate with us and join us um and you can basically you know provide some feedback. Uh so to all the teams who want to establish a full full onchain identity uh simplify their naming operations and even manage their org metadata or embrace agents for naming

operations and be the be among the first uh teams to ma on mainet with full onchain identity. Do join us scan the QR code it will uh it will bring the inscribe website and you can apply for an early access. So uh thank you. That's all from my side. If you have any questions

just uh >> yeah thank you. So I wanted to ask how do you deal with proof of identity in these cases? Let's imagine I want to register the new name Binance and it wasn't taken before. what stops me as an attacker to like what is there any KYB in place or something which actually

would make this thing semi-entralized or fully centralized because essentially DNA DNS and proof of web identity is centralized and I'm interested in how you bridge it to make it decentralized in this case. >> Yeah. Uh it's a nice question. So we already have like DNS on ENS. So how it

works is uh if you have like maybe unis swap or binance.org right? Uh so via DNS sec you can establish a link to your ENS name or basically you can say okay I have binance.8 and you can also link it to the binance.org or you can even use binance.org as an ENS name right because you own binance.org right and via DNS

you are proving it. So it's like uh that that's how uh the proving of identity works in this case. Yeah. >> Okay. We can maybe yeah take it afterwards. Thank you.
