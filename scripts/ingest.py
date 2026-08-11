
import data
from src.ingested import load_document

file_path = "/Users/awantikachauhan/PycharmProjects/RAG_Foundations_From_Scratch/src/data/sample_notes.txt"

document = load_document(file_path)

print("---DOCUMENT---")
print(document)

print("\n----SOURCE")
print(document.source)

print("\n----TEXT----")
print(type(document))

print("\n---OBJECT TYPE----")
print(type(document))