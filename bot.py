import telebot
import time

from secret import bot_api_token 
bot_token = bot_api_token

bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
    for text in msg:
        if "@" in text:
            return text

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome!")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "To use this bot, send it a username")

@bot.message_handler(func=lambda msg: msg.text is not None and "@" in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
