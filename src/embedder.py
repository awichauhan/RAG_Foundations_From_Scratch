from sentence_transformers import SentenceTransformer
from src.config import EMBEDDING_MODEL
from src.models import EmbeddedChunk

model = SentenceTransformer(EMBEDDING_MODEL)

def embed_chunks(chunks):

    embedded_chunks = []
    for chunk in chunks:
        embedding = model.encode(chunk.text)

        embedding_list = embedding.tolist()

        embedded_chunk=EmbeddedChunk(
            chunk_id=chunk.chunk_id,
            text=chunk.text,
            source=chunk.source,
            embedding=embedding_list
        )

        embedded_chunks.append(embedded_chunk)

    return embedded_chunks

def embed_query(query):

    embedding = model.encode(query)

    return embedding.tolist()