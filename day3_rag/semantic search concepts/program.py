from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Step 1: Sample Documents

documents = [
    "Python is a programming language",
    "Artificial Intelligence uses machine learning",
    "Football is a popular sport",
    "Deep learning is a subset of AI",
    "Cricket is played in many countries"
]

# Step 2: Load Embedding Model

model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 3: Convert Documents to Embeddings

doc_embeddings = model.encode(documents)

# Convert to float32
doc_embeddings = np.array(doc_embeddings).astype('float32')


# Step 4: Create FAISS Index

dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

# Add embeddings to index
index.add(doc_embeddings)


# Step 5: User Query

query = "What is AI?"

# Convert query to embedding
query_embedding = model.encode([query])

query_embedding = np.array(query_embedding).astype('float32')


# Step 6: Search Similar Documents

k = 2

distances, indices = index.search(query_embedding, k)


# Step 7: Show Results

print("\nQuery:", query)

print("\nTop Matching Documents:\n")

for i in indices[0]:
    print(documents[i])