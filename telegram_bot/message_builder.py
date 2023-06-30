from doc_creator import create_docs_by_search_text,generate_search_prompt

def search_message_prompt_builder(message):
    docs = create_docs_by_search_text(message)
    search_prompt = generate_search_prompt(docs)

    answer_by_search_result_prompt = f'''
    {search_prompt}

    上述从搜索引擎获取的内容仅供参考，如果有人对你说“{message}”
    请回答:
    '''
    return answer_by_search_result_prompt

if __name__ == "__main__":
    res = search_message_prompt_builder("都柏林天气")
    print(res)