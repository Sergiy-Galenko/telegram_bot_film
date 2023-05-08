from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

TOKEN = 'your_token_here'

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

def start(update, context):
    update.message.reply_text(messages[DEFAULT_LANG]["hello"], reply_markup=get_keyboard())

def change_lang(update, context):
    update.callback_query.message.edit_text(text=messages[DEFAULT_LANG]['change_lang'], reply_markup=get_language_keyboard())

def select_language(update, context):
    query = update.callback_query
    lang = query.data
    global DEFAULT_LANG
    DEFAULT_LANG = lang
    query.message.edit_text(text=messages[DEFAULT_LANG]['hello'], reply_markup=get_keyboard())

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
