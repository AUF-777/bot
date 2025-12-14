import time

import telebot, random

from telebot import TeleBot

#@luckbetterbot

token = '8578953696:AAGGkO0xLQ0YdFsXswJe8WYZRWSFxL2mgkg'

bot = telebot.TeleBot(token)


citat_stethem = [
    'Тебе не повезёт',
    'Сегодня будет плохой день',
    'Сегодня удача на твоей стороне',
    'Удача будет преследовать тебя'
]

citat_coin = [
    'Выпала - решка',
    'Выпал - орёл'
]

citat_mem = [
    '67',
    'Окак',
    'Бу испугался',
    'Чипи-чипи чапа-чапа',
    'Дикий огурец',
    'Мага сияй'
]

@bot.message_handler(commands=['mem'])
def mem(message):
    bot.send_message(message.chat.id, random.choice(citat_mem))

@bot.message_handler(commands=['password'])
def password(message):
    lenght = 12
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVNBM1234567890!@#$%^&*()'
    password = ''.join(random.sample(chars, lenght))
    bot.send_message(message.chat.id, f'Ваш пароль : {password}')

@bot.message_handler(commands=['cyb'])
def cyb(message):
    bot.send_dice(message.chat.id, emoji='🎲')

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.reply_to(message, "Пиши текстом.")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет.Я твой бот на векиииии.Напиши  /help  для список команд')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/start - приветстиве\n/help - список команд\n/mem - зачитование мем\n/coin - подкинуть монетку\n/cyb - бросить кубик\n/gada - гадание')


@bot.message_handler(commands=['gada'])
def citat(message):
    bot.send_message(message.chat.id, random.choice(citat_stethem))

@bot.message_handler(commands=['coin'])
def coin(message):
    bot.send_message(message.chat.id, random.choice(citat_coin))

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()
    if text == 'привет':
        bot.send_message(message.chat.id, 'Пппппппппррррррррриииииииииввввввввееееееееттттттт')



bot.polling()
