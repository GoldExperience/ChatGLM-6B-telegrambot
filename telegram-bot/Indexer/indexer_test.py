from transformers import GPT2TokenizerFast
from langchain.text_splitter import CharacterTextSplitter,TokenTextSplitter,RecursiveCharacterTextSplitter
from transformers import AutoTokenizer
import sys
import re

chunk_size = int(sys.argv[1])

def countToken(input_string,tokenizer):
    tokens = tokenizer.tokenize(input_string)
    return(len(tokens))


# This is a long document we can split up.
with open('example_text.txt') as f:
    example_text = f.read()

# bert-chinese tokenizer
# tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
# text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=chunk_size, chunk_overlap=0)

# token_based tokenizer
# text_splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=0)

# gpt2-tokenizer
# tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
# text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=chunk_size, chunk_overlap=0)

# tiktoken tokenizer
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=100, chunk_overlap=0)

# Recursive
# text_splitter = RecursiveCharacterTextSplitter(
#     # Set a really small chunk size, just to show.
#     chunk_size = chunk_size,
#     chunk_overlap  = 20,
#     length_function = len,
# )

def split_text(text, max_tokens=20):
    # 将文本按照句子的标点进行拆分
    sentences = re.split(r'[\n。，？！,.?!]', text)
    sentences = re.sub('([。！？\?])([^”’])', r"\1\n\2", sentences)  # 单字符断句符
    sentences = re.sub('(\.{6})([^”’])', r"\1\n\2", sentences)  # 英文省略号
    sentences = re.sub('(\…{2})([^”’])', r"\1\n\2", sentences)  # 中文省略号
    sentences = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', sentences)

    result = []

    for sentence in sentences:
        if sentence:
            # 删除前后的空白字符
            sentence = sentence.strip()
            # 计算中英文混合字符串的长度
            token_count = len(sentence) + sum(map(lambda x: x >= '\u4e00' and x <= '\u9fa5', sentence))
            # 将较长的句子进行再分割
            if token_count > max_tokens:
                result.extend(split_text(sentence[:max_tokens]) + split_text(sentence[max_tokens:], max_tokens))
            else:
                result.append(sentence)

    return result


# texts = text_splitter.split_text(example_text)
sys.setrecursionlimit(10000)
texts = split_text(example_text,max_tokens=chunk_size)


chinese_tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
for text in texts:
    print("="*20)
    print(text)
    print("lenth of string",len(text))
    print("token of string",countToken(text,chinese_tokenizer))