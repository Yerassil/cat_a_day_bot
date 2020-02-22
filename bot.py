from telebot.types import ReplyKeyboardMarkup
import requests
import telebot
import config


url = 'https://api.thecatapi.com/v1/images/search?mime_type=jpg'
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(True, False)
    markup.row('Get a cat')
    bot.send_message(
        message.chat.id,
        'Hi! Click the button below',
        reply_markup=markup)


@bot.message_handler(regexp='Get a cat')
def cat(message):
    response = requests.get(url)
    data = response.json()
    cat = data[0]['url']

    bot.send_photo(message.chat.id, cat)


bot.polling(none_stop=True)
