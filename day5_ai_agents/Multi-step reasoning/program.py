# Multi-step Reasoning with LangChain Agents
# pip install langchain openai

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.agents import AgentType
import math

# TOOL 1: Calculator

def calculator(expression):
    return eval(expression)

# TOOL 2: Word Counter

def word_counter(text):
    return f"Word count: {len(text.split())}"

# DEFINE TOOLS

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for solving math problems"
    ),
    
    Tool(
        name="WordCounter",
        func=word_counter,
        description="Counts words in text"
    )
]

# LLM

llm = ChatOpenAI(
    temperature=0,
    openai_api_key="YOUR_API_KEY"
)

# AGENT

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# USER QUERY

query = """
Calculate 25 * 8,
then count the words in:
'Artificial Intelligence is transforming industries'
"""

# RUN AGENT

response = agent.run(query)

print("\nFINAL RESPONSE:")
print(response)