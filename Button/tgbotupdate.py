from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, CallbackContext, MessageHandler, Filters

import random

TOKEN = '5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo'

DEFAULT_LANG = 'en'

messages = {
    'en': {'hello': 'Hello!', 'change_lang': 'Change language'},
    'uk': {'hello': 'Привіт!', 'change_lang': 'Змінити мову'}
}

def get_keyboard():
    keyboard = [
        [InlineKeyboardButton("Change language", callback_data='change_lang')]
    ]
    return InlineKeyboardMarkup(keyboard)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(messages[DEFAULT_LANG]["hello"], reply_markup=get_keyboard())

def change_lang(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=messages[DEFAULT_LANG]['change_lang'], reply_markup=get_language_keyboard())

def select_language(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    global DEFAULT_LANG
    DEFAULT_LANG = query.data
    query.edit_message_text(text=messages[DEFAULT_LANG]['hello'], reply_markup=get_keyboard())

def get_language_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English", callback_data='en'),
            InlineKeyboardButton("🇺🇦 Українська", callback_data='uk')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(change_lang, pattern='^change_lang$'))
    dispatcher.add_handler(CallbackQueryHandler(select_language, pattern='^(en|uk)$'))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
