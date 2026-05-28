# OPEN AI EMBEDDINGS EXAMPLE

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="What is Retrieval-Augmented Generation?"
)

embedding = response.data[0].embedding

print("Embedding Length:", len(embedding))
print("\nFirst 10 Values:")
print(embedding[:10])



# Local Embeddings Example using Sentence Transformers

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Python is used for AI and machine learning.",
    "Football is a popular sport.",
    "RAG systems use embeddings for semantic search."
]

# Convert documents into embeddings
doc_embeddings = model.encode(documents)

# User query
query = "How does semantic search work in AI?"
# Query embedding
query_embedding = model.encode([query])

# Similarity search
similarities = cosine_similarity(query_embedding, doc_embeddings)

# Print results
for i, score in enumerate(similarities[0]):
    print(f"Document {i+1}: {score:.4f}")

# Most relevant document
best_match = similarities.argmax()

print("\nMost Relevant Document:")
print(documents[best_match])