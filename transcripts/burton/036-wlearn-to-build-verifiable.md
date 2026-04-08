---
title: "WLearn to Build Verifiable"
speaker: "Dayan Brunie (Consensys), Satya"
organization: "Consensys"
stage: "Burton"
youtube: "https://www.youtube.com/watch?v=O8qbWZ7E3LE"
transcription: "youtube-auto-captions"
---

# WLearn to Build Verifiable
**Dayan Brunie (Consensys), Satya** (Consensys) --- Burton Stage

It's 55. >> We can start. >> Okay. Good. >> Hello. >> Test. Test. >> Perfect. >> Thank you very much for attending this session. So um we are both from

consensus and we work on agentic for the company and we are doing experimentation. I've contributed for the ARC804 for trustless agents. Um so I'm software architect and Satia. >> Hi I'm Sat Satyit Kabre. I work uh in consensus. I'm a senior software

developer. >> So this uh session is a workshop. So you would be able to code but it will be intense and you have some prerequisites. Um so is there any one that plan to to code in parallel? It's okay. I think the best is to code after if you are convinced about our

qualitative presentation. You would be able to to code and to do the workshop. But if you want to try at the same time you can. Um I will give you the prerequisite and you can try. Okay. Get ready with your computer. Everything is settled. Okay. So um we have um investigated uh the way to build

trustless agents. So trustless agents are agents that are transparent so with open source and um so ability to see what the agent is doing. So in contrast with all OPAC agents that are existing today or also AI services that exist and also verifiable. So this is leveraging cryptography and it's how you trust but

verify with cryptography what the agent has committed uh itself to do uh in a in a very transparent way. And the last property of trustless agent that we are going to showcase is the trust minimized aspect. So AI agents have agency over wallet and they will be able to um to have delegation from a user in order to

do some operation. So the the idea is here is to do the enforcement of of the permission at the settlement layer. So at the blockchain layer. So we are talking about um agent for end user. So real user at scale it's not like your personal agent that you will

use for your own uh good but it's agents that you will be able to deploy and run a business or that will be able to uh interact with thousand of users of of agent million of agents uh in a in a trustless man. So for for building this agents so we are going to to surface some um stack

that we feel that was optimized for what we want to show. So first we are going to leverage lung graph uh for the the agentic runtime x402 for the internetative payments onchain delegation for uh permission um granting to agent and 8804 and te for verification and discovery of the agent.

Okay, so for those that want to to follow up, there are a lot of prerequisite. So, uh you need to have NodeJS PNPM package manager. Um and you need to have API key for an LLM. So, your favorite LLM and uh we are using a smart account. So you need a a bundler access or pimnico

and you need some if so if you feel that you will be able to follow and having all these prerequisite uh go ahead but uh um otherwise you can just scan the the GitHub and you can do it afterward. I give you a few minutes seconds. Okay.

Okay. Good. So, let's have a quick overview of this landscape. [snorts] So, we try to surface what are the agent uh trustless agent building blocks. So, here we we define some layers. So, we

have of course the um interfaces layers. So how the agent can interact with human with chatbot for example. Um how the agent can interact with other agents uh with A2A MCP and so forth. Then you have the agentic layer. So it's all the reasoning of the agent all the the execution of the agent all the routting

of the agent. So all the the the yeah the the runtime then you have the settlement and verifiable state. So here um you have like the settlement and the agenty of of the agent with his uh account and the ability to delegate with smart contract and also uh register on chain and so

forth. You have all the cryptographic aspect with creation of of private key uh having the the proof like the different proofs you you will need for uh this uh trustless agent and the infrastructure uh dimension. We have surfaced here all the trust model because each of those so for example for

the settlement and verifiable state you have blockchain uh and here you have everything that is verifiable and so forth but for others you have different quality of uh of trust uh with like cryptography with authentication cap capability based solution and so forth. So I will let Satia just uh give an

overview of each stack that we are going to use that are covering the different aspect. >> Yeah. So for the um limited time we decided to uh use the subset of uh uh this stack. Uh so for the interaction uh surface for the user u we we are using telegram uh and discord and we are

exposing the endpoint with a2a. Uh for the agent computation layer we are using lang graph and lang chain. Uh these uh this langraph is basically one of the um one of the many famous tools uh used for the uh developing the agent workflow. uh and I'll explain a little bit in brief why we chose langraph uh in the upcoming

slides. In the settlement verifiable state uh we are using metamas delegation toolkit uh like metamas smart accounts for the uh identity registry we are using 804 agent zero uh SDK uh which can perform operations on the 804 like registering agent uh and etc etc. for payments [clears throat]

uh X402 uh ERC20 uh tokens and u for the cryp cryptographic uh control plane we we are basically uh deploying our agent on the Egan compute uh and uh VM basically for performing the blockchain operations u and um we are executing all these transactions on um um base uh L2 but

just because I mean uh it it's probably um compatible with X4020 SC20 but Um it works on any L2. >> Thank you. So let's build. Okay. So in the repo uh you have a readme that will uh help you to go over the the different um steps in order to run the workshop. So the first uh aspect

uh is to understand the project structure. So in the repo you have uh the source and you have the workshop correction where you have everything implemented and the workshop. Um so those are the prerequisites um in order to to play with this workshop. So

first uh we have uh implemented some scripts. So the first one is to create smart account. Um so um you just uh launch through PNPM the create uh function. So we are using VM to create the smart account and then we are going to test it with a hardcodit uh arcodit prompt in order to test that our

trustless agent is working correctly with like basic setup and then we will launch u an agent with an HTTP server in order to make it accessible uh by any uh uh anyone. So it can be an agent or a human and at the end the registration process to register the u the agent in the RC804

identity registry. Um so let's start uh with the environment variable. So you need to come up with your um LLM API key. So we are using open AI lungsmith is a monitoring tool in order to be able to monitor all the reasoning of the agent in the the workflow. So we we'll

see this after um bundlers. So they enable to to to to tackle smart uh accounts. So it's a smart contract uh and smart account um uh transactions that are uh managed here. And since we are use delegation we need uh this and in our example we will um have one first persona that is a user a human user. So

here for the user we have is it smart account address and its um EUA address. Then this user will interact with an agent that have its own address as well. And this agent will interact with another agent that will uh be the the final agent that will um do the the final um um service that we want to

offer. So it's just to illustrate that we can delegate with a chain of delegation a target address just to to send like phone to to this address. So once all those uh environment variable uh uh setup you can start the workshop. So the the entry point is in the index file. So

in the index file you have uh the entry point where you can launch uh the different uh command I I show before. So we'll start with the test part. So test is just here we have the agent runtime that we are going to invoke with a human message. So it's a a static message where we transfer a certain amount of if

um so okay we go to the agent runtime where we have implemented the agent. So if I start uh and test the execution we have an error that if you will do the workshop that we say okay we need to implement the invocation of an LLM. So we are building an agent uh so agent are

working with LLM. So we are using n chain and n graph. So longchain is giving lot of tools to interact with llm and provide like agentic tool and lung graph is doing the orchestration. So I will cut this in order to show you those different aspects. So I use open AI. So I will create like

just a model um up new chat open AI. Okay. And this model will have like a few characteristic. So we just copy this to go faster. So you have the the model uh the

temperature that we will uh let as default on the API key. So this will be the LLM that we will reuse for different reasoning that will be conditioned by different prompts. So here is a long graph uh dimension where we have this object that we call the state graph. So this is one of the

main uh um primitive of long graph. So basically you add nodes. So here you have my LLM that is one node and each node is a function. So um we have the LLM the reasoning and you have tools you can add like many tools for the agents in order to fulfill uh its services. Um and then you have edges that connect the

different nodes together in order to have the different uh conditions that you want to offer to to your agent. And conditional edge is the condition where you decide whether whether the agent are going is going to call another agent is calling is going to call tools or is going to

end the process to provide the the final results. So in order to illustrate this um I will let Satia just explain all this uh mechanism with this uh this workflow mechanism offered by uh Lang graph. >> Yeah thank you. Uh so hello is audible. Yeah now it's good. Uh yeah

so lang graph uh is one of the like as I said uh is one of the uh many tools available u to uh create the workflows with u uh agents in langraph particularly uh the the nominee used like there are some few terminologies it's very easy like uh there are only two main terminologies in uh langraph uh

one is node and one is age so you can create as many nodes as possible for your um requirements and then connect those uh nodes with the ages Uh so you can see here there are two um uh yellow nodes which are mandatory which doesn't nothing that doesn't have any code inside is just uh to langraph

to know that uh the workflow starts here and workflow ends here. So between that uh [clears throat] for our example uh code we created one LLM node. The node uh basically is an agent. Uh it can uh use LLM or it cannot like I mean uh it doesn't have to uh it can only have a pure code. Uh but with our example as we

want to get input from the human u we going to use LLM to understand what's the requirement. So the LLM node is connected uh as shown in the code like um the open AI model because just to give a brief uh history about um uh lang chain and langraph lang chain was initially created to compete with open

AI SDK and uh it was like in very basic form then they evolved into langraph so u that's why you can see there are some core libraries used um on the langraph so inside that so uh that's why the by default it's using OpenAI model but uh if you want to use something else like a deepseek you can still use it using the

URL parameter. So that's that LLM node will use the LLM then it will uh basically call the LLM. LLM is not able to is not capable basically to do the action. So I it depending on the message it will basically um conclude if it needs a call or not and then uh give it back to the agent. Then the

conditional age will decide whether the tool is requested or not. Depending on the tool requested, uh the control will go to the tool node and then tool node depending on the array of um basically it will pass the array of u uh list of um tools which needs to be executed. Then the tool node will execute the to

uh the tool then get the response back from the tool uh send it back to the LLM. If LLM is satisfied with it uh then it will basically go to the end. uh if it needs more tool calls uh the loop will just continue and you can imagine you can design u these if conditions and make uh complex systems uh using the

langraph. Yeah, one more thing sorry the state uh the the to share the information between the nodes uh nodes needs to let's say pass some information between them like what's the context happened before so for that state is used uh in langraph by default the state is shared only for the one execution

let's say there are concurrent messages u happening between uh human and uh this workflow for that if you want to sh keep the track of the state like previous messages uh it's just one line of code just add a checkpointer and it will keep track of it. Yeah. Back to Dan. >> We can we can illustrate uh the states

uh with like the the the first the the main uh object that are messages. So basically you can see the state as a a collection of message and you have three kind of messages. You have human message. So it's all the prompts that are coming from an external actor. uh system message uh can be like any uh

preprompt or any system information that we want to provide to guide uh the agent with other context and AM message it's the uh reasoning uh message provided by uh the the the LLM nodes basically and we can enrich the state with any information we can structure the the the state with uh uh the the needs that we

have so in our case we manage delegation Because each execution of the workflow so it's a invocation of workflow we call that we can we provide the delegation in order that the agent is able to uh act on behalf of the of the delegator. So going back to the code um so

state graph so as I said before this is the main object um first we need to implement the reasoning so it's the uh llm node here so each node are function and here we have this error that have been thrown so we need to implement the the logic so let's say I want to give some uh preprompt to my

uh to my LLM. Um so I want to say uh you are a trustless agent that orchestrate onchain uh actions and uh then I want to retrieve the prompt of the user. So here as we surface it we can get the state from the messages um inside the state. So I go state do

messages and here I will have all the message. So I can console log this in order to show uh this part. Okay. Um so the next step is to call the the LLM with this state as an input. So um I will uh get a response and I will call the

model. So you remember before we called uh we create this uh chat open AI object that we called model. Uh so this just call um the uh llm and we will do model and then we will uh invoke the model okay with uh the preprompt that we will uh instantiate as a new system message and the prompt here that will be a human

message. So it would be a new human message. Okay. And we have the prompt. Okay. Maybe here I just do this and it would be good. Okay, we need an array and we are good. Okay. Um

this I'm not sure about this. Okay. So uh now I can uh just reexecute my uh my agent. So I will run the test. So you can see the human message transfer if to this address. [snorts] You can see uh the response of the AI. So the AI is not able to do this

transaction because we haven't affected any tool to this uh AI. Um so now this is our next step. We will add tools to this uh to to our AI. Um so we create so in long uh chain you have the tool node where you can add tools um and here we have uh implemented a transfer tool. So if we go to transfer

tool basically it's just a function uh with the logic we return uh the response this will be read by the uh by the uh agent and in order that the agent decide to whether this tool is is relevant or not it will the agent will read uh those metadata. So the name of the tool, the description of the tool and will provide

as input those uh those fields. >> So basically behind the scenes uh the langraph understands uh this u the format of that node uh so the tool basically and then it uh guides um uh that which tool needs to be called. So this is the format by default. There are so many tools given by uh lang graph

itself but this is one example of creating your custom node. So you have control over over your code and this is align with uh different standards like uh MCPS KS and so on. So you can easily uh like with the the native SDK add like new tools that are coming from another source and not just implementing you you

set the tool. Um so here we have the check checkpointer is as uh mentioned SATA is a way to uh register the um the state uh across the different interactions. So now we have the the tools that are available for the agent. But first we need to implement the conditional edge.

So here we return n by default. But we need to look at the state retrieve the last message. So here I retrieve uh the end of the the array of the message and then I do a condition. So where I um return the I I check if the last message in the state is a AI message meaning that the our LLM has uh spoken uh at the

end of of this uh loops and I will verify that the LLM asked u to call a tool or not. If not we end it. If yes we call the tool node. Um and then we will have uh another loop where the agent will uh say okay we can finish with the with the operation and it will respond uh with a message

without any tool call and with an end message. All right. So now I will [snorts] execute uh this So you have still the human message. Okay, I forgot one thing is to uh bind the model with the tool. So for this we need to have like um the this just model

bind tools uh and you affect uh the model with all the tools uh as a collection of tool for an capability for the agent and here I will call I we call model with tools >> that's just basically to uh make uh LLM aware that which tools are available with Okay,

so we have the message here behind the scene we have delegations that get that are signed offchain and then uh you see the AI message where you see tool calls okay and if you go down you have tool calls and the list of tools that needs to be called. So here it's require a transfer uh tool call with those

parameters. So everything have been code and you see that all the the transaction have been successfully executed on chain leveraging um our um delegation and using bundler for um for the delegations. >> Do you want to show langmmith?

>> Yes. >> So lang is a monitoring tool of lang graph. So it it show all the the reasoning of uh the nodes because here we have just one tool and one model but we can have like yeah many tools and many models that reasoning models that call each others but here you can see

how it looks uh like >> yeah so it's basically u giving visibility of what's happening behind the scenes like u especially that's a challenge with multiple nodes talking to each other it can go into the loop you don't know what's kind of prompts are being used um for the communication

between the agents and nodes. Um so lang is uh like um uh the tool provided by langraph it just you have to add the keys and it will just start working. That's one of the reasons we uh that's another good point of using langraph. uh you don't have to code much about it on on it and as you can see here uh like um

there are you can go through like how many tokens are being used uh you can go into the details metadata all kind of prompts system prompts AI prompts u uh AI messages human messages everything is uh listed um and it's quite helpful just for you know uh checking to make your prompt better uh you can go through it

and uh revise your strategy yeah >> yeah so here you just have the model that calls tool and then you go back to the LLM that say okay I have everything I I need so I go to the end of the process all right um so um behind the scene uh we have

used delegation so just quickly so here when we invoke the uh the agent we uh provide a message of a human so it can so here it's hardcoded then we will see how we can send it with HTTP but it can be coming from telegram or any kind of of source and then we provide uh in the state a sign delegation. So here we

just sign the delegation. So basically to sign a delegation you just create a smart account. So here we used uh smart metamas smart account. So we provide we sign it with the private key of the of the user um and we create a delegation here uh with a scope. So here we have a scope uh

that is named native token transferment. So uh the agent that will receive this um this delegation will be only able to do transfer with a a certain uh address. So here we have just one address that is uh possible to to send um and we can add like a lot of of condition. We can have a maximum amount.

We can have like a periodical um allowance and so forth. >> Yeah. So basically you can achieve a granular level of control over what kind of transactions you want agent to perform on your behalf. You can set a limit on your u let's say token amount. You can even restrict number of

executions um per month. Uh you can even restrict uh let's say uh only these transactions can be only done uh by a particular unis swap uh uh address. So yeah it it can be granular. It can go to a very low level. U so that's the uh power of it. Yeah. >> Yeah. So this is like the the first

delegation. So maybe uh let's see it with like an example uh with a diagram. Okay. Such I you explain the first part. >> Uh yeah. So in uh uh there are different varieties of u smart accounts. Uh metam mask has a one way of implementing it. So in uh metamask delegation toolkit metamas smart accounts there is uh some

part which is offchain and some part which gets executed onchain. Uh so delegation is the main part where it's like a signed permission like I allow uh user to uh execute transactions on my behalf. That part is uh this permission. So this is composed of like from which user and to which address the permission

is given. Then user [clears throat] signs uh that uh delegation but u it can be kept off chain basically because it's a signed thing. Then uh you can see another delegation that's to uh show the capability of chain of delegation. So one example could be I allow uh my agent to perform uh pay for my subscription on

Netflix or Amazon. So Netflix and they will have their own agents. So it it's kind of a chain of delegation. So I allow agent to give my delegation it can give transformation subset of delegation to various other agents as well. So that's uh that can be achieved using the chain of delegation. So here you can see

the there is a reference to the parent delegation and uh the permission which is a different it can be a different permission it can be a subset of permissions and then from agent one to the agent two and agent two is the last end user who will actually use the delegation uh so that actually creates a

user operation u user operation I think u yeah Dian uh will explain that's the onchain part >> yeah so in our in our use case uh we have the users that delegate uh over transferring if from its account. So when a delegation is sent to this agent, the agent can transfer if from the user

account. And when you look at the block uh explorer, you see that it's the user that sends the transaction. But behind the scene, it's the agent one that triggers the operation sends to to the delegation in implemented in the smart account of the user. Um and then the agent one just can redle and for

redelegation it just you cannot delegate more than the permission the initial permission you can do the same or a little or less so it's if the maximum amount is to transfer one if it can transfer like 0.5 say okay the the final agent can just transfer 0.2 to E for example.

Okay. And the user up is like the transactions equivalent for a smart account. So the agent to uh in our example as a smart account. So it will uh send the the transaction so user up uh through the the the entry point. So in each blockchain you have an entry point for

smart uh account verification and actions. So here the agent 2 smart account will verify that the agent 2 is the owner of the smart account and then it calls a delegation manager that will be the the smart contract that will enable to execute uh from the agent to uh smart account the

the operation on the user smart account. So yes here you have all the chain uh of delegation and all the process end to end. So in the code we have seen like the delegation part from the the user perspective at the beginning when it sends the message to the agent. But if

you go if you go to the to the tool here we what we are doing is that uh we are retrie retry retrieving the the sign delegation. So we have the parent delegation and then we can um on top of this create a transfer delegation. So this is a second delegation. So it's the same operation but for the chain and

then we call the external agent that will do the final transfer and we s we send the two delegation in order that the agent uh agent two this one will uh execute the uh final operation. So all the magic happens in that bundler thing where the uh transactions are submitted via entry point and the uh

validation and everything happens inside and then actually the transaction is executed on behalf of user. >> So now to make it more uh production uh ready we will launch a server. [snorts] Um so here you can directly go to the uh agent service and here you have all the endpoints that we

offer from our agent. Uh so basically um it's just an express server. Um and we offer like an agent card. So in in A2A standard agent card is the the card of the agent describing the the the endpoint to access to this agent the auization authentication method that you need the skills that are

available the price and so forth and agent URI is like the metadata uh that we will push to the ERC80004 so the identity registry and then we expose like several service so free service paid service and as example MCP and eightway endpoints. So if I go to the agent service, uh you

can see that um you have the different uh endpoint. Okay, I'm going down. So basically it's just the express app and then we just uh do uh some uh get uh rest endpoints for card for ur agent uri and then we have like post for uh actually using the agent. So here we'll show like just two uh endpoints the free

service that are accessible for anyone for free and the paid service where we will put x402 um middleware. So the server is is is up and running. So I can do a http request. So for example I will use uh this uh curl command. So this car command is just calling uh

with a post request HTTP request the free service and we just put in the message to send uh 40 uh some if to this address. So behind the scene it will be exactly the same execution than the test. It's just that uh here we can change uh the the the prompt. um to make it a little

bit more interesting I will add here. So I'm going back to my uh runtime. So aent runtime. So here it's my state graph with all the prep prompt and so on. And I will add new tools. So today we just put the transfer tool. This is actually working but we mocked some other tool. So we have swap tool,

staking tool, yield farming tool, lending tool. um up. So I will import all those tools uh functions. So if I go back to okay trans to the tool so it's just a collection of tool. So we saw before the transfer tool with uh all the the logic and then we have swap tool. So here if

you want to to play with the workshop after at home you can just uh try to implement the swap tool and basic basically um so same for staking tool and so on and basically um the agent is just reading the the return message. So if we put it's successful the LLM say okay it's successful. So it's easy to

mock. So here it will if we ask to do staking since it's written successful it will just uh return uh the the message. So if I do this, so I will ask to send uh if to this address and stake uh five if uh on mainet and to uh borrow no to lend um yeah one,000

USDC um and to yield uh to do to do the best yield farming uh um transaction in a liquidity pool. Okay. And I will show after in nmmith. So you will see all the tool call and so forth. Okay. So the tool have been added and

now here we see like everything that is being called. Um yeah. So you see the different invocation. So I will go to long smith [snorts] and it will appear. Maybe this is this one already.

Okay. So he called like uh like several time the same tool. Um let me see why. agent runtime. Okay, I will just put this like this and I will reexecute. I know why because I didn't restart the server. Sorry, I did the same error in our test

before. Okay, so I will restart the server because I changed this but I keep the server uh live. So no. Okay. [snorts] Suspense. Okay. So yeah, you see that I can see on

my message here that it's calling the different tools landing, yield farming and so on. Okay. It's a lot of comments but uh here you see the initial human message and here you see all the tools that have been invoked and basically in each AI message it was a new tool call uh either depending on on the reasoning

it will be like um each tool uh at in parallel or or each different tool um recursively. Um, okay. So, I'm going back here and here it will refresh. I believe it's this one. >> Yes, sure.

>> Yes. Okay, I will show you that. So here you can see like uh that the agent has called all those tools and at the end here you see um yeah the message that okay we have stake five if okay we have learned this and this so uh you question okay so the conditional edge here is

quite simple uh it's just taking the last message so if we go back to the loop in the workflow. So the model uh have the the prompt with like all the the things that it needs to do and it will first call the trans it will say okay I need the transfer tool but just

the transfer tool. So in the conditional edge it will look at the last message. The last message will be AI message with like metadata uh requiring transfer transfer tool. So it will call the tool to tool node and we'll uh just uh call the transfer. It will be done. Then it will go back to the LM node and it will

look at the the state again and say okay the transfer will be done. Now I need to stake. So it will go to the conditional edge and we will have the tool node uh stake and we'll go back to to node. the tool will do the staking thing and will go back here etc etc >> yes exactly

>> yeah the lang graph actually um I mean uh if we are using the uh tools provided by langraph itself uh this probably is not required because uh it knows the tools um which it has but we because we are using custom nodes uh we can add some custom logic okay this means this transfer for means transfer node. So

that's the reason. Yeah. >> Uh so uh when we add uh tools to LLM uh he it already is aware of what tool it has but uh by the I mean if it's a properly named uh prop Yeah. Yeah. first. >> Yeah. Yeah. Because

>> then then it will only choose two. Yeah. Uh >> in the order as well. Yeah. Yeah. But it depends like how specific prompt you want to give. Uh if LLM is not good enough, the model is not good enough, uh it probably won't perform well because it's chat GPD like uh it it is

understanding those things in sequence. But you can control that as well. If you want to use like a let's say smaller model maybe your prompt has to be a little bit specific like if you these are the tools available. If user ask transfer then use this tool. Uh yeah the reasoning layer is really uh

deciding the way the tools are used. For example, you can ask, okay, can you uh transfer this token to uh this uh chain uh with a a swap and it will automatically see okay, I need to to use bridge first and then I need to do a swap and so forth. So the reasoning layer will be able to do it if you have

like it depends of the quality of the model but also the quality of the prompt and also uh how rooting is is uh is implemented. So you have to do >> I would say that if we need crosschain we would need to have uh an additional bridge tool that will uh do the the the

bridge between one chain to another chain and then we need to have like swap that are uh working for the chain the the target chain >> especially not just the swap. >> Yeah. Exactly. Yeah, actually we have many tools and then the agent do his magic by using the right tool in the

right order. >> So is this different from the export to layer or >> from the what >> export? Ah yes it's uh it's different and this is a good trans >> yeah so actually x402 is is completely uh used for different purpose u I mean

this thing is um explaining basically how delegations can be used for bridging and uh I mean any blockchain operations u x402 um is on one layer above uh it's in the middleware uh I mean like uh I think u dan can explain it through the code itself um >> yeah okay

Um so going back to the code so I mean my express server in agent service this um so let's say that we have the paid service today it's not um implemented with x402 so what we need is to create a middleware that will intersect the call the HTTP call that will um be um enforced here with uh with X402 and

interact with a facilitator. Okay, I will show you the diagram. Um so here the client is the the the the user the entity that will send the HTTP request. So for example here we have the paid service that is a post HTTP request send it to the server. The server has a

middleware that say okay um this endpoint need to be paid in order to access the service. So you send a a response message with the code 402 and in this uh 402 uh response you have in the header a x payment uh field that will say all that will give all the information about the

payment how much which chain uh and so forth. Once the client have received this, it can send the request with the X payment header uh um fulfilled and in this uh X payment header. It will be it will be an offchain signature uh that will be a ERC uh 3009 authentication. So is there

behind the scene it's a it's um a P712 signature that is usable in ERC20 token with the function transfer with authorization. [snorts] So another uh slight explanation on it like uh in this example particularly x402 let's say imagine I am developing

few agents and I want to deploy it u and I want people to use it but I don't want to give it for free. I want to charge let's say 01 for each u request. So this example shows basically we can use x402 payment in that and um um collect some fees just to pay for the um I mean services we are providing. So behind the

scenes what uh in in the code what we uh we showed is u not related to the x402 that's a completely different thing u just to clarify the confusion. >> Yeah. So what I I'm going to code now uh it's the server that is having a um a collaboration with a facilitator. So it's a trusted entity for the server. So

the server has nothing to do just uh finding a facilitator. The server will say okay I want to receive 0.01 USDC to this address. It will be send the the request to the facilitator that will check that the signature is correct. Send to the right uh address and will then execute the USDC contract and send

the respond to the server. the server can check if it if if it wants uh and and then fulfill the service uh that is offered by the paid service in our case. So going back to the code so I have the paid service. So today you have like SDK that enable to implement that really easily. So in express for example you

have like a solution that uh enable to do it with few lines of code. So you have uh app dot use and you have uh this object that the payment middleware and the payment middleware will have uh in parameter the the address on which you want to receive the payment. So I have the target address and then you provide

uh the endpoint on your on your um express server, the price you want to make uh it uh payable, the network and the uh information for in the HTTP request for interpretation. Okay. So now we have the middleware and normally uh if I try to to call this request uh I will have um the uh x402 uh

response. So I will restart the server. >> Uh check the target address if it's added. >> Yeah, thank you. Yeah, it's good. Uh it's just want to type. Yeah, it's okay. >> Okay, I know. So, okay. Target address

as Okay, now we have a type. Awesome. Thank you, Sata. So, I will restart the server. My server is now running. And what I will do now is just to call this uh endpoint. So paid service. So the same as we have

done before but paid service. Uh uh empty reply from server. Okay. I think we have problem with the pay to address because it's not pay to address. >> That's I think there are three minutes

left. Um >> okay, three minutes left. Okay. >> Shall we do QA? >> Yeah, I we conclude. So I just show you the request and then we >> Yeah. >> Okay. So it's just the wrong one. Let's finish with with a positive not

with something executing correctly. >> Yes. Okay, it's here. So here you have the X402 uh headers that say okay I require to pay blah blah blah blah blah and then you can um we have like something implemented that pay automatically. Uh okay so it's this call service and here

we just pay USDC and it's calling correctly the the uh the endpoint and everything is uh is done. It's under the hood managed. Okay, so it's all for X402. And the last thing, so we will not go into detail. It's ERC 80004. And here basically we have three registries, identity registry, reputation registry,

and validation registry. And here, so you can play with the workshop at home. So it's the last step agent registration. So here basically we are just registering the the the agent. So to do so you call register and this will register the agent onchain. So there is an SDK that is really convenient that is

uh agent zero. So we provide like uh the information the private key and so forth of my our agent name description and so forth and and then everything is registered on the registry and then the agent is is discoverable. So you can see the chain ID and the ID of my agent. So it's 3336 on the test net and here you

can see information about the agent directly on the explorer. So there are explorer that enable to see agent information and so on. So that that's uh that's it basically um right in time. Uh so just to conclude so I will show you again the repository um QR code if you want to play with it

at home. Okay, there is a trust executioner environment. We will not go in in in deep inside this one, but it's about enclave and verification and you can send the verification to the to the ERC804 uh verification registry. So this is a repo. So you go to the readme and

everything is explained step by step step by step if you want to play with it. And you have the slides if you want to use the slides. It's a PDF. It's not the last version but it's a good version. >> [laughter] >> Uh okay uh Satya if you want final words

or anything. >> Yeah thank you uh everyone uh I mean yeah it was a good I mean we had so many things to we tried our best u u because we tried to cover so many things in a short time. So sorry if we have missed anything or confused you guys. Uh yeah, >> thank you.
