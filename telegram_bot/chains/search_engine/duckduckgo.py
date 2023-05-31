from duckduckgo_search import DDGS,ddg

def search_text(search_text):
    results = ddg(keywords, region='wt-wt', safesearch='Off', time='y')
    return results

# def search_text(search_text, region='wt-wt'):
#     result = []
#     with DDGS() as ddgs:
#         for r in ddgs.text(search_text, region=region, safesearch='Off', timelimit='y'):
#             result.append(r)
#     return result

def search_answer(search_text):
    result = []
    with DDGS() as ddgs:
        for r in ddgs.answers(search_text):
            result.append(r)
    return result
