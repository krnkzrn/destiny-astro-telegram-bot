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

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    print_start_dialog(message.chat.id)

def print_start_dialog(message_chat_id):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton('Зарегистрироваться',callback_data='register'))
    markup.row(telebot.types.InlineKeyboardButton('Оформить подписку',callback_data='subscribe'))
    markup.row(telebot.types.InlineKeyboardButton('Узнать активации на эту неделю',callback_data='week_activations'))
    markup.row(telebot.types.InlineKeyboardButton('Помощь',callback_data='help'),
               telebot.types.InlineKeyboardButton('Связаться с нами',callback_data='contacts'))

    bot.send_message(message_chat_id, 'Чем я могу вам помочь? В любой момент вы можете прервать диалог с помощью команды /end', reply_markup=markup)
    # print(message)

@bot.message_handler(commands=['end'])
def reset_dialog(message):
    user = User()
    bot.send_message(message.chat.id, 'Что бы снова начать диалог используейте команду /start')

@bot.callback_query_handler(func=lambda call:True)
def register_name(query):
    print("QUERY:")
    print(query)
    bot.answer_callback_query(query.id)
    if query.data == 'register':
        print("Query to register")
        user = User()
        msg = bot.send_message(query.message.chat.id, 'Введите свои ФИО')
        bot.register_next_step_handler(msg, register_save_name)

def register_save_name(message):
    user.name = message.text
    msg = bot.send_message(message.chat.id, 'Введите дату рождения')
    bot.register_next_step_handler(msg, register_birthday)

def register_birthday(message):
    user.birthdate = datetime.date(message.text)
    user.userid = message.from_user.id
    bot.send_message(message.chat.id, 'Спасибо, {name}, вы успешно зарегистрированы с id {id}.'.format(name=user.name,id=user.userid))
    print(user)
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

