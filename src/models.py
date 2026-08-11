from pydantic import BaseModel

# BaseModel gives structured objects with validation; typed structured models
class Document(BaseModel):
    text: str
    source: str

class Chunk(BaseModel):
    chunk_id: int
    text: str
    source: str

class EmbeddedChunk(BaseModel):
    chunk_id: int
    text: str
    source: str
    embedding: list[float]
