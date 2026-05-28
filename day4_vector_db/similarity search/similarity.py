# similarity search using Basic Similarity Search
# pip install sentence-transformers scikit-learn

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Python is a programming language",
    "Cats are domestic animals",
    "Machine learning uses neural networks"
]

doc_embeddings = model.encode(documents)
query = "Artificial Intelligence and deep learning"
query_embedding = model.encode([query])

# Calculate similarity
similarities = cosine_similarity(query_embedding, doc_embeddings)

# Print similarity scores
print(similarities)

# Find best match
best_match = similarities.argmax()

print("\nBest Match:")
print(documents[best_match])




# similarity search using FAISS
# pip install faiss-cpu

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Documents
docs = [
    "Python programming",
    "Deep learning",
    "Cats and dogs"
]

# Embeddings
embeddings = model.encode(docs)

# Convert to float32
embeddings = np.array(embeddings).astype('float32')

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add vectors
index.add(embeddings)

# Query
query = "Artificial Intelligence"

query_vector = model.encode([query])
query_vector = np.array(query_vector).astype('float32')

# Search
k = 2
distances, indices = index.search(query_vector, k)

print(indices)
print(distances)

# Print results
for idx in indices[0]:
    print(docs[idx])