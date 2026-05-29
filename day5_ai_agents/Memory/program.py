from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

# Create LLM
llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    temperature=0.7
)

# Create memory
memory = ConversationBufferMemory()

# Create conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Chat
response1 = conversation.predict(
    input="My name is Jabir"
)

print(response1)

response2 = conversation.predict(
    input="What is my name?"
)

print(response2)    

# Vector memory example

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Jabir likes Python",
    "AI agents use memory",
    "LangChain supports workflows"
]

vector_db = Chroma.from_texts(
    texts,
    embedding
)

query = "Who likes Python?"

results = vector_db.similarity_search(query)

print(results[0].page_content)