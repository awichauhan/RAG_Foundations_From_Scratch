from src.ingested import load_document
from src.cleaner import clean_document
from src.chunker import chunk_document
from src.embedder import embed_chunks, embed_query

from src.vector_store import (
    create_collection,
    store_chunks,
    search_chunks
)


file_path = "/Users/awantikachauhan/PycharmProjects/RAG_Foundations_From_Scratch/src/data/sample_notes.txt"


# --------------------------------
# BUILD THE VECTOR DATABASE
# --------------------------------

document = load_document(file_path)

cleaned_document = clean_document(document)

chunks = chunk_document(cleaned_document)

embedded_chunks = embed_chunks(chunks)

vector_size = len(embedded_chunks[0].embedding)

create_collection(vector_size)

store_chunks(embedded_chunks)


# --------------------------------
# USER QUERY
# --------------------------------

query = "How are gradients calculated in a neural network?"

print("\nUSER QUERY:")
print(query)


# Convert the question into a vector.
query_embedding = embed_query(query)


# Search Qdrant.
results = search_chunks(
    query_embedding=query_embedding,
    limit=3
)


# --------------------------------
# DISPLAY RESULTS
# --------------------------------

print("\nSEARCH RESULTS:")

for result in results:

    print("\n-----------------------")

    print("Similarity score:")
    print(result.score)

    print("Text:")
    print(result.payload["text"])

    print("Source:")
    print(result.payload["source"])