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

#       Your bot code below
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row('Зарегистрироваться')
    markup.row('Оформить подписку')
    markup.row('Узнать активации на эту неделю')
    markup.row('Помощь')
    markup.row('Связаться с нами')

    msg = bot.send_message(message.chat.id, 'Здравствуйте, чем я могу вам помочь?', reply_markup=markup)
    print(message)

    bot.register_next_step_handler(msg)

@bot.message_handler(regexp=['Зарегистрироваться'])
def start_register(message):
    bot.send_message(message.chat.id, 'Введите свои фамилию')

def echoToChat():
    if os.environ['PUBLISH_UPDATES'] == 'TRUE':
        print('Sending update')
        bot.send_message(-543753474, 'Я тут буду публиковать всякие штуки')
    else:
        print('Updates are off')

def job_threading():
    schedule.every(5).minutes.do(echoToChat)
    while 1:
        schedule.run_pending()
        time.sleep(1)

bot.polling()
job_thread = threading.Thread(target=job_threading())
job_thread.start()

