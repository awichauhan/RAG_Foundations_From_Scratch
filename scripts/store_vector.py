from src.ingested import load_document
from src.cleaner import clean_document
from src.chunker import chunk_document
from src.embedder import embed_chunks
from src.vector_store import create_collection, store_chunks

def main():
    file_path = "/Users/awantikachauhan/PycharmProjects/RAG_Foundations_From_Scratch/src/data/sample_notes.txt"


    document = load_document(file_path)

    cleaned_document = clean_document(document)

    chunks = chunk_document(cleaned_document)

    embedded_chunks = embed_chunks(chunks)


    # All our embeddings have the same dimension.
    vector_size = len(embedded_chunks[0].embedding)

    create_collection(vector_size)

    store_chunks(embedded_chunks)


    print("Chunks stored successfully!")

    print("Number of stored chunks:")
    print(len(embedded_chunks))


    #text > document > chunks > vectors > qdrant

main()