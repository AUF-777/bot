import telebot, random

from telebot import TeleBot

#@luckbetterbot

token = '8578953696:AAGGkO0xLQ0YdFsXswJe8WYZRWSFxL2mgkg'

bot = telebot.TeleBot(token)


citat_stethem = [
    'Только благодаря проблемам мы растём умственно и духовно. Именно через боль, возникающую при столкновении с проблемами и их разрешении, мы учимся',
    'В середине трудности кроется возможность',
    'Людям нужны тяжёлые времена и трудные испытания, чтобы развить мускулы души',
    'Если Бог хочет сделать тебя счастливым, то он ведёт тебя самой трудной дорогой, потому что лёгких путей к счастью не бывает',
    'Трудности порождают в человеке способности, необходимые для их преодоления'
]

citat_coin = [
    'решка',
    'орёл'
]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет.Я твой бот на векиииии.Напиши  /help  для список команд')





@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/start - приветстиве\n/help - список команд\n/citat - зачитование цитаты\n/coin - подкинуть монетку')


@bot.message_handler(commands=['citat'])
def citat(message):
    bot.send_message(message.chat.id, random.choice(citat_stethem))

@bot.message_handler(commands=['coin'])
def coin(message):
    bot.send_message(message.chat.id, 'Выпал : ' + random.choice(citat_coin))

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()
    if text == 'привет':
        bot.send_message(message.chat.id, 'Пппппппппррррррррриииииииииввввввввееееееееттттттт')


bot.polling()