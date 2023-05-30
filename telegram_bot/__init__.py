from text_splitter import *
from chains.search_engine import duckduckgo

search_text = "都柏林城市大学在哪？"
res = duckduckgo.search_text(search_text)
for r in res:
    print(r)

print("="*20)

res = duckduckgo.search_answer(search_text)
for r in res:
    print(r)