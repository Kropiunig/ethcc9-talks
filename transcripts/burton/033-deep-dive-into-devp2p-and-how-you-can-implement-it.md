---
title: "Deep dive into Devp2p and how you can implement it"
speaker: "Lola Rigaut-Luczak"
organization: "Placeholder Network"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=y-hn004TkHs"
transcription: "youtube-auto-captions"
---

# Deep dive into Devp2p and how you can implement it
**Lola Rigaut-Luczak** (Placeholder Network) --- Burton Stage

Is it working? Yes. Okay. Hello everyone. Good morning. I hope you're feeling well. And uh well, welcome to this workshop about deferto. Okay. Who is familiar with def peer-to-peer already? All right. One person, two. Okay. Nice. So maybe you're not going to learn new

things, but I hope you are going to enjoy the next session. Uh first uh let me tell you who I am. Let me introduce myself. I'm Lola Goligac. I'm a software engineer. Uh I have been for the last 10 years. I've discovered Bitcoin in Italian back in 2013. I was studying cryptographic at

uni and someone started to talk about crypto. I was like nice. What is this? Is it about cryptography? and it was about Bitcoin and Ethereum and I've since been kind of obsessed with the topic and every topic around uh peer-to-peer technology and protocols. So things like Bit Torrent, Zeronet,

Bitcoin, obviously the original cash peerto-peer, uh, dev peer-to-peer, letoer. Also, you might have noticed I'm French. I'm really sorry for the accent. I'm sorry to mispronounce. Uh, and I really thank you to be here to this morning.

All right, let's start. So this workshop will be in two parts. First part we are going to see theoretically uh peer-to-peer in Ethereum and the second part is going to be a workshop. So unfortunately sorry is not going to be exactly how to implement this but don't worry I still have something for you

guys but we are going to do something a little bit together and we are going to try to figure out what can we build with what we just learned. So you will need to contribute. All right. So, first part peer-to-peer and Ethereum. Okay. Little survey. Um, how does

peerto-peer uh how does Ethereum not talk between them? When you think you hear the correct answer, please raise your hand. There is several answer and there might be several correct answer. First answer using TCP. Okay. Two, three, four. Someone is not sure.

Oh, al also please we are a small group so if you have question uh please raise your hand during the presentation we can make it dynamically it's more fun like this I think. All right. Second answer. Using JSON RPC. Nobody's raising their hand. Okay. Okay. Uh using def peertopeer.

Okay. Almost everyone using lip ptopia. [laughter] Someone is not sure. uh and well the correct answer are actually a C and D. So yeah all of you you didn't fall for the for the wrong answer which was designer PC.

All right so I've already talked twice about def peerto-peer but what the hell is dev peerto-peer? Dev peerto-peer is a set of uh italion ptopia protocol but only used for the execution clients. So it was uh introduced uh by uh in Ethereum at the beginning right uh and it allow you for it allow like to do

different things uh like finding other nodes syncing blocks uh it's also allowing like clients at least that's something that Ethereum is trying to do is still trying to do uh sharing uh state snapshots uh also access to the mele transaction

So you know when you have a new transaction nodes talk to them they share it between them and then it's added into the blockchain. Uh also get transaction receipt receiving being the result of this transaction on what is being added to the blockchain. Uh is it uh successful or not do you have some

logs. So that kind of information that you can get through the dev peer-to-peer uh protocol. Also some of them are encrypted and this is kind of important. All right. So what are those protocols? So I took all the protocols that you can find in the documentation. You might

have some more but I don't think there is. Uh first one will be the RLPs the transport protocol. This one must be supported by all nodes and they use RLP uh encoding. Is everyone familiar with RLP? It's it's a kind of a encoding for data for it. So you have a specific field and

then you make it into bytes so you can send it over the network. Uh second protocol actually there is two is this v5 this v4 and this v5 it's used for the peer discovery. So it's used to discover new pier right you connect it to a node and you might find more node to connect to so you can have a bigger network.

Um it's yeah so this protocol use can like DHT to store information about the node. It's something that we can find actually in bittorrant. So when you want to find the file in bittor you will share ash on using this algorithmia and you will find information about p who actually has this file and you can

connect to it. So we use something similar. It's I'm not sure how we can justify to have this because well in Ethereum blockchain everyone have the same data right but I would be interesting to know if any of you knows about this someone who is not entirely agreeing

and uh yeah something interesting also uh when you discover new peer you actually don't know about which network they are from and by that I mean they might be mennet they might be test net but They might also be like other network entirely. As you know lots of project have fork bitcoin uh fork

ethereum sorry and they they are also using this peer-to-peer uh discovery protocol and so you might have like base polygon uh binance. So you are not sure that the node you are going to have is the one that you want to connect to. It's part of your network. Right? All right. Uh other protocol which is

not really a protocol. It's an open format. So when you it's called enrum note record [clears throat] sorry. So when you have uh when you have requested a pier you will have a message on the format of the node record which will give you information about the node like it's

public key uh IPv4 address TCP and UDP port and IPvC v6 address. So everything that you need to connect to it then after and it's also RLP encoded. Okay, last one uh which is a DNS disk for DNS peer like to discover new DNS new peers using DNS because when you

have when you start a node this node is not aware of any pair right but you still need something somewhere to start with so we are coded DNS but because it's easier then to update to read from the DNS record and to update a list of p than to do a new release of the client every time you want to restart or add

new starting peers, right? So, this is pretty useful. Okay, so we are going to take talk now about the main uh protocol that we want to understand which is ALPX the transport protocol. So, I'm going to read the description from the documentation.

ALP transport protocol a TCP based transport protocol is used in communication among nodes. Okay. Now that's why we add TCP because it's TCP based. Uh this protocol uh carries encrypted message. All right. So we will have encryption starting with this and uh it

can belongs to one or more capabilities. So capabilities is going to be a term that we are going to see a lot in the next in this presentation in the next slide. Uh it's basically sub protocol. All right. So then using this transport protocol you need to negotiate which protocol your node is talking and what

is the other node you are trying to connect to is talking. So it's not easy to find a match, right? Because let's say I speak French, you speak Spanish, we don't have any language in common. I cannot talk with you, right? I cannot exchange with you. It's going to be really difficult. It's kind of the same

idea uh with capabilities. You need to have the same one. And uh LLP is named after the LP seration format because most of the message are LMP encoded and the name is not an acronym for anything. Okay. So what kind of message can you send using aerial pics? You have four

message. Uh first message is the hello message which is the most important one. You are going to uh exchange it automatically with all the peers and they are going to give you information about which version of LPX they are using the node ID but also those capabilities. Right? This is why this is

the first step. Uh second message. Okay. uh small thing I have added uh zero is because every message the first bite of the message that you are going to receive is going to describe describe what kind of message it is. So if you see zero, it's going to be to be a hello message. If you see one, it's going to

be a disconnect message. All good. Okay, that's noting. All good. Um, so okay, disconnect message. Really important message because you are going to see it a lot of time. P are going to disconnect from you and you are going to disconnect for P. So for different reason, you actually don't share any

capabilities. So you cannot process to do anything more anything else. Might be also you are not on the same network. So the PI is going to disconnect because obviously you are no use to it. Uh could be also that you send a message which is wrongly encoded. So it say okay I don't understand what what you're

talking about. I'm going to disconnect from you. Could be also because they already have too many peers. So they go say sorry dude there is too many peers that are talking to me. I'm going to let you go. Uh so a lot of reason for disconnect. Two last message uh ping and pong. It's basically message to uh see

if you are still alive. So quite often node is going to send you a ping. You will need to answer a pong. If you don't, what else is going to happen? Disconnect. Thank you. You are following. Thank you. Uh okay, I've put a link to the documentation where you can find all of

this and even more. It's on the GitHub Ethereum Desperto repo. And there is a way more than than this slide and that I'll just say about so yeah go and take a look. All right capabilities I'll talk about capabilities. I mentioned already that there are sub protocol right. So every

capabilities every sub protocol is designed for a specific feature functionality. Could be light client could be snapshots could be exchanging blocks and you can even create your own. uh they all have version is kind of important because it will also enter into the phase where you negotiate

between capabilities. you have a capability and it version if you don't have the same version well same disconnect um and yeah some u some uh capabilities actually depend on other to work so you will need to have the both of them okay example of capabilities that we can find

first one is ETH is used for exchanging uh blocks new transaction and network info this is the most important one uh second one is less It used to be also in all the clients is for the light client Ethereum unfortunately now it's being deprecated so it's being removed you can only find it in the oldest node.

Uh next one is snap is to facilitate the exchange of state snapshot between node and this is an example of a capability that require another one because this one require ETH and last one is an example of uh a company or foundation I mean parity created their own uh capability that

they're implementing in their own client. Uh it was also an attempt to do an Ethereum light client and but now I think it's also deprecated and they have removed removed it. All right. Uh so those four also you can find in the documentation right and uh yeah I was um I was saying that

we are going to talk about ETH which stand for ATM wire protocol which is the most important one because this is the one that you're going to use if you want to sync uh with so get blocks transaction and everything with other node. Uh the current version of this protocol is ETH69.

So in in um during its live on mainet we have seen like nine different version of this protocol and something important is clients are not I mean clients by admin nodes they are not going to support all of them right most of them support the

last one or the two or three last one uh which means that oldest node cannot talk to the newest one that kind of makes sense because lots of things have changed in the last 10 years but yes and the version before were like during development so we don't really care okay so ETH uh what kind of message can

you send over the network right and what kind of information can you actually gather you you will have like kind of like two two kind of of things that you can do first you you can request for information uh you you will like see that the request to request an information you

have prefix gate. So when you send a message which is get block headers, you will have an answer which is block headers. Okay. So when you want to have some information you send this and you will have the response right after. You will also have like sometime have messages that you didn't ask for or

subscribe for is because the network is relaying the new information on the network and is trying to give you information that he thinks you don't have. So example uh new block new pull transaction new block ash transaction and there is one last message which is kind of particular uh this one is

status. So first thing that you do when you connect and over the this ETH sub protocol is that you are going to exchange the status and you have it has really really important information into it which is a network ID. All right we will see why it's really important. Uh again, I've put the link

if you want to learn more about this and what kind of formats those messages are. Um okay. All right. Let's see an example uh a use case. Uh let's say we have Alice. She has a node and she want to sync block, right? Where is Bob? if you want to connect to block to Bob to get the

blocks and uh first thing TCP connection obviously uh second thing is going to be an end check. So I mentioned that messages are encrypted. So you are going to send what we call a message and they are going you are going to received a response which

is called act message. is give you all the information you need to then start the encryption for the following protocols and it's not okay I'm going to share my opinion on this it's not really useful because all the message uh are blockchain blockchain is public we all

know what the message are like all the information are but yes it's a good standard but yeah he has it does add complexity because then after that all the message you are going to encrypt them and decrypt them so he had complexity to the clients. I see someone who is agreeing with me.

All right. So, I'm not the only one to share this opinion. Uh also like fun fact in comparison, Bitcoin doesn't have uh encryption in the message. All right. Uh second step is the RLP uh it's part of the RLP protocol. So I mentioned you need to negotiate uh the capability. So you need to send the

hello message and you are going to receive the hello message to be sure that you have uh you can talk the same language right the protocol um so here I don't know it's maybe too small you can see you can see like the version client ID you also have like clients what kind of client they have uh capabilities port

and things like this [clears throat] all right next uh then it's Yeah, then you we are part in the ETH capability to protocol. So you need to send the status and you need to have the status in rebones and why this is really important because you

have the network ID. So it might you might have done all of this and actually have to disconnect which is making like discovering new peer that are actually useful to you a bit more complex and taking a long time. I think it's not optimal and maybe there is other way to do I would be interesting in your

opinion about that. Uh but also something really interesting that is new in ETH69 that's why I put new uh is that you have the field earliest and last test. Do you guys know it why why they added that >> checkpoint? No, not really.

>> S. >> Yeah. Yeah, exactly. [laughter] Uh I will tell you more about about this after. Uh so yeah and then uh last test ash the last test block that you have received. All right and then only then you can start syncing. So you are going to start

by requesting the block and in answer B is going to tell you give you the blocks. All right. So you when you request for block headers you can start at any block. Uh also you can batch and this is really interesting I think. uh maximum being 1,024.

Uh but that's already a lot because in one exchange you can have 1,024 blocks header information, right? Uh you can also go either uh from uh the last test to the earliest or reverse which is pretty neat actually this one I think. All right. And the answer you we got the header but we are still missing

information right we don't have the complete block we only have the header. So we are missing information like transaction withdraws and uh everything that you can find in block bodies. You also used to find something called uncles uncle's block but since we have uh moved to post it's not there anymore

right uncle blocks were part of the proof of work protocol [snorts] all right and then you keep doing those so beginning it's a bit a lot of effort I would say but then you can keep doing those and you can sing pretty fast right and this is the end of the example so so far so good all All right, thank you.

Okay, so I mentioned this earliest and lastest field which are new fields that app appeared after the PE spectra upgrade really sorry. Uh and it's really important because so it's called EIP 4*4 which is a bond historical data in exeution client. I'm going to read the description. Clients must stop serving

historical eders body and received alter than one year on the P2P layer. Clients may locally prune this historical data. That means that clients are not going to have the old blockchain. The kind of the concept of blockchain and be able to reproduce a step from the start to the end is going to disappear because since

we've moved to post, we actually don't need all this data, right? You can create consensus on the layer using post without having access to historical data. So it's good. I understand the motivation because it's taking a lot of this space. Uh so you usually need 1 TB SSD can be a bit expensive if you want

to run it run your node locally like at your house or something like this but I think that's kind of sad because that mean that you are going to lose all those data and uh a call to action to maybe start uh archiving those data right let's take it early all right so I'm done talking almost uh

we are going to have a small uh workshop session. So unfortunately unfortunately we are not going to do the implementation. It will be long even if I already do it and we don't have tables. This is not kind of practical but what we can do is that we can uh get together and think

about what can we build now that we have learned all of that. Maybe you have some idea of application that you can do. But uh if you're interesting in how to implement FP2 LP in Rust, I have a workshop uh project on GitHub you can scan. It already has like basic function like to create messages like hello

status with the pair encoding. Uh each branch is a step of the slide that we have seen with the diagram and uh the final br the final branch is the full project and uh yeah so yeah I haven't updated so it doesn't support ETH69 it's only 68 and 67 but I will do it in the next

days. All right time for you to work. We have three minutes. I don't know what time is it. Sorry. We have 10 minutes left. >> Oh, we have 10 minutes left. Okay. So, if you want to take maybe two minutes to find proposition of what you want to

build on deftopia or maybe you you already have some ideas. Okay, we have someone with an idea like you you can get them. Oh, question. So I'm just curious what is the the minimal state that a node needs to implement or the minimal amount of commands that it needs to implement to

be accepted by by other nodes in there. So if you would for example want to monitor the me pool or block blocks without running an actual node and don't use that overhead to verify everything because you don't care. >> Yeah. Yeah. So good question. The minimal unit is the aerial pics. So

those four message hello disconnect ping pong you you won't get then anything for the mele for example then you will need to have the ETH but then you can ignore all the message right or you don't need to do request you can just get confessing to for the message with the meool

>> I read that nodes kick you out if you don't provide them sorry >> um I I read that nodes are kicking you out if you don't provide them if data so for example if they asking about block headers etc and you just don't respond respond or just say I don't have that. They will kick you out and disconnect

your peer connection. So you lose kind of an inside and peers quite fast. >> Yeah. So that's something I actually haven't uh monitoized yet. Um like look at really deeply. Uh but some clients want it depends I guess on the client but also like let's say you you start to index a node you don't have any block

right? So if you say they don't have any block they cannot request anything for you and that would be unfair for them to kick you if you are just a n starting there is no way to know if you are a bad node or a good node at this point but you have an idea then you you mentioned mele do you have an idea

>> yeah I just recently built an an MVV bot to to do backgrounding etc and currently it's not profitable I'm still off by a few cents to win some bits but there I was curious how or where do I get the mepool information and all the transactions out without running an actual full node because as a as mebot I

don't care about if a block is valid or not. I just want to get the the transactions in a me pool and try to figure out something to make a profit. >> Okay. Yeah, that's a that's a good thing. Uh anyone else want to share something? >> All right.

>> Uh yeah, you mentioned um Par made their own subprotocol, their own capability. is this uh if you meet nodes and you tell them, hey, I have capability XYZ, and they've never heard of it, they're not going to kick you for that. So, you can just have uh you can create a a sub protocol and have just uh you and a

bunch of friends use it in their client >> and that works. >> Yeah. Yeah. Yeah. Exactly. They don't care if you have if you have like sub protocol that they don't know about. So, you can create your own, propose your own for your own use case, convince other client to add it or just write

your own client. Now that you know about this now there is way more like to do when you build a client right I'm kidding very stuff uh maybe that will be another talk [gasps] all right okay we are going uh another >> one

>> if you if you were to rebuild the protocol um what would you keep what would you take out >> and why >> yeah that's a good question uh so I will change a peer discovery to add network ID so you don't have peer that are not useful to you. I would remove the

encryption actually just so you can get things faster. That's that's a choice. Uh and maybe I would make it compatible with to because here you have information about your IP address and IP address already give you a lot of

information. I think this is more dangerous than knowing what kind of message you exchange. And it was a plan, right? I remember I read the blog article about the having the encryption and moving toward to but then never done it. But it was an idea back in 2013.

All right. Okay. So I I do have some application that I've built that I want to share with you. Those those are all like uh just for fun, right? Uh you can contribute. it was just to see like what can we do and are we going to be kicked out of the network. So first uh things that I wanted to

build when I learned all of that is a node to index blockchain because data I think data are interesting. Uh so it also allow you to fetch directly like blocks from the network. You don't need to deploy a node and it save you space right also no general RPC. So I've done project for indexing where we had to use

vision PC and I hate it. So this is also hate has been a big motivation for me to learn about FP2. Uh so yeah no need to deploy a node and wait for it to sync right you just start and uh save space and it's fast. It's fast no but you can batch do batch call right.

uh you you there is a link to the GitHub repo uh it's called prototype ETH prototype uh don't have a good name if you have a proposition for name or if you want to also run it uh it's working so I'm able to like u I tried hoodie like to uh sync udi node and put everything in the in the

database and create index and everything in postgress took me like uh one morning to do that uh yeah so if you're a RS developer fun stuff right sorry I'm checking time I have two minutes left I think uh you can map the network we talked about disk before this V5 uh

and you can get a bunch of information also if you have ETH protocol so what kind of uh data do you get you get uh pup key client what kind of client they use like get rest or things like this are they synced uh which network ID they're on. Uh that's a bit something I'm obsessed with

network ID. You will see why after uh fork ID and uh their IP address. So then you can analyze those data and see okay they are where are they based in the world and uh it's low in resources because if you remove EVM if you remove the database you don't need a beefy server

to run this. It's really cheap and you can deploy a bunch of them. Actually, I have a bunch of them already on the network. Eight. [laughter] And same uh link to the project. Uh also if you have a better name and if you if you want to run this and uh do the metric yourself, you're welcome to

uh yeah so I wanted to share like some of the findings that I have. So I've been running this for a year. Uh here what the Postgress uh table looks like. if you query things. So you have the IP, you have the ports, you have the network ID, uh the clients, here is bore, uh and I've also added the what kind of

capabilities we have, right? So you can start to do data analysis on this and a little bit more of like numbers, metrics. So how many node I've contacted? Uh almost 25,000, right? So there's lot of them on the network. And here uh here's the number on nodes associated to the network idea. So you

will see that Ethereum is one. It's not the first one. You you have like more node for 137 which I don't know what it is. Someone knows >> it's Ethereum test network >> which >> one the first one >> yeah I think sepoleia is this one

actually >> it's polygon okay it's polygon uh 56 is actually benance so we have a lot of nodes but please note that uh because it's really difficult to map the network it also uh depends on the time because nodes go up and disappear. This might not be right. Right. This change a lot.

But it I only have like almost 2,000 nodes. But it might also have happened that I was not able to connect some not. Right. They might have disconnected from me. But this is this is this gives you a little bit of an idea. All right. Meool. [laughter] So you can get all the information for

the ramp pool and same you get rid of the database EVM everything that you don't want and you can get the new transaction and connect to a lot of nodes. So you want so you can try to be the first one to get the information low in resources. It's really cheap to deploy nodes because they are like skin

from everything that you don't need and yeah easy to deploy and it's actually a small service that I have started with my friend Morat who is here uh that does that it's called puddle network it's free to use please send us an email contact us also if you want to help and contribute and same you can contact us

it's a fun project that we have done and yeah so Last uh idea that I have things that I want to do is that building is fun but breaking things also is fun. Uh there is something called uh an Eclipse attack that you can do on Ethereum. I mean theoretically you can deploy enough node to isolate one node

and we have seen that I've mentioned several time already that uh they are low resources node when you only keep the peer-to-peer stuff. So you could theoretically deploy a bunch of them and be an So if it's something that interest you like to try in practical maybe not to attack the Ethereum network

but let's try on a test net please contact me and uh yeah there is more peer-to-peer uh at the beginning of the presentation I mentioned um I mentioned lip peer-to-peer which is actually used in the consensus layer that's something that I have not yet uh been studying

deeply like doing a deep dive like I've done for this, but that's something that will be interesting to do. Uh, what I have I have a bit of beef though with lip peer-to-peer. I'm not the only developers. People kind of hate it. I've used it for other project and I also kind of hate it. Uh, it's really

bloated, difficult to use, but maybe there is things that you can do that we can do like to improve it consensus layer P2P protocols. And that's all. Thank you. All right. Do you guys have some more question? Otherwise, we are good. All good. Well, thank you.
