from src.ingested import load_document
from src.cleaner import clean_document


file_path = "/Users/awantikachauhan/PycharmProjects/RAG_Foundations_From_Scratch/src/data/sample_notes.txt"

document = load_document(file_path)

cleaned_document = clean_document(document)

print("--------ORIGINAL DOCUMENT--------")
print(document.text)

print("\n----CLEANED_DOCUMENT----")
print(cleaned_document.text)


# file > Document > Clean document()  > cleaned document

