from transformers import AutoTokenizer, AutoModel
import os
import telebot

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()
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
	response = get_response(message.text)
	bot.reply_to(message, response)

bot.infinity_polling()