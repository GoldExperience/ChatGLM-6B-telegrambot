from chains.search_engine import duckduckgo
from text_splitter.ChineseTextSpliter import ChineseTextSpliter
import os
import sys

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma


OPENAI_KEY = os.environ.get('OPENAI_KEY')
splitter = ChineseTextSpliter.ChineseTextSpliter.split_text()


def search_result_splitter(results):
    for res in results:
        split_results = text_splitter.split_text(res)


def create_docs_by_search(search_text):
    search_results = duckduckgo.search_text(search_text)
    search_results = [f"{x['title']},{x['body']}" for x in search_results]
    
    results = []
    for r in search_results:
        r_splitted = splitter(r)
        results+=r_splitted

    return results

if __name__=="__main__":
    results = create_docs_by_search(sys.argv[1])
    for r in results:
        print(r)