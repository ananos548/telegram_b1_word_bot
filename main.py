import telebot
from sqlalchemy import select
from sqlalchemy.orm import join

from database import session_maker
from telebot import types
import random
from models import Word, TranslatedWord
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Send random b1 english word")
    markup.row(btn)

    bot.send_message(message.chat.id, "Press the button to send a random b1 English word.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Send random b1 english word")
def send_random_pair(message):
    session = session_maker()
    query = select(Word.word, TranslatedWord.translated_word).select_from(join(Word, TranslatedWord)).where(
        TranslatedWord.word_id == Word.id)
    pairs = session.execute(query).fetchall()
    if pairs:
        pair = pairs[random.randint(0, len(pairs) - 1)]
        bot.send_message(message.chat.id, f"{pair[0]}, {pair[1]}")


bot.polling(none_stop=True)
