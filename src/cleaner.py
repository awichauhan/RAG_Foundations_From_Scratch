import re  #regular expression
from src.models import Document

def clean_document(document):

    text = document.text

    text = text.strip()  # this could be just conventional way without using regex operations below

    text = re.sub(r"[ \t]+", " ", text)  # replacing multiple spaces/tabs with one space

    text = re.sub(r"\n{3,}", "\n\n", text) # replacing 3 or more line breaks with only 2

    cleaned_document = Document(
        text = text,
        source = document.source
    )

    return cleaned_document

