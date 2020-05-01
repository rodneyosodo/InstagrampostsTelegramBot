#!/usr/bin/env python3
import telebot
import time
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
bot_token = os.getenv("BOT_API_TOKEN")

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


if __name__ == "__main__":
    while True:
        try:
            bot.polling()
        except Exception as e:
            print(e)
            time.sleep(15)
