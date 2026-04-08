---
title: "New AI Workflows in Remix - from Concept to DApp"
speaker: "Stéphane Tetsing"
organization: "Remix Labs"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=yqSjY9VznQc"
transcription: "youtube-auto-captions"
---

# New AI Workflows in Remix - from Concept to DApp
**Stéphane Tetsing** (Remix Labs) --- Burton Stage

Hello everyone. >> Yeah, good afternoon. Uh I am Stefan Tessing from the Remix team. We are based in Germany and pretty much uh everywhere in in the world. And today we will be talking about new AI uh workflows in the Remix uh IDE. As uh I guess most of you know what is the remix

IDE the remix environment it's the browser based IDE that you can actually use for deploying in a very quick manner smart contract and do further stuff without having to install anything on your desktop machine. So with AI uh with significant progress made in the AI environment lately, we are having deep

integration that actually let you do quite a lot in in the web three environment. Even without specific knowledge, you can actually achieve a lot of stuff. So the goal of this talk will be to have uh an interactive uh way of doing stuff together. So you are pretty much free to ask question at any

time. We will be running some live demo on stuff that are actually live right now on the IDE. And then from there on we will be also having a at a less uh at the end of the uh of this workshop a live demo of something. I actually grabbed yesterday because yesterday I was attending another meeting here uh a

a team from Switzerland also based here in France. They were talking about a philanthropic platform for helping children maybe in Cambodia or pretty much everywhere in the world. And they were having some issues for raising funds and so on. And then I taught myself, okay, I can just set up

those stuff very quickly in order to show them this is actually what you can also do in order to show your shareholders without having any deep technical knowledge. So with that being said uh let us start by going through the overview. So uh we are now uh releasing the remix version two with the

release of the version two. We have significant uh we have significantly improved some stuff that we will go through and then I will go uh over the AI workflow what we have um integrated so far and then we will have an interactive live demo where we will go through the philanthropic example that I

just stated some some while ago and I will give some outlook what is actually to be expected over the coming month or years from our site. So let us start with uh first explaining a little bit vibe coding. I'm pretty sure you are all

talented in coding and understanding coding and maybe some of you might not be understanding coding and so on. Actually VIP coding is a nice thing and nice thing also have a a dark side. I mean with VIP coding you can pretty much uh create the app that you have ever wanted to uh to create but

there there might be some security risks behind it and also the fact that you might not be understanding exactly the techni u the technical stuff that are that were created from the AI and so on. So with that being said, V coding is good for pretty much everyone. Not without any deep review, good for

production code. It is good for you to kind of create a proof of concept. So okay, the idea that I currently have right now is something that I can turn uh I can turn it into a technical proof of concept. Yeah. And the good side of VIP coding is that you are interacting with uh a machine in term of natural

language. You are using plain English or you you can also use a voice in order to uh interact with the AI to create yeah edge cutting uh applications and so forth. And I said it is not suitable for production environment unless you made significant review go through security

and order uh architectural review. And the good side is that it is personalized. I mean back then if you want to change something inside your code, you will have to kind of uh uh contact a a programmer or you will have to contact someone with the required expertise to go through your uh your

code and do the change and so on. Now you can do it in a lapse of time and that's actually useful and this is what actually tries us to kind of integrate that inside remix because the remix IDE we combined with the complexity of the web3 environment is not that very much understandable for everyone and sometime

you don't want to bother with all the security all the different mechanism that involve web three development you just want to know if something is achievable if I can actually do it and then just use plain English or plain German, plain French and then explain to the AI

what you want to have and then go from there on to see if that can be manageable. So what is new in Remix AI version two? In version one, we already had some AI integration. And if you recall, one year or two years from now, we were having AI chat BS kind of arising pretty much from

everywhere. And those AI chatboard were not very much aware of the platform where they are actually uh where they actually operating your game. Of course them where technologies like retrieval augmented system where you go into a database get some data and try to extend the prompt from the AI but you have no

way of knowing exactly what is going on on the platform. What has the user done and this was it was pretty much okay just explain me what this stuff is doing and then I will manage the rest. Now the the AI has a much more deeper integration that the AI understand exactly what did you click last time,

what did you did, what did you do before and what are the foreseeable next step that can be that can be engaged and these are stuff that are enabled with the MCP integration and the assistant. assistants now understand pretty much your uh the entire environment in which you are living or what you are actually

doing and we now also have a front-end builder which is actually a deep a deal breaker. We have seen a a lot of services out there um a lot of services out there proposing uh AI generated uh AI generated websites and so on. Now what we are doing we are bringing the combination of uh automatic

contract gener I mean AI generated contract combined with a front end with a a website which actually communicate with the contract that has been generated in the background with one single prompt which is actually really nice and we have done also some revamping of the deploy and run for

those who have already been on the remix IDE And we are also introducing cloud storage. So you will you won't fear missing any files anymore. Everything is backed up if you wish. So talking about MCP integration which is actually really nice to uh to state here is that we have two

types of uh of MCP integration layers. We have internal ones which are pretty much legacy one and internal ones which are developed by us not by any third platform and those one are actually living in a browser which are understanding uh pretty much everything inside the uh

inside the remix IDE environment going from contract deployment going from what file the user is actually being editing going uh also covering What are the next steps or what is the user intent? What is the user wanting to actually perform right now? How can we help the AI understanding what the user is doing so

that we can give we can retrieve the best value out of the AI to propose to the to the user. Yeah. And we also have external uh MCP uh MCP server. And actually they there's a a big challenge. I mean from the browser perspective you cannot just host a MCP a MCP server uh and so on. So you will have to uh you

will have to create another backend in order to uh host it somewhere and go it from there and then and then uh have access to that MCP. So MCP is not something that is just given out by the uh I would say manufacturer or the guy or the company that actually provide the MCP. It's just a piece of code that you

will have to host by yourself somewhere and then have access to to those specific uh to those specific feature. And this is what we are actually providing for uh major base uh I mean major big pro big uh protocol either protocol or project in the web3 environment such as alchemi openane

uh hrscan all the other stuff those are external uh MCP project which are not developed by us but which are actually contributing a lot into smart contract development interaction with the uh web3 uh platform. form and and so on. And upcoming we will be enabling the user to also host his own MCP host his own MCP

uh server as we already do with Olar. I mean we have a integration that where you can go full uh offline still use uh AI to achieve some workflow and we plan to uh carry out this analogy to uh to MCP where you can actually host your own MCP server either on the cloud or locally in order to achieve specific

task if you are technically versatile. So we have already touched a little bit uh the points of MCP resources in the sense that now the platform is pretty much aware about what the user does. The platform being aware about what the user does doesn't mean that we as remix know what is the user is doing. This is just

piece of code in order to help the AI. Okay, this uh this is most probably what the user is actually doing. This is just some probabilistic model in order to say okay this is this might be interesting for the user if you say I want to compile a specific project or a specific contract there's no way that we as uh

remix we know what you as user but probabilist um in a a probabilistical manner the word compile is already matching with the feature that we are providing and therefore compiling will be at the top of the list of actions that the AI might choose to propose to you. And this is the type of resources

that we are providing to the AI in order to uh to provide much a seems integration. I mean quite good value to to the user. Are there any question until now? Feel free to ask any question if you have any. Now let's jump a little bit into the

remix AI assistant. What is actually being what has actually been implemented? Uh on the left hand side you have some convers some conversation starter and those conversation starter are actually good for someone who actually doesn't know what he wants to do. It's like a really nice kickoff

into doing stuff. You can here you can press on alchemi or the graph to have some example prompt that you can actually use in order to query some stuff. I mean for the graph example you can query okay what was the last transaction above maybe to Ethereum and so on. These are information that of

course you can navigate ether scan. You can go pretty much into two or three web pages until they get there until you get the the answer. But here you actually have uh you actually have that in a very simplistic manner. And right now we have a set of model we are supporting mist trial open AI and also

the the frontier coding expert um from uh entropic I mean the haiku and also the uh the sonet model and for now they are they are free for now for our beta user as we will also see later there's also this mistral medium which is also free of use nothing is chargeable right now And we have also

the history uh yeah the history as in any traditional chart environment. Uh actually this is the place where we actually jump into some live demo. I hope you can clearly see what is going on. Yeah,

as I was explaining some while ago, as you load the Remix IDE, it looks like this. You have the chatting environment. On your right hand side, you have your conversation starters and the conversation starter actually help you kind of starting any type of conversation that you will

that you would like to have. you will see the what the uh remix is able to do. If you are not pretty much sure about what you are actually wanting to engage, you can just click okay. What can I do? What are the MCP functionality? Here's a summary. You can write solidity contract. You have fire management. You

have deployment in interaction. And let us pick up some example from this remix AI workflow. We I have written a very simple workflow prompt that you can use onetoone in the IDE in order to deploy a contract and interact with a contract

without even having to take a look into a code. And we can do that together. So I will start this by starting a fresh session, a fresh chat session and then I will just copy I will just copy this which is ah okay I will just type it create a new ballot contract in

a in a new way. So what I will be expecting here is the AI to come in back to the IDE and then create a new file because we have a file system abstraction and we have a little bit of security. I mean that's the stuff with AI. We we we should always have security for writing files. If you don't

want that AI write any file into your workspace, you just deny. But in this case, we want to accept pretty much everything what the AI is proposing to us. And now we are seeing we are seeing a a a file has been created. Create a new contract. Oh, sorry. I did. Yeah.

>> Oh, >> yeah. Yeah. Yeah. And now I can't see anything. A ballot can track a maintain. You can also be sarcastic to with the AI. And now he's processing in the

background. It seems like there was an issue with the code formatting the ballot contract. Well, this is a showcase issue. Let us repeat the process in new in a new file. What is actually happening is that we have a set of tools

also in cooperation with uh open tippellin. I know every time a tool is being executed the tool name is being written over there and I know by experience that that tool is a tool from top from open seline since openelline are actually providing secure contract and the

contract will be based on the open seline uh libraries but it doesn't mean that the contract is safe. So that's something to be taken with a little bit of caution. As you can see here, we have a new ballot contract. Oh, maybe there was a little bit of

collision because in the workspace that I already have right now there was a there was already a ballot contract. But the point is we have a new ballot contract here. You can review it. You can do pretty much everything you want with it. But I don't want to take a look to the code. I just want to say compile

that contract and then you will have some feedback from the AI saying that the comp that the contract has been compiled and so on. I will say just deploy it on the VM. So, Remix is having in a browser a virtual a virtual machine chain for very very quick deployment. Of course, you

can also hook this uh to Sepia as we will see in shortly in the example later. Okay, I see what is going on. The Ber contract requires constructor argument. Please provide those constructor argument. I don't know about constrictor argument. I will just say make

some arguments up. >> Uh pardon me. >> I copy paste the error message. >> Oh the error message. Oh yeah. Uh but in this case you will rather get an error message from the uh from the terminal. Yeah. We can copy paste or we can just

ask the AI to make some to make some arguments up for the deployment and hopefully it will make some argument up and then create a deployment. Yeah, as we can see the contract has been deployed on the remix VM and for anyone who wants to read exactly what

happened can kind of you can kind of go through the contract and say okay I want to know exactly the program and so on but what we actually want to highlight here is the possibility that it's actually made being made available that you can actually create a contract even if you don't have a deep knowledge what

is a constructor and so on you and you can still have access to the blockchain and and so on. So we have compiled and we also have deployed and we can also we can also deploy it to to metamas. I already have metamas here in my environment. I will just ask

it to switch my environment to sele what I will be expecting is that it will change the execution environment for those who actually know how to use remix is that we will have a execution environment here. will be browser

extension because MetaMask is a browser extension and then in the background it will it will call the MetaMask API because this has been done automatically because I already I already was connected uh priorly and there was already a a an approval. If there was no approval, I will get a

traditional MetaMask popup to actually allow the access to to it. And then I can ask him deploy the same contract on CIA. Yeah. And here there's a little bit of caution because I mean cipia is a test net. You won't get any warning. uh there is a security warning whenever you are

trying to deploy a contract to a uh to a life chain there will be there will be some warning from the AI because that can you can end up into the AI paring and deploying the same contact maybe 200 time it won't happen but you can never you can never discard this uh this eventuality

and now we just accept here to deploy the contract track and it going it's going through the deployment infrastructure of the Solia network and everything is being done in the background until we have yeah exactly we have the confirmation that the contract has been deployed on sepoleia we can

also navigate uh I can close metam mask we can also navigate on scan for that specific transaction I don't even know which one I think that was the second one. Uh yeah, there's no there's no direct link, but I can copy the contract address and

simple. Yeah, just to make sure. Yeah, it says it is a contract. There is no interaction now with a contract and so on. So this was a very super duper vanilla integration of I mean showcase of uh AI usage for contract deployment and

uh functionalities. Yeah, what you can actually do with the remix AI in order to achieve some minor minor stuff. Yeah, we have gone through the compile and depart in and deployment workflow using their AI which is fairly easy. You

just use natural language. You can also use audio prompt if you don't feel like you want to type on the keyboard and your audio will first being transcribed to plain English. Now I think we only support English. You always never know with those model what kind what other languages are still supported and so on.

Maybe if you speak French, it will also get supported, but most likely you won't have the same accuracy as if you happen to speak English. Yeah. And of course, we also have advanced prompt. And in advance prompt, you actually want to achieve something much more bigger than just a simple

contract. You want to you want to create something new. And by creating something new I means like creating a entire new workspace. Entire new workspace with a new project. Let's say okay I want to kick I want to kick off a project and I don't know where to start. Uh I don't know where to start up. I just come

there in Remix in the Remix environment I say okay where I want to start a new workspace and I just describe what actually this workspace will be able to do let's just say I just copy this first one which is an example a practical example I want to create an ESC20 token and explain with comment in a contract

what I will be expecting thing from this workflow is that I get a new workspace generated with a set of contract. I don't know how many contract I just need exactly a ESC20 contract being generated and also with pretty much all the description of every function what that function is actually doing what is the

input parameter what is the output parameter without me specifying anything. So the AI come up with a structure and when that structure is done when that structure is done it creates contracts and uh one uh very specific part of this um of this process is that the contract that is generated

is being checked to be uh is being checked in in the back end to uh not uh to not be having any vulnerability I mean static check uh with leader and other stuff and also it has been made sure that the contract is compilable. I mean when we get the payload from the AI we pretty much verify that the contract

is compilable so that the user won't have to tweak it anymore with other with other stuff. There might be some dynamic error as we have seen earlier with the uh with the deployment where we might need some uh some complex argument for the for the constructor. Now we have our commentator token. So what the AI

actually understood is that we want to have an ESC20 token and he decide to call that token commentator token. And now you can see what power each word is actually having in the prompt that you actually have that you write. What the result you will get from the AI

will strongly depend on how you formulate your prompt. I mean if you are precise enough to give a lot of pinpoint to the AI, the AI will come back with a very solid answer to you. And if you just give some middle quality prompt you will have something

similar that I mean no one will ever write a commented token ping me if someone does that. Yeah, as you can see, we end up having a project with exactly that uh token ESC token that we uh uh that we requested and everything is commented for some for someone who actually wants to learn about solidity

without even getting that much deep inside the code that is already very valuable because every function that has been generated has a uh has a comment that he can actually relate to. Yeah. And then I go back. We also have introduced the newest technology or the newest stuff going on with open cloud,

code, open AI, codeex, and so on the skills. Now in Remix AI, you can actually load a specific skill, a specific skill set in order to achieve a very specific function. Now we might ask the AI. A good thing to always do is to ask the AI what he can actually do. We might ask him what skill do you have?

Yeah, as I was saying, a good thing to explore the AI is to have a a sort of conversation with the AI like first have an acknowledgement of what is the AI capable to do because it doesn't make sense to ask the AI yeah use the solidity skill to write a contract solidity if the AI doesn't have an

implementation of that solidity scale, it will start making some stuff up because the AI is a piece of knowledge or a probabilistic model that thinks he knows pretty much everything without any constraint. He will pinpoint something from his memory and then use that for generation which is not also wrong.

Okay, here we have a set of scales that are actually load inside the remix environment. It is up to the user to kind of discover those scales. Now those skills are not load dynamically based on the user request. This is also something that we might work on but it's up to the user to know exactly what skills he

actually wants to to use to perform a specific task and yeah security skills. Let us say now you know the AI is having a specific security skills. We ask the AI to review this contract using the uh security skills using Yeah. Using the security scale analyze

the commented token. What this will do, it will trigger uh from the AI it will trigger a workflow where first there is exactly the security scale being loaded which is a set a set of instruction that the AI will follow while reviewing a specific contract and this set of instruction is written in plain English

like okay when scanning a contract maybe you look for the specific latest uh uh maybe zero day exploit If that uh I mean if that uh if that scale were is hosted somewhere online it might be updated in like 2 seconds and with the zero scale and the that scale will be loaded in the AI and there are

specific there are specific uh there are specific instruction that will be that will be executed. Huh. I don't know what happened. We'll just repeat. Oh, it was still working. I'm sorry. The security analysis contract has been saved to

Okay. I don't know. Contract security analysis. I don't see anything. Okay, it's saying that this has been saved. Let's give it another try. This might be an HS where the IC is paring a little

bit. I mean from the workflow it is very it is matching what we will be expecting from the scale to be done. We first load the scale and then we load the contract and then we do the analysis. And now it says contract has been the analysis has been saved in

security MD token. I don't know why. Well, this is a case where writing files are is actually failing. Give me security on V.

This is in plain text. Yeah. Okay. Actually, we might be having a a tiny issue either with the model or or the tool. But I want to highlight here that we are using a low-end tier model. So there might be a little bit of paring

somewhere. It is actually dedicated for very simple task. And yeah as you can see we use the scale and there is uh there's a report about what can be done there is a issue there's a fixed solution which we can actually address in in subsequent message we can actually

write here fix all this proposition uh fix all the proposition you did above and then the AI will go through the over the contract and then perform all those fix for us And then we will have a we can also we can reperform that uh security analysis. After reperforming that security analysis we will be

helping to have a much more flawless contract that yeah that is audited and that you can use in uh to deploy somewhere. Okay. And then we also have quering token and nodes and specific uh address holder. I mean you can also play a

little bit of kind of quering what actually vital did last night if he kind of send some token around the globe. You can you can query that with the with the with the AI integration win date and maybe you can construct a business case based on that or you can

create a contract which is doing some specific stuff based on that. Yeah, we went through generating a workspace where you actually generate a new workspace with contracts and depending on the description that you're actually providing and and so and so forth. And whenever you generate a

workspace, there's a new workspace with your dedicated code. And you can be pretty much sure that every time you generate a new workspace, you will get a contract which is compilable. You don't have to fix around in the contract. you will yeah I mean you can extend the contract just by asking also the AI

where the AI interacting with it doesn't guarantee it to be compilable or to be static analyzed yeah now we come to the to the second part of our workshop which is about dab creation we call this quick tab quick tab why because it's quick. We can really create

uh the central eyes application in a very in a very quick manner and this has been done by employ by extending our already available quick tab version version one uh by integrating AI and now we have also several options. You can publish your app on different on different uh uh on different blockchain.

You can even have a a blockchain mini mini app and the source code of your front-end application you can also host it somewhere uh either on limo or or or also on IPFS and yeah let's create the philanthropic project we I was talking earlier um as I started

this uh this workshop I will push this a little bit. I cannot see anything. I will start this I will start this by creating a new chart session and then create a new workspace. And in create a new workspace, I will paste in

here the preparated prompt I I crafted yesterday, which is create a uh create a contract for supporting a philanthropic project that helps family and kids. It should be uh it should issue some initial tokens to user registering for the first time through direct minting. This is a little bit of

web tree speaking. In order to kind of restrict their generation, the generation space for contract and anyone can register themsel. A user could uh a user could then spend his token to a special project. The contract owner should be should be able to update a list of project and

also close them manually or automatically after a specific uh time has uh has gone and also add comment to the to the function so that I will be able to maybe uh explain it to someone else or uh grasps the idea behind it. And then I hit generate.

And I am using here the workspace the new workspace generation uh feature because I want to have an atomic solution. I want a solution that kind of match my intent and also want a solution that is compilable that works that only works out of the box without me having to interact with anything at

all. And yeah now we wait a little bit while it is generating you always have some feedback here what is actually going on in the background we are compiling the contract and if it fails there is a I mean the agent will reiterate re reiterate the process reiterate the process in sense in the

sense that the same prompt will be sent again to the to the AI and then we will be uh Yeah, that was the case that the contract was not compilable and then we sent the prompt to the AI to for another generation and the timer a little bit of water.

Well, that takes way too much time. Let us give it one more try otherwise we will maybe reload the page and start from scratch again. Yeah, there might be there might be an issue. Always have to check maybe the issue can be related with the internet connection

which is optimally not the case here. Just a little bit of patience and then we will be we'll be there soon. Yeah, exactly. And here we have our philanthropic token which is an ESC20 with the I guess with the initial amount of

with the initial amount of token by user which is 1,000 which is really good. I mean by experience I already know when I'm looking at function minting and so on I already know that there's a process of issuing some tokens to some users and so on but this is not what is actually

uh good for us I mean we can go through the process of asking the AI to compile and deploy it everything and so on we have already gone through that we don't want to do it anymore so we will just do it manually to speed up the process I compiled the project. The project is compatible and now I want to deploy this

project on uh on Sepia because uh it will be much more easier to interact with and also for you. I select the browser we have separ from which I am logged in and then I will just deploy the philanthropic token which is compiled here. I press deploy. I expect Metamas to send to create a

transaction which I confirm. Okay. I wait a little bit and then voila, I have a contract which is deployed on Sepia. The good thing is now in order to start quick tab there's this tree up here right to your contract you just go over there and then you create a DAP and creating a D app when you press

that you will also have a text field where you actually describe how your decentralized application will look like and this decentralized application is just a website which will be reflect uh reflecting what is inside the contract. What is done here is that uh we are taking the contract source code and also

the contract API. So we know exactly how to connect those and then we connect it to traditional uh traditional website uh uh uh I mean traditional website uh front end generation that we already know. And for that purpose, I already also have a a prompt for that which is a little bit long

because we want to have something nice which I will just paste in there and then read again through it. So I want to create a DA for this phanthropic project that I already created the the contract for where user can participate to some blockchain web three donation. So I want some user to to donate some tokens

in real world case that will be donating money. Once the user connects to uh connects to the platform with its wallet there should be a mintable button for initial minting process in order to get the philanthropic token. actually the token you want to uh you want to u uh contribute with that will that will

contribute to the philanthropic project. Okay. So see register user from the ABI to make sure that stuff are aligned, make it much more modernistic to look it to look make it modern to to have a really nice UI. As a contract owner, I want to be able to push new contract. I want to stop

ongoing ones. I want to I want the AI to make all contract function available to those with access. I mean there might be users uh that I want to really get uh access to. I mean maybe at some times I don't want to host any project anymore. I would like to say okay this user you

have contributed a lot just go ahead and take over this project and so on. This is what this prompt is. I mean we can go further but I will hit generate and what this does is it is similar to it is similar to what we already know from the new workspace. This one will generate for you a react a react front

end uh application and that react front end application will be will be right here in your browser. So you can also use the AI in order to uh yeah you can use the AI in order to go through uh through the code review or change specific stuff if you don't like

it. I mean if you have the design and say okay that looks maybe too bright you can just ask the AI okay make it a little bit dark and so on. I think you get the idea what without getting too much uh specific into into details you can you can change everything you want as as you desire

and also one good thing is that uh the the space for the react app is very different from the space uh from the from the workspace for your contract. So there is no so there is no interaction there's no confusion I mean the front end app is based on your contract but where you are actually developing your

contract is separated from where you are developing your front-end application which is something you always want to have you don't want to mix them all up now it's taking a little bit of time still cooking in the background cooking and then I hope we will end up with with a nice front in project that we can

publish. Yeah. And then we are done. And then once it is done, you can see up there capia. That means the contract has been deployed on Coolia and all the interaction you are having is on Solia. And here you have your philanthropic platform. You can click here deploy to

IPFS in order to have a yeah an external link and we can also register it to be a remix application and then I will give it uh filler. Okay, then register subdomain. I hope this goes really quick as we only have less than five minute. And then I can click to this link.

Let's see which one was quicker. Yeah, I think the IPFS was much more quicker. Now there's no project. You can connect your wallet to it. I will just connect my Metam mask. I am already connected and I can register and mint my token. As you can see, it creates a it creates

a metam mask transaction where I now get thousand tokens and so on and I can also create a new project. Exactly. After the minting process, you can see my account balance has been updated and now I can create a project. I can say this project I want to test. And now you can also specify the bene the beneficiary of the

uh of the philanthropic project and the target amount also. Let's put this to 100. Huh? What did I do wrong? Let's create again. Oh, I think yeah, I think I guess I know what the typical problem is.

Yeah, I mean, nevertheless, we do not have enough time to go through through this anymore, but I think you guys all get the point of uh these philanthropic tokens being created. This is this is actually the power of the new of the new tool that you actually get in in

Remix AI. Whenever you encounter such a such a problem, you can you can always return you can always return to the to the remix to the remix AI and then explain the problem here and then this front app application will be updated until you will arrive to the point where you say okay this this front end

application is now reflecting my proof of concept that I can actually uh show to uh my stakeholder and then they will have a much more better understanding of what I am trying to build without going through several months of development and and so and so on. Since the time is very short or already

almost up, is there or are there any question that I can quickly answer? Yes, please. >> Yeah. Can you please >> um we came a bit uh I came a bit late so I'm sorry about this but um which model is below the remix AI. >> Yeah we are using a set of models for

different task and now we are using the mistral medium as a default model that you can always get I mean for for free. Yeah, for specific for specific uh deep AI uh requests it might not be sufficient. I'm guess you already know that's the main reason why OpenAI and CL they have a

pricing tier which is much more higher for this big model and actually if you have a solid workflow it will be much more better to use those model because you can definitely feel the difference. >> Yeah. Is there any rate limits on this like if you can iterate and iterate again and again?

>> Yeah, there's a there's a rate limit. You cannot iterate 24/7. >> And uh do you have any number like if people are using it for mainet deployments or anything like >> I mean the this is a very very new concept. This is a very new tools and we are actually giving everything out in

the beta. I mean there's absolutely no restriction, no pay world. You just register as a beta user. I will encourage pretty much everyone to go on beta and then try these features all for free. Are there any further questions? In that note, I thank you very much for

taking all this time. Thank you. Hey.
