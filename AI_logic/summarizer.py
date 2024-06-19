from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms import HuggingFaceHub


def divide_text_on_chunks(text):
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_text(text)
    return texts


def convert_chunks_to_document(text_input):
    splited_text = divide_text_on_chunks(text=text_input)
    docs = [Document(page_content=text) for text in splited_text]
    return docs


def load_llm():
    llm = HuggingFaceHub(repo_id='facebook/bart-large-cnn',
                         model_kwargs={'max_length': 512, 'temperature': 0.5}
                         )
    return llm


def chain_document(docs):
    llm = load_llm()
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.run(docs)


def run_summarizer(text_input):
    docs = convert_chunks_to_document(text_input=text_input)
    response = chain_document(docs)
    yield response


if __name__ == "__main__":
    input_text = input("Enter a sentence: ")
    for sentence in run_summarizer(input_text):
        print(sentence)
