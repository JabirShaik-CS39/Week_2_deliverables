import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create Chroma client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="my_docs")

# Documents
documents = [
    "Python is a programming language",
    "Artificial Intelligence is transforming the world",
    "Machine Learning is a subset of AI"
]

# Generate embeddings
embeddings = model.encode(documents).tolist()

# Store documents + embeddings
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=["1", "2", "3"]
)

# Query
query = "What is AI?"

query_embedding = model.encode([query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=2
)

print(results)