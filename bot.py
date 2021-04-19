# -*- coding: utf-8 -*-
# import redis
import os
import telebot
import schedule
import time
import threading
import datetime
# import fileprocessor

class User:
    name=''
    birthdate=datetime.date.today()
    userid=''

#           Config vars
token = os.environ['TELEGRAM_TOKEN']

#       Your bot code below
bot = telebot.TeleBot(token)
user = User()
is_dialog_in_progress = False

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    print_start_dialog(message.chat.id)

def print_start_dialog(message_chat_id):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row('Зарегистрироваться')
    markup.row('Оформить подписку')
    markup.row('Узнать активации на эту неделю')
    markup.row('Помощь')
    markup.row('Связаться с нами')

    is_dialog_in_progress = True
    msg = bot.send_message(message_chat_id, 'Чем я могу вам помочь? В любой момент вы можете прервать диалог с помощью команды /end', reply_markup=markup)
    # print(message)

@bot.message_handler(commands=['end'])
def reser_dialog(message):
    user = User()
    is_dialog_in_progress = False
    bot.send_message(message.chat.id, 'Что бы снова начать диалог используейте команду /start')

@bot.message_handler(commands=['Зарегистрироваться','register'])
def register_name(message):
    if is_dialog_in_progress :
        user = User()
        msg = bot.send_message(message.chat.id, 'Введите свои ФИО')
        bot.register_next_step_handler(msg, register_save_name)

def register_save_name(message):
    user.name = datetime.datetime(message.text)
    msg = bot.send_message(message.chat.id, 'Введите дату рождения')
    bot.register_next_step_handler(msg, register_birthday)

def register_birthday(message):
    user.birthdate = datetime.date(message.text)
    user.userid = message.from_user.id
    bot.send_message(message.chat.id, 'Спасибо, {name}, вы успешно зарегистрированы с id {id}.'.format(name=user.name,id=user.userid))
    print_start_dialog(message.chat.id)

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

