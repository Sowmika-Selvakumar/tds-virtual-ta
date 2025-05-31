# qa_engine.py
from langchain.document_loaders import JSONLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def load_and_index_data():
    loader = JSONLoader(file_path="data/discourse_posts.json", jq_schema=".[] | {content: .title + \" \" + .excerpt}")
    documents = loader.load()
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(documents, embedding=embeddings, persist_directory="vector_store")
    return db

def get_answer(question):
    db = Chroma(persist_directory="vector_store", embedding_function=OpenAIEmbeddings())
    qa = RetrievalQA.from_chain_type(llm=OpenAI(model="gpt-3.5-turbo"), retriever=db.as_retriever())
    return qa.run(question)

