from transformers import GPT2TokenizerFast
from langchain.text_splitter import CharacterTextSplitter,TokenTextSplitter
from transformers import AutoTokenizer
import sys

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
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=100, chunk_overlap=0)


texts = text_splitter.split_text(example_text)



chinese_tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
for text in texts:
    print("="*20)
    print(text)
    print("lenth of string",len(text))
    print("token of string",countToken(text,chinese_tokenizer))