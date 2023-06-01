from chains.search_engine import duckduckgo
from text_splitter import ChineseTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document

import os
import sys

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma


OPENAI_KEY = os.environ.get('OPENAI_KEY')
splitter = ChineseTextSplitter.ChineseTextSplitter()
embeddings = OpenAIEmbeddings()

def search_result_splitter(results):
    for res in results:
        split_results = text_splitter.split_text(res)


def doc_build(result):
        return Document(page_content=f"{result['title']},{result['body']}",metadata={'source':result['href']})

def create_docs_by_search(search_text):
    search_results = duckduckgo.search_text(search_text)
    docs = [doc_build(x) for x in search_results]
    db = Chroma.from_documents(docs, embeddings)
    docs = db.similarity_search_with_score(search_text)
    return docs

if __name__=="__main__":
    results = create_docs_by_search(sys.argv[1])
    for r in results:
        print(r)