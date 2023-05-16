import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import buton_zanr_anime, buton_zanr_films, buton_zanr_serials

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

class BotHandler:
    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('menu', self.menu))
        self.updater.dispatcher.add_handler(CallbackQueryHandler(self.button))

    def start(self) -> None:
        self.updater.start_polling()
        self.updater.idle()

    def help(self, update, context):
        update.message.reply_text("Використай команду /menu щоб визвати вікно з вибором того що ти хочеш подивитися.")

    def menu(self, update: Update, context: CallbackContext):
        keyboard = [[InlineKeyboardButton("Сериалы", callback_data='Сериалы'),
                     InlineKeyboardButton("Фильмы", callback_data='Фильмы'),
                    InlineKeyboardButton("Аниме", callback_data='Аниме')],
                    [InlineKeyboardButton("Фільм за описом", callback_data='Фільм за описом')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Выберите категорию:', reply_markup=reply_markup)

    def button(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        genre = query.data
        query.edit_message_text(text=f"Ви обрали жанр: {genre}")

if __name__ == '__main__':
    bot = BotHandler(TOKEN)
    bot.start()
