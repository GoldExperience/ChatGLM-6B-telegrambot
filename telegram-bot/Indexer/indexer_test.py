from transformers import GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
# This is a long document we can split up.
with open('example_text.txt') as f:
    example_text = f.read()
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(example_text)

for text in texts:
    print(len(text))