from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# STEP 1: Read PDF

reader = PdfReader("sample.pdf")

full_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        full_text += text + "\n"

print(full_text[:500])

# STEP 2: Split into Chunks

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(full_text)

print("\nTotal Chunks:", len(chunks))

# STEP 3: Create Embeddings

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

# STEP 4: Store in FAISS

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

print("\nEmbeddings stored successfully!")

# STEP 5: Query Search

query = "What is the document about?"

query_embedding = model.encode([query])

distances, indices = index.search(
    np.array(query_embedding),
    k=3
)

# STEP 6: Retrieve Results

print("\nTop Relevant Chunks:\n")

for idx in indices[0]:
    print(chunks[idx])
    print("\n----------------------\n")