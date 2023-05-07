import logging
import gettext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler

import requests
from requests.sessions import Session


# Set your Telegram bot token received from BotFather
TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

# Create a session object to use for requests
session = Session()


def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Оберіть мову", callback_data="button1"),
            InlineKeyboardButton("Кнопка 1", callback_data="button2"),
            InlineKeyboardButton("Кнопка 2", callback_data="button3"),
            InlineKeyboardButton("Аніме", callback_data="button4"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Виберіть кнопку:", reply_markup=reply_markup)


def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "button1":
        response_text = "Ви натиснули кнопку 1."
    elif query.data == "button2":
        response_text = "Ви натиснули кнопку 2."
    elif query.data == "button3":
        response_text = "Ви натиснули кнопку 3."
    elif query.data == "button4":
        response_text = "Ви натиснули кнопку Аніме."


def handle_text(update, context):
    # получаем текст сообщения от пользователя
    text = update.message.text
    # отправляем пользователю ответное сообщение
    update.message.reply_text(f"Вы написали: {text}")


def language(update: Update, context: CallbackContext):
    user = update.message.from_user

    lang_code = user.language_code

    lang = gettext.translation("messages", "locale", [lang_code], fallback=True)
    _ = lang.gettext

    lang_keyboard = [
        [
            InlineKeyboardButton("🇺🇸 English", callback_data="en"),
            InlineKeyboardButton("🇺🇦 Українська", callback_data="uk"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(lang_keyboard)
    update.message.reply_text(_("Оберіть мову:"), reply_markup=reply_markup)


def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))
    dispatcher.add_handler(CommandHandler("language", language))

    updater.start_polling()
    updater.idle()

import requests
import json

# Установите свой токен, который вы получили у BotFather
TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

# Определяем URL-адрес для отправки запросов к Telegram API
API_URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(chat_id, text, reply_markup=None):
    # Формируем параметры запроса к Telegram API для отправки сообщения
    params = {"chat_id": chat_id, "text": text}
    if reply_markup:
        params["reply_markup"] = json.dumps(reply_markup)

    # Отправляем запрос к Telegram API для отправки сообщения
    response = requests.post(API_URL + "sendMessage", json=params)

    # Возвращаем ответ в формате JSON
    return response.json()

def start(update):
    chat_id = update["message"]["chat"]["id"]
    keyboard = {
        "inline_keyboard": [[{"text": "Кнопка 1", "callback_data": "button1"},
                             {"text": "Кнопка 2", "callback_data": "button2"},
                             {"text": "Кнопка 3", "callback_data": "button3"}]]
    }
    reply_markup = json.dumps(keyboard)
    send_message(chat_id, "Выберите кнопку:", reply_markup)

def button_callback(update):
    chat_id = update["callback_query"]["message"]["chat"]["id"]
    query_id = update["callback_query"]["id"]
    button_data = update["callback_query"]["data"]

    if button_data == "button1":
        response_text = "Вы нажали кнопку 1."
    elif button_data == "button2":
        response_text = "Вы нажали кнопку 2."
    elif button_data == "button3":
        response_text = "Вы нажали кнопку 3."

    # Отправляем ответ на нажатие кнопки
    response = {"text": response_text, "callback_query_id": query_id}
    send_message(chat_id, json.dumps(response))

def get_updates(offset=None):
    # Формируем параметры запроса к Telegram API для получения обновлений
    params = {"timeout": 100, "offset": offset}

    # Отправляем запрос к Telegram API для получения обновлений
    response = requests.get(API_URL + "getUpdates", json=params)

    # Возвращаем ответ в формате JSON
    return response.json()

def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates["result"]:
            if "message" in update:
                start(update)
            elif "callback_query" in update:
                button_callback(update)
            offset = update["update_id"] + 1


if __name__ == "__main__":
    main()
