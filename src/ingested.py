from pathlib import Path
from src.models import Document

def load_document(file_path):
    path = Path(file_path)  # creating object of file path so we can do operations like path.name
    # we could have directly passed "file_path" to open function

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

        # src = path.name  #we will use structure pydantic object (Document) instead of this

        document = Document(
            text = text,
            source = path.name
        )
        # return text, source
        return document

# file path > open() > file.read() > python string  #conventional way

# .txt file > read text > Document object (Pydantic data structure)

