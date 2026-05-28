# app.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# STEP 1: Load PDF

loader = PyPDFLoader("sample.pdf")

documents = loader.load()

print(f"Loaded {len(documents)} pages")

# STEP 2: Chunking


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# STEP 3: Generate Embeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# STEP 4: Store in Vector DB

vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

# Save locally
vectorstore.save_local("faiss_index")

print("Ingestion completed successfully!")