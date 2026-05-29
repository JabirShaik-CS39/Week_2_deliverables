# LangChain Basics Example
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Create LLM
llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    model="gpt-4o-mini"
)

# Create Prompt
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms"
)

# Create Chain
chain = prompt | llm

# Run
response = chain.invoke({
    "topic": "AI Agents"
})

print(response.content)


# Explanation
#Part	                         Purpose
#Prompt Template	            Dynamic input
#LLM	                        Generates response
#Chain (`	                    `)
#invoke()	                    Executes workflow 