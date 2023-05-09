import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

def anime(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Комедії", callback_data='Комедії'), 
                InlineKeyboardButton("Жахи", callback_data='Жахи')],
                [InlineKeyboardButton("Драми", callback_data='Драми'), 
                InlineKeyboardButton("Фантастика", callback_data='Фантастика')],
                [InlineKeyboardButton("Трилери", callback_data='Трилери'), 
                InlineKeyboardButton("Бойовики", callback_data='Бойовики')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Виберіть жанр аніме:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    genre = query.data
    query.edit_message_text(text=f"Ви обрали жанр: {genre}")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('anime', anime))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
