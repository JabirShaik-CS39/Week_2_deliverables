# Chunking in Retrieval-Augmented Generation (RAG)

from langchain_text_splitter import RecursiveCharacterTextSplitter

text = """
Retrieval-Augmented Generation combines retrieval systems
with large language models. Documents are split into chunks.
Chunks are converted into embeddings and stored in vector databases.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

print("Generated Chunks:\n")

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    print("-" * 40)



# Manual Chunking
text = """
Artificial Intelligence is transforming healthcare.
Machine learning helps in diagnostics.
Deep learning improves image analysis.
"""

chunk_size = 50

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

for idx, chunk in enumerate(chunks):
    print(f"\nChunk {idx+1}:")
    print(chunk)



# Recursive Chunking Using LangChain
# pip install langchain
from langchain_text_splitter import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence is transforming healthcare.
Machine learning helps in diagnostics.
Deep learning improves image analysis.
RAG systems use embeddings and vector databases.
"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)


# Token-Based Chunking
# pip install tiktoken
import tiktoken

text = "Artificial Intelligence is transforming industries."

encoding = tiktoken.encoding_for_model("gpt-4")

tokens = encoding.encode(text)

print("Tokens:", tokens)
print("Token Count:", len(tokens))


# Chunking PDF Documents
# pip install pypdf langchain
from pypdf import PdfReader
from langchain_text_splitter import RecursiveCharacterTextSplitter

# Load PDF
reader = PdfReader("sample.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()


# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(text)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])