import telebot
from sqlalchemy import select
from sqlalchemy.orm import join

from database import session_maker
from telebot import types
import random
from models import Word, TranslatedWord
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

all_pairs = []


@bot.message_handler(commands=['start'])
def start(message):
    global all_pairs
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Send random b1 english word")
    markup.row(btn)

    bot.send_message(message.chat.id, "Press the button to send a random b1 English word.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Send random b1 english word")
def send_random_pair(message):
    global all_pairs

    # Если список всех пар пуст или все пары были отправлены, перезаполняем его
    if not all_pairs:
        session = session_maker()
        query = select(Word.word, TranslatedWord.translated_word).select_from(join(Word, TranslatedWord)).where(
            TranslatedWord.word_id == Word.id)
        all_pairs = session.execute(query).fetchall()
        random.shuffle(all_pairs)  # Перемешиваем пары для случайного порядка
    if all_pairs:
        pair = all_pairs.pop()  # Извлекаем и удаляем пару из списка
        bot.send_message(message.chat.id, f"{pair[0]}, {pair[1]}")


bot.polling(none_stop=True)
