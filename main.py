import logging
import gettext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Установите свой токен, который вы получили у BotFather
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


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

    query.edit_message_text(text=response_text)

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
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))
    dispatcher.add_handler(CommandHandler("language", language))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
