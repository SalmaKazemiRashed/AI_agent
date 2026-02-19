# AI agent Course 
This repo is the summary of AI agent course I took from [maktabkhooneh](https://maktabkhooneh.org/)

##### The final goal of AI_agent course is to make a personal AI_agent from scratch for doing personal tasks

## chapter 1: Python

In n8n we sometimes need to write a function node, This is written in Javascript, but we need to write it as a python node in order to e.g., read a csv file, analyse it with pandas, cleaning or normalizing it before sending to a LLM, or use a local pretrained_model. With Python we will have lots of customized features.
N8n is for automated running of Agents, however, developing and testing Agent itself is always conducted in Jupyter notebooks or colab.
Without Python we will remain a user, not a designer or developer.

To start we need a IDE (Integrated development environment). VS code we use. 

Both Jupyter notebook and Jupyter Lab gives us iPython or interactive python as web based IDEs.


#### lambda function
```python
lambda arguments: expression
lambda x, y: x+y

my_square_func = lambda x: x ** 2
print(my_square_func(4))  
```

#### Map function
``` python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  
```

#### Filter function
``` python
numbers = [5, 12, 17, 24, 3]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
  
```

#### Sorted function
``` python
people = [("Ali", 25), ("Soheil", 35), ("Reza", 20)]
sorted_people = sorted(people, key=lambda person: person[1],reverse=True)
print(sorted_people)
  
```

pip install packages from pypi.org 


## chapter 2: AI agent, chatbot, Agentic AI, and n8n

AI agents are good to have these days, we will compare them to chatbots and also we will define Agentic AI.

AI agent: a software layer that would do us some repetitive tasks and frequently (They won't need access level and won't need much thinking). 

```plaintext
Agentic revolution: Cloud  -->  SaaS
                    Mobile -->  App
                    Agents --> Agentic Economy
LLMs will be used in Agent AIs.
```

There was chatgpt moment at 2022. Now is AI agent moment for us. They are all like personal agents for us. 
There are different Agents: Customer Agents, Employee Agents, Creative Agents, Data Agents, Code Agents, Security Agents

LLMs give rise to the Agentic economy.

#### agentic AI and AI agent

AI agents would do the repetitive tasks daily but for those who need human feedback or human intervention still no. 
In agentic AI, agents do everything and find the task they should do. We are still far from that. but AI agents are great now at doing defined tasks such as checking, tagging emails...
All of these are possible with LLMs and the connection to LLMs. 

A use case: search through web pages are now mostly done by agents. 

Some tasks still need human feedback such as LLM-chatbots they use RLHF protocol. 
So, there is a distance between AI agents and agentic AI.
The goal of this course is to have our own Ai agents after this for doing our tasks,

#### n8n, Dify and Flowise AI
In this course what we will learn mostly is n8n, because of  it is open source and we can use in our local machine (not cloud). All the environment of three tools are graphic "drag and drop" env. n8n is much simpler in connecting to different APIs such as telegram, slack, email,.... It also has larger community (check all three githubs).

The license of other two are apache 2.0 but for n8n is sustainbale use license. If we want to make a chatbot + LLM , defy or flowise would be better. But not to forget all three needs zero or less coding compared to tools such as langchain,.... Those give us more freedom btw.


## chapter 3: LLM and propmt engineering

LLMs: A neural network with millions of parameters. 

The more sentences the LLM saw, the better they predict the next token not based on reasoning, That is why we are far from agentic world.

Token: each unit in the sentence where has to converted to a vector. Then based on the content the LLM saw and trained on, the words will be predicted with different probs.
And this sequence will continue. LLM does not understand of generated words, but If it has the reasoning ability, then it would create agentic world.

#### Challenges: 

- Hallucination
- Data dependency (garbage in, garbage out)
- Security 
- Privacy


What we want is to connect different tools and filesystems together and use LLMs(chatgpt) as the brain.
Chatgpt has this ability now.
AI agent will be our colleague or assistant, where it will 
1. learn pattern from data, 
2. generate new content,
3. categorize data and tasks and,
4. do smart follow up and remind.


The most updated LLMs now: 

- GPT (OpenAI) general applications.
- Gemini (Google) Better in research area and less biased good together with other google tools such as notebooKLM
- Grok (xAI) More social realtime events
- Claude Sonnet (Anthropic): Code developing
- DeepSeek Give lots of unnecessary info

Prompt engineering:
The best way to ask questions from LLMs. 

1) Ask clear question
2) Always check the output
3) No private data

Prompt is very important, because the generated text is based on our prompt. The prompt engineering is like ordering food in a restaurant.

prompt engineer tasks:

- Design smart prompts to get the best output from AI models
- test and improve prompts for increasing quality
- convert the customer need and applications to a meaningful prompt
- prompt documentation and make a library out of best prompts
- technical and non-technical collaboration for better promp designing


Good Prompt has:

1. What (e.g., write, summarize, suggest,...)
2. How (e.g., for who, official, friendly)
3. Limits (e.g., in less than 100 words, ..)

We can use some tools to convert the voice to text in our own language and this could be the prompt.
We can even ask the LLMs to give us a prompt.
Also we can ask for the edits in an image and upload the image with the prompt to the LLMs.

The course project for this chapter involved prompting an assistant by providing detailed information about the role, abilities, and preferred answer style. By modifying the details of the prompt, we were able to compare the outputs and explore how prompts can be shaped effectively, illustrating the principles of prompt engineering. The source files for this project are provided [here](src/Prompt_engineering_chapter/).







chapter 4: API and applications

chapter 5: Installation of n8n

chapter 6: RAG and VectorDB

chapter 7: projects


chapter 8: MCP and applications
