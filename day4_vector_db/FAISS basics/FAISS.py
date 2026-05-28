import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Documents
documents = [
    "Python is easy to learn",
    "AI is the future",
    "Deep learning uses neural networks"
]

# Create embeddings
embeddings = model.encode(documents)

# Convert to float32
embeddings = np.array(embeddings).astype("float32")

# Vector dimension
dimension = embeddings.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# Query
query = "What is artificial intelligence?"

query_embedding = model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

# Search
k = 2
distances, indices = index.search(query_embedding, k)

print("Indices:", indices)

print("\nRetrieved Documents:")
for i in indices[0]:
    print(documents[i])