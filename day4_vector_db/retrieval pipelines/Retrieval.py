from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load document
loader = TextLoader("data.txt")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

# Create embeddings
embedding_model = HuggingFaceEmbeddings()

# Store in FAISS
db = FAISS.from_documents(chunks, embedding_model)

# User query
query = "Explain vector databases"

# Retrieve documents
results = db.similarity_search(query, k=3)

# Print retrieved chunks
for i, doc in enumerate(results):
    print(f"\nResult {i+1}:")
    print(doc.page_content)