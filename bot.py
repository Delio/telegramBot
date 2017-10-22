# -*- coding: utf-8 -*-
import config
import telebot
import datetime
import requests
from telebot import types

bot = telebot.TeleBot(config.token)






greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()


# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    today = now.day
    hour = now.hour
    minute = now.minute
    #user = bot.get_me()
    if  today == now.day and 6 <= hour < 12:
        bot.send_message(message.chat.id, 'Доброе утро {}'.format(message.from_user.first_name))
    elif today == now.day and 12 <= hour < 18:
        bot.send_message(message.chat.id, 'Добрый день {}'.format(message.from_user.first_name))
    elif today == now.day and 18 <= hour < 23:
        bot.send_message(message.chat.id, 'Добрый вечер {}, какую информацию ты хочешь узнать? Найдены данные по: /ozerkovskaya и /koyashli'.format(message.from_user.first_name))
    elif today == now.day and 23 <= hour < 6:
        bot.send_message(message.chat.id, 'Доброй ночи {}'.format(message.from_user.first_name))
#    bot.send_message(message.chat.id, 'Сейчас 16 часов {}'.format(message.from_user.first_name))
    #        if hour == 16:
    #        bot.send_message(message.chat.id, 'Сейчас 16 часов {}'.format(message.from_user.first_name))

@bot.message_handler(commands=['ozerkovskaya'])
def ozerkovskaya(message):
    bot.send_message(message.chat.id, 'Напиши пин-код {}'.format(message.from_user.first_name))
    @bot.message_handler(regexp="1234")
    def handle_message(message):
    	bot.send_message(message.chat.id, 'Код верный {}'.format(message.from_user.first_name))

@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)




# Handles all text messages that match the regular expression
@bot.message_handler(regexp="test")
def handle_message(message):
	bot.send_message(message.chat.id, 'Не пиши больше ТЕСТ {}'.format(message.from_user.first_name))






#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#   bot.send_message(message.chat.id, message.text)


#@bot.message_handler(content_types=["text"])
#def default_test(message):
#    keyboard = types.InlineKeyboardMarkup()
#   url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
#   keyboard.add(url_button)
#    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
