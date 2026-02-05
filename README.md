### The final goal is to make a personal AI_agent using tools and python
chapter 1: Python

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





chapter 2: AI agent, chatbot, Agentic AI, and n8n

chapter 3: LLM and propmt engineering

chapter 4: API and applications

chapter 5: Installation of n8n

chapter 6: RAG and VectorDB

chapter 7: projects


chapter 8: MCP and applications