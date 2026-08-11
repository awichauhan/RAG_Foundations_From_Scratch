from src.ingested import load_document
from src.cleaner import clean_document
from src.chunker import chunk_document
from src.embedder import embed_chunks

file_path = "/Users/awantikachauhan/PycharmProjects/RAG_Foundations_From_Scratch/src/data/sample_notes.txt"

document = load_document(file_path)

cleaned_document = clean_document(document)

chunk = chunk_document(cleaned_document)

embedded_chunks = embed_chunks(chunk)

for embedded_chunk in embedded_chunks:

    print("\n-----------")

    print("\n-----------------------")

    print("Chunk ID:")
    print(embedded_chunk.chunk_id)

    print("Text:")
    print(embedded_chunk.text)

    print("Embedding dimension:")
    print(len(embedded_chunk.embedding))

    print("First 5 values:")
    print(embedded_chunk.embedding[:5])


# Chunk text >> MiniLM >> 384 numbers
# The pretrained model maps semantically meaningful text into vector space
