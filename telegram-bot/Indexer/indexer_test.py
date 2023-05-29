from transformers import GPT2TokenizerFast
from langchain.text_splitter import CharacterTextSplitter
from transformers import AutoTokenizer
import sys

chunk_size = sys.argv[0]

def countToken(input_string,tokenizer):
    tokens = tokenizer.tokenize(input_string)
    return(len(tokens))

# tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")

# This is a long document we can split up.
with open('example_text.txt') as f:
    example_text = f.read()
text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=chunk_size, chunk_overlap=0)
texts = text_splitter.split_text(example_text)

for text in texts:
    print("lenth of string",len(text))
    print("token of string",countToken(text,tokenizer))