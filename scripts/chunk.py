from src.ingested import load_document
from src.cleaner import clean_document
from src.chunker import chunk_document

file_path = "/Users/awantikachauhan/PycharmProjects/RAG_Foundations_From_Scratch/src/data/sample_notes.txt"

document = load_document(file_path)

cleaned_document = clean_document(document)

chunks = chunk_document(cleaned_document)

for chunk in chunks:
    print("\n-------------")

    print("Chunk_ID:")
    print(chunk.chunk_id)

    print("SOURCE:")
    print(chunk.source)

    print("TEXT:")
    print(chunk.text)
