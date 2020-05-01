import unittest
import bot
import telebot
from telebot import types
import time


class TestWholeBot(unittest.TestCase):

    @staticmethod
    def create_text_message(text):
        params = {'text': text}
        chat = types.User(11, False, 'test')
        return types.Message(1, None, None, chat, 'text', params, "")

    def test_find_at(self):
        """
        Test to find @ in a sentence
        """
        message = "@python"
        result = bot.find_at(message)
        self.assertEqual(result, "@")

    def test_send_welcome(self):
        """:return
        """
        tb = telebot.TeleBot('')
        msg = self.create_text_message('/start')

        @tb.message_handler(commands=['help', 'start'])
        def command_handler(message):
            message.text = 'got'

        tb.process_new_messages([msg])
        time.sleep(1)
        self.assertEqual(msg.text, 'got')

    def test_at_answer(self):
        tb = telebot.TeleBot('')
        msg = self.create_text_message(r'@python')

        @tb.message_handler(
            func=lambda
            message: message.text is not None and "@" in message.text)
        def at_answer(message):
            texts = message.text.split()
            at_text = bot.find_at(texts)
            return at_text

        tb.process_new_messages([msg])
        time.sleep(1)
        self.assertEqual(msg.text, '@python')


if __name__ == '__main__':
    unittest.main()
