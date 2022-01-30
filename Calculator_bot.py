import telebot
from telebot import types

bot = telebot.TeleBot("5045863537:AAGf4gRFE4QKOqsSmdg2xJsHWwNeHPv0qpw")
value = ""
old_value = ""


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я — бот-калькулятор! Могу че-нибудь считануть! ;)")


@bot.message_handler(commands=["calculator"])
def start(message):
    global value
    if value == "":
        bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


# кнопки по строкам
keyboard = types.InlineKeyboardMarkup()
keyboard.row(   types.InlineKeyboardButton(' ', callback_data = "no"),
                types.InlineKeyboardButton('C', callback_data = "C"),
                types.InlineKeyboardButton('⌫', callback_data = "<="),
                types.InlineKeyboardButton('÷', callback_data = "/"),  )

keyboard.row(   types.InlineKeyboardButton('7', callback_data = "7"),
                types.InlineKeyboardButton('8', callback_data = "8"),
                types.InlineKeyboardButton('9', callback_data = "9"),
                types.InlineKeyboardButton('×', callback_data = "*"),  )

keyboard.row(   types.InlineKeyboardButton('4', callback_data = "4"),
                types.InlineKeyboardButton('5', callback_data = "5"),
                types.InlineKeyboardButton('6', callback_data = "6"),
                types.InlineKeyboardButton('–', callback_data = "-"),  )

keyboard.row(   types.InlineKeyboardButton('1', callback_data = "1"),
                types.InlineKeyboardButton('2', callback_data = "2"),
                types.InlineKeyboardButton('3', callback_data = "3"),
                types.InlineKeyboardButton('+', callback_data = "+"),  )

keyboard.row(   types.InlineKeyboardButton(' ', callback_data = "no"),
                types.InlineKeyboardButton('0', callback_data = "0"),
                types.InlineKeyboardButton(',', callback_data = "."),
                types.InlineKeyboardButton('=', callback_data = "="),  )


# обработчик кнопок, подсчет
@bot.callback_query_handler(func=lambda call: True)
def callback(query):
    global value, old_value
    if query.data == "no":
        pass
    elif query.data == "C":
        value = ""
    elif query.data == "<=":
        if value != "":
            value = value[:-1]
    elif query.data == "=":
        try:
            value = str(eval(value))
        except Exception as e:
            value = "Ошибка! " + str(e)
    else:
        value += query.data


# надо
    if (value != old_value and value != "") or ("0" != old_value and value == ""):
        if value == "":
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="0", reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)


    old_value = value
    if value == "Ошибка!": 
        value = ""
   

bot.polling(none_stop=True, interval=0)