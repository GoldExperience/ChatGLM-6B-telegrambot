from transformers import AutoTokenizer, AutoModel
import os
import telebot

# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
# model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()
# model = model.eval()
# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
print(BOT_TOKEN)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()