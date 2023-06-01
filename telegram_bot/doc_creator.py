from chains.search_engine import duckduckgo
from text_splitter import ChineseTextSpliter
import os
import sys

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma


OPENAI_KEY = os.environ.get('OPENAI_KEY')
text_splitter = ChineseTextSpliter


def search_result_splitter(results):
    for res in results:
        split_results = text_splitter.split_text(res)


def create_docs_by_search(search_text):
    results = duckduckgo.search_text(search_text)
    # results = [f"title:{x['title']},content{x['content']}" for x in results]

    return results

if __name__=="__main__":
    results = create_docs_by_search(sys.argv[1])
    for r in results:
        print(r)