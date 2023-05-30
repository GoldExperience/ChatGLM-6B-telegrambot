from duckduckgo_search import DDGS

def search_text(search_text, region='wt-wt'):
    result = []
    with DDGS() as ddgs:
        for r in ddgs.text(search_text, region=region, safesearch='Off', timelimit='y'):
            result.append(r)
    return result

def search_answer(search_text):
    result = []
    with DDGS() as ddgs:
        for r in ddgs.answers(search_text):
            result.append(r)
    return result
