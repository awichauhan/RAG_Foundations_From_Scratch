from src.models import Chunk

def chunk_document(document):
    paragraph = document.text.split("\n\n")

    chunks = []
    for index,paragraph in enumerate(paragraph):
        if paragraph.strip() == "":
            continue

        chunk = Chunk(
            chunk_id = index,
            text = paragraph.strip(),
            source = document.source
        )

        chunks.append(chunk)

    return chunks

