from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document


def divide_text_on_chunks(text):
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_text(text)
    return texts


def convert_chunks_to_document(splited_text):
    docs = [Document(page_content=t) for t in splited_text]
    return docs
