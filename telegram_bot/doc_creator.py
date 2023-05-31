from chains.search_engine import duckduckgo
from text_splitter import ChineseTextSpliter
import os
import sys

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma


OPENAI_KEY = os.environ.get('OPENAI_KEY')

def create_docs_by_search(search_text):
    result = duckduckgo.search_text(search_text)

    return result

if __name__=="__main__":
    result = create_docs_by_search(sys.argv[1])
    for r in result:
        print(r)