import chromadb
from sentence_transformers import SentenceTransformer

# Initialize embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample documents
documents = [
    "Artificial Intelligence is powerful",
    "Machine learning enables prediction",
    "Deep learning uses neural networks"
]

# Generate embeddings
embeddings = embedding_model.encode(documents)

# Create ChromaDB client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="ai_docs")

# Store embeddings
collection.add(
    documents=documents,
    embeddings=embeddings.tolist(),
    ids=["1", "2", "3"]
)

print("Embeddings stored successfully!")