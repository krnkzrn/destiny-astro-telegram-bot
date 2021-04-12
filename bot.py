# -*- coding: utf-8 -*-
# import redis
import os
import telebot

#           Config vars
token = os.environ['TELEGRAM_TOKEN']
# some_api_token = os.environ['SOME_API_TOKEN']

#       Your bot code below
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я стану умнее')


print(token)
print(bot)
bot.polling()
