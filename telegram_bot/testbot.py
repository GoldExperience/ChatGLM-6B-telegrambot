from transformers import AutoTokenizer, AutoModel
import os
import telebot
from message_builder import search_message_prompt_builder

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True).quantize(8).cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
# print(response)

def get_response(message):
	response, history = model.chat(tokenizer, message, history=[])
	return response


BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "你好，请问有什么可以帮到你？")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	search_message_prompt = search_message_prompt_builder(message.text)
	print(search_message_prompt)
	response = get_response(search_message_prompt)
	bot.reply_to(message, response)

bot.infinity_polling()
