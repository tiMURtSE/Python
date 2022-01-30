import telebot
import pymorphy2


bot = telebot.TeleBot("5045863537:AAGf4gRFE4QKOqsSmdg2xJsHWwNeHPv0qpw")

def text_analysis(text):
    # количество предложений
    number_of_sentences = text.count('.') + text.count('!') + text.count('?')
    
    
    # удаление союзов и предлогов
    def pos(word, morth=pymorphy2.MorphAnalyzer()):
        return morth.parse(word)[0].tag.POS

    words = text.split()
    functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}  # function words
    text = ([word for word in words if pos(word) not in functors_pos])
    
    
    # удаление символов и пустых элементов
    for i in range(len(text)):
        for char in text[i]:
            if char in ",.?/<>:;\'\"«»{[]}|!@#$%^&*()_+=–—":
                text[i] = text[i].replace(char, "")    
    text = [i for i in text if i != ""]
    
    
    # количество уникальных слов
    unique_words = set(text)
    
    
    # самые частые слова
    max_amount = 0
    word_amount = ""
    for i in range(len(text)):
        text[i] = text[i].lower()
        counter = text.count(text[i])
        if counter > max_amount:
            max_amount = counter
            word_amount = text[i]


    return f"Количество уникальных слов: {len(unique_words)}.\n\
Самое популярное слова: \"{word_amount}\", количество: {max_amount}.\n\
Количество предложений: {number_of_sentences}."


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Напиши текст для анализа.")


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, text_analysis(message.text))


bot.polling(none_stop=True, interval=0)

