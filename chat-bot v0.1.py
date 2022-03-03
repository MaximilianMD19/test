import telebot
from telebot import types

bot = telebot.TeleBot('5107250105:AAGmEXjY-JZIEO9lJPToN2M4GI_ikwmU9Z0')

# /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Связь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Связь")
        exits = types.KeyboardButton("Отключиться")
        markup.add(btn1, btn2, btn3, back, exits)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("21")
        btn2 = types.KeyboardButton("Прислать анекдот")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)

    elif ms_text == "/21" or ms_text == "21":# ......................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        c = [6,7,8,9,10,11] * 4
        import random
        random.shuffle(c)
        count_k = 0
        btn1 = types.KeyboardButton("Вытащить карту")
        btn2 = types.KeyboardButton("Остановится")
        markup.add(btn1, btn2)
        bot.send_message(chat_id, text="Что будете делать?",reply_markup=markup)
        while True:
            if ms_text == "Вытащить карту":
                count_k += c[0]
                c.pop(0)
                bot.send_message(chat_id, text="Что будете делать?", reply_markup=markup)
            elif len(c)==0:
                bot.send_message(chat_id, text="Карт нет")
            elif ms_text == "":
                bot.polling(none_stop=True, interval=1)
            elif ms_text == "Остановится":
                bot.send_message(chat_id, text="Ок")
                break

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton("Нет")
        markup.add(btn1, btn2)
        if count_k > 21 or count_k < 21:
            bot.send_message(chat_id, text="Loser! Переиграть?", reply_markup=markup)
        elif count_k == 21:
            bot.send_message(chat_id, text="Win! Переиграть?", reply_markup=markup)

    elif ms_text == "Прислать анекдот":  # .............................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "WEB-камера":
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Управление":  # ...................................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Связь" or ms_text == "❓ Связь":  # ...............................................................
        bot.send_message(chat_id, "Автор: Полуновский Максимилиан")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/mBumblebee")
        key1.add(btn1)
        img = open('ddd.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    elif ms_text == "Отключиться":  # .................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться")
        markup.add(btn1)
        bot.send_message(chat_id, text="Пока :3 ", reply_markup=markup)

    elif ms_text == "Вернуться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Главное меню")
        btn2 = types.KeyboardButton("❓ Связь")
        markup.add(btn1, btn2)
        bot.send_message(chat_id, text="C Возвращением) ", reply_markup=markup)

    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

bot.polling(none_stop=True, interval=0)
print()
