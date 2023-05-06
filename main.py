import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Встановіть свій токен, який вам надав BotFather
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Кнопка 1", callback_data="button1"),
            InlineKeyboardButton("Кнопка 2", callback_data="button2"),
            InlineKeyboardButton("Кнопка 3", callback_data="button3"),
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

    query.edit_message_text(text=response_text)

def main():
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
