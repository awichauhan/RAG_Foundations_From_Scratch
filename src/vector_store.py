from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from src.config import QDRANT_COLLECTION_NAME


client = QdrantClient(":memory:")  # starts a local in-memory Qdrant database.

def create_collection(vector_size):
    client.create_collection(
        collection_name=QDRANT_COLLECTION_NAME,

        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE   #semantically similar
        )
    )

def store_chunks(embedded_chunks):
    points = []
    for chunk in embedded_chunks:
        point = PointStruct(  #Qdrant's object representing one database entry  (ID,VECTOR,PAYLOAD)
            id=chunk.chunk_id,

            vector=chunk.embedding,

            payload={   # payload is simply metadata attached to the vector.
                "text":chunk.text,
                "source": chunk.source,
                "chunk_id":chunk.chunk_id
            }
        )

        points.append(point)

    client.upsert(
        collection_name=QDRANT_COLLECTION_NAME,
        points=points
    )

def search_chunks(query_embedding,limit=3):
    results = client.query_points(
        collection_name=QDRANT_COLLECTION_NAME,
        query=query_embedding,
        limit=limit
    )
    return results.points