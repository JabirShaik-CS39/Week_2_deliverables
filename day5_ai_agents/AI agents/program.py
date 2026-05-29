# Simple AI Agent Coding Example
# py -m pip install langchain openai

from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.llms import OpenAI

# Calculator Tool

def calculator(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

calc_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Useful for solving math problems"
)
# Load LLM

llm = OpenAI(
    temperature=0
)

# Create Agent

agent = initialize_agent(
    tools=[calc_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Run Agent

response = agent.run(
    "What is 45 * 12 + 100?"
)

print(response)