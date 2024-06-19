from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms import HuggingFaceHub


class SimpleSummarizer:

    def __init__(self):
        self.chunk_size = 10
        self.chunk_overlap = 5
        self.max_length = 512
        self.temperature = 0.5
        self.repo_id = 'facebook/bart-large-cnn'

    def divide_text_on_chunks(self, text):
        text_splitter = CharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap)
        texts = text_splitter.split_text(text)
        return texts

    def convert_chunks_to_document(self, text_input):
        splited_text = self.divide_text_on_chunks(text=text_input)
        docs = [Document(page_content=text) for text in splited_text]
        return docs

    def load_llm(self):
        llm = HuggingFaceHub(
            repo_id=self.repo_id,
            model_kwargs={
                'max_length': self.max_length,
                'temperature': self.temperature})
        return llm

    def chain_document(self, docs):
        llm = self.load_llm()
        chain = load_summarize_chain(llm, chain_type='map_reduce')
        return chain.run(docs)

    def run_summarizer(self, text_input):
        docs = self.convert_chunks_to_document(text_input=text_input)
        response = self.chain_document(docs)
        yield response.strip()
