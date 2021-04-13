# -*- coding: utf-8 -*-
# import redis
import os
import telebot
import schedule
import time
import threading
import fileprocessor

#           Config vars
token = os.environ['TELEGRAM_TOKEN']
publish_updates = os.environ['PUBLISH_UPDATES']

#       Your bot code below
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я стану умнее')
    print(message)

def echoToChat():
    bot.send_message(-543753474, 'Я тут буду публиковать всякие штуки')

def job_threading():
    if publish_updates == 'TRUE':
        schedule.every(5).minutes.do(echoToChat)
    while 1:
        schedule.run_pending()
        time.sleep(1)

job_thread = threading.Thread(target=job_threading())
job_thread.start()
print(token)
print(bot)
bot.polling()
