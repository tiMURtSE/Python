import requests
import telebot

bot = telebot.TeleBot('5045863537:AAGf4gRFE4QKOqsSmdg2xJsHWwNeHPv0qpw')

def url_check(url):
    try:
        r = requests.get(url)
    except Exception:
        return "Такого адреса нет!"
    else:
        if r.status_code == 200:
            return True
        else:
            return False

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Прив, напиши url сайта, чтобы проверить его на доступность!!!")

@bot.message_handler(content_types=["text"])
def get_url(message):
    bot.send_message(message.chat.id, f"Проверка сайта {message.text} на доступность: {str(url_check(message.text))}")

bot.polling(none_stop=True, interval=0)