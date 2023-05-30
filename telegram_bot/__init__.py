from text_splitter import *
from chains.search_engine import duckduckgo

res = duckduckgo.search_text("where is dublin city university?")
for r in res:
    print(r)