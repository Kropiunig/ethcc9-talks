---
title: "Spritz — Building a Truly Decentralized"
speaker: "Kevin Jones"
organization: "BuidlGuidl / Edge & Node"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=XprZCC9lnhc"
transcription: "youtube-auto-captions"
---

# Spritz — Building a Truly Decentralized
**Kevin Jones** (BuidlGuidl / Edge & Node) --- Burton Stage

Hello everybody. Thank you so much for coming. Uh my name is Kevin Jones. I am the co-founder of Spritz. I'm also working in the graph ecosystem. Uh and I've been working in the Ethereum space for about seven years and very excited to talk to you guys a little bit about a project that I've been working on uh

called Spritz. So this talk is is titled building a decentralized censorship resistant and permissionless communication app on Ethereum. And uh so what is Spritz? Well spritz is exactly that. It's the first decentralized truly decentralized video

and messaging application built on Ethereum uh with using Ethereum as u the identity first approach of being able to communicate um in a censorship resistant way. So our mission is to restore communications as a fundamental human right by building censorship resistant

decentralized infrastructure that enables anyone or anywhere to communicate privately and directly without centralized servers, surveillance or gatekeepers. Um funny thing is that Spritz was actually born out of an actual problem of

censorship. Um it started actually with my wife trying to contact her mother in Russia. My wife is Russian. Um and one of the issues that she had is that pretty much any application that she tried would either completely cut off obviously after um in the in the past couple years. And so it was definitely

an issue for her to be able to communicate freely. Additionally, uh recently I was in Abu Dhabi for a conference Salana Breakpoint. Don't judge. Uh I was there uh and uh we were uh trying to FaceTime with my family and I just could not and I come to believe that in uh well in all the surrounding

area of United Arab Emirates you basically cannot use um video video conferencing services. Then I tried getting on my VPN and I found out that my VPN was actually blocked as well. Um, so this censorship issue is definitely something that I think if you're not in a place where you experience it or you

don't travel, you're not really aware um that it is is a serious problem. And so again, Spritz was built out of that concept. Um, so the team is me uh in Eugenia. Um, previously I've worked at EngineX. Again, I'm working in the graph ecosystem uh at Edge and Node. I am um experienced with infrastructure and uh

yeah, that's enough about me. So what is the problem? So uh the problem is that there's an estimated uh 29% of the global population. So almost 2.3 billion people that live in countries where essentially VOIPE is restricted or censored in some way. It's a lot of people. Um on top of that uh a lot of

enterprises have uh limited options for communication platforms especially decentralized communication. uh there are some things like XM XMTP and logos messaging which I'll talk about which actually spritz is built on which help with that but there is not a platform that makes it easy for enterprises to

adopt these decentralized solutions uh they have to kind of build it from scratch so what we aim to do and I'll focus on the individual side is switch chat is this decentralized messaging platform for video and for um uh messaging on built on athereum first um conversations are encrypted end to end

with uh your um wallet essentially and um you're using your wallet as an identity. So um this also helps you integrate things like uh using uh spritz to do financial transactions inside of the chat as well. Uh and we'll get to that in a little bit. So the key components how it's built uh

essentially we're using Logos messaging for all of the messaging features. So you can do uh peer-to-peer messaging. You can create private group chats. You can also do more public group chats uh on the on logos. Uh for people that don't know Logos, Logos is a messaging, decentralized me messaging uh system

that uses this concept of like light nodes and routing. So uh Spritz Chat itself, when you load Spritz chat, it is a light node on the Logos network. And so you're instantly connected on your device to and you're routing your transactions in a private way. Uh we're also using obviously web3

authentication. So we support signin with ethereum and sign in with salana. Um and so in this method you know you do own your identity, you own the login uh and all the code is open source. We also have x42 enabled in uh some context. So you can also uh link your calendar to uh spritz and the the benefit there is you

can essentially use it similar to like kalanly for like setting up meetings. Um, and you can do paid meetings through uh via x42, which is a really cool feature. Um, and we also support video conferencing and audio conferencing uh through decentralized WebRTC as well. So when you connect uh and you want to

connect to another user, another Ethereum user, uh you we're routing that that traffic again through a decentralized network called Huddle01. Uh so yeah you a user can come in uh sign sign in with their wallet ENS uh or SNS sign in with Ethereum sign in with Salana. Uh they can also use something

like alien ID or world ID. So we have that direct integration so you can log in and connect. Um and this is interesting because it opens up a use case where maybe in the future we can do um some kind of like proof of human so that you know that you're chatting with someone uh that it hasn't you know it's

not a it's not a bot essentially. We also support email login for people that don't necessarily uh know how to use web 3, but they want to talk to their son that is an Ethereum maxi. Uh they can just log in with email and we'll create a account for them. Uh one of the coolest things I think about spritz is

we also support pass keys. We're using what's called web offn which is a special package that lets you sign with a pass key uh and create an Ethereum account just by using your face ID or uh whatever mechanism that your phone supports for uh pass keys. Then uh users can send messages, make calls, um join

chat channels, do live streaming as well. We support live streaming um uh which is a really cool feature uh using live pier. So we have a direct integration with live pier. So you can stream similar you would do with like Instagram or Facebook live or something like that. You can add friends. Uh we

also have this cool little thing called pixel art which is fun. You can make these little pixel arts and send them in chat. Uh just a fun little thing. And uh we also have a lot of other features for chat that differentiate us because we're using blockchain native kind of concepts. Uh we have built-in web3

wallets, built-in vaults. Uh social wallets is you often hear at Vital Vitalic talk about social wallets. We bring that to the table. Um, we also support AI features that are coming soon. It's currently in beta, but essentially like for ETH Denver, we had a Buffy the Buffacorn AI agent that was

sitting inside of a group chat that was hosted on a decentralized network where people could query and talk to it in a decentralized way, which is super cool. And uh, we also support uh, again scheduled sessions. So, similar to like Calendarly, you can essentially use Spritz as this kind of like all-in-one

communication tool. Um, the native AI chat features. Again, this is like uh just a screenshot from the ETH Denver community chat. You can see here you can just literally just tag an AI agent inside of the chat. Uh, we're going to be opening this up probably eventually uh soon. We're just

trying to figure out exactly what the model looks like for supporting the LM inference. But essentially, you'll be able to create your own AI agent uh put it into a chat room and train it uh on, you know, people chatting in your community and like basically gathering that stuff. Uh, one of the integrations

we're looking at is maybe using Bonfires. If you guys have heard of Bonfires, um, which is basically a product out of DI World. Uh, we're we're eventually hoping to to integrate that. Uh, so you can basically do some kind of AI agent stuff inside of chat rooms. Uh, this is probably the coolest feature I

again that I think is is we have uh Spritz smart wallets which are powered by safe. Um, and the cool thing is again you can sign with a pass key. So if you sign in with a EOA or a pass key, we can create a Spritz wallet for you uh inside of uh the chat application. Uh and then we have the built-in account

abstraction. So we sponsor all of the gas on layer 2s that we support. Um we also are using uh the graph's token API for all of the data that we're using inside of that. So we support pretty much all the networks that the graph's token API supports. And then we also have the vaults which

again uh Vitalic often talks about this concept of like being able to have a multi-IG with friends and family. Uh we do support that as well. So you can come in here, you can create a social vault. Uh you can literally just tag your friends that are in there. So you can tag an ENS name, you could tag a spritz

username, uh you can put in an Ethereum address, and you can build a multi-IG and deploy it all through the UI. And again that is also sponsored uh gas on all layer 2s as well. Uh we also just recently added uh ENS subnames. So now if you have a let's say you bring up app.s spritz.hat you create

a pass key you claim a username uh it's going to create an Ethereum wallet for you uh under the hood and then you're just going to need to come in here put in your username and you'll instantly have an ENS name subname. So you would have like you know my name.spritz.eth teeth. Um, and uh, you can again just

claim it through the the normal flow and then you get this kind of like resolver and you can save that. So, thank you so much. I appreciate I I didn't want to take up too much time. I know we're we're running over, but I'm definitely uh open to answer any questions about the platform uh that you

might have. Any questions? Thank you. Thank you so much. Want someone back there? Yep. Oh, there's a mic. >> Yeah, I'll have a strong voice. Uh, well, I'm just curious about where you came from with the name Spritz because I like it and also obviously the the the

the protocol in general. It's really nice and it's really useful nowadays. Thank you. >> Yeah. Yeah. The name was uh it's it's it's silly, but it's like appperal spritzes. Like it's kind of a fun little summer feeling thing. And like we were literally just like talking like me and

my uh wife and she's like, "Oh, like spritz is kind of a fun name." And it's fun to say, you know, it's like a good it's hard to find a good name for a product actually. Okay. And spritz just kind of runs rolls up the tongue is very rememberable. Uh and who doesn't like appear spritzes every comment. Um yeah

and I appreciate the comment. Thank you. >> I have also >> I have also question. >> Uhhuh. >> I >> I see that one of your USPS is actually the chat the video chat. So you had to still build the whole infrastructure for

wallet and all this onboarding stuff on it because that's the internet of the future, right? web three. So we solve do it did it exactly the same. But my question to you is are you also like your chat features and your video features can it also work as a DAP so that I could integrate it via API in our

wallet and our users get the features because we solving like many people solve the same problem but they have enough different USB on top and yours is clearly the video voice chat. >> Yeah, that's a really good question. So uh we are we do have an SDK uh it's very lightweight right now and it's directly

used for like messaging um but we do want to support video and audio soon through it. Um so we'll probably we are basically going to do a v2 of spritz. Uh it will be a slight revamp to make it even more like kind of social uh sorry censorship resistant and pass like the walk away test. try to be following this

whole crops guideline for that Ethereum is focused on and one of those things will be yes a fully kind of decentralized SDK that supports all of the protocol um so until that happens probably in the next six months or so that will be come to a reality so very and we would love to chat with you so

for sure awesome I think maybe one more question if we have if anyone has one no awesome thank you so much for coming guys appreciate you
