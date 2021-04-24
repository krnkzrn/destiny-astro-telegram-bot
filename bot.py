# -*- coding: utf-8 -*-
# import redis
import os
import telebot
import schedule
import time
import threading
import datetime
import fileprocessor
import user

#           Config vars
token = os.environ['TELEGRAM_TOKEN']

#       Your bot code below
bot = telebot.TeleBot(token)
user = user.User()

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    print_start_dialog(message.chat.id)

def print_start_dialog(message_chat_id):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton('Test',callback_data='test'))
    markup.row(telebot.types.InlineKeyboardButton('Зарегистрироваться',callback_data='register'))
    markup.row(telebot.types.InlineKeyboardButton('Оформить подписку',callback_data='subscribe'))
    markup.row(telebot.types.InlineKeyboardButton('Узнать активации на эту неделю',callback_data='week_activations'))
    markup.row(telebot.types.InlineKeyboardButton('Помощь',callback_data='help'),
               telebot.types.InlineKeyboardButton('Связаться с нами',callback_data='contacts'))

    bot.send_message(message_chat_id, 'Чем я могу вам помочь? В любой момент вы можете прервать диалог с помощью команды /end', reply_markup=markup)
    # print(message)

@bot.message_handler(commands=['end'])
def reset_dialog(message):
    user.reset()
    bot.send_message(message.chat.id, 'Что бы снова начать диалог используейте команду /start')

@bot.callback_query_handler(func=lambda call:True)
def register_name(query):
    print(query)
    bot.answer_callback_query(query.id)
    if query.data == 'test':
        fileprocessor.print_all_clients()
    elif query.data == 'register':
        print("Query to register")
        user.reset()
        msg = bot.send_message(query.message.chat.id, 'Как к вам обращаться?')
        bot.register_next_step_handler(msg, register_save_name)
    elif query.data == 'subscribe':
        is_active = fileprocessor.is_client_active(query.from_user.id)
        bot.send_message(query.message.chat.id, 'У вас {ny}активная подписка'.format(ny=(is_active and '' or 'не ')))
    else:
        bot.send_message(query.message.chat.id, 'В разработке')

def register_save_name(message):
    print(message)
    user.name = message.text
    register_request_birthday(message)

def register_request_birthday(message):
    print(message)
    msg = bot.send_message(message.chat.id, 'Введите дату своего рождения (формат: дд.мм.гггг)')
    bot.register_next_step_handler(msg, register_birthday)

def register_birthday(message):
    print(message)
    try:
        user.birthdate = datetime.datetime.strptime(message.text,'%d.%m.%Y')
        user.userid = message.from_user.id
        user.active = True
        fileprocessor.add_client(user)
        fileprocessor.print_all_clients()
        bot.send_message(message.chat.id,
                         'Спасибо, {name}, вы успешно зарегистрированы с id {id}.'.format(name=user.name,
                                                                                          id=user.userid))
        print_start_dialog(message.chat.id)
    except ValueError:
            msg = bot.send_message(message.chat.id, 'Ошибка в дате рождения. Пожалуйста проверьте формат.')
            register_request_birthday(msg)

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
# job_thread = threading.Thread(target=job_threading())
# job_thread.start()

