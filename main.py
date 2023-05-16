import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

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

        if genre == 'Фильмы':
            self.serials(update, context)  # if 'Фильмы' is chosen, show the serials menu
        else:
            query.edit_message_text(text=f"Ви обрали жанр: {genre}")

    def serials(self, update: Update, context: CallbackContext) -> None:
        keyboard = [[InlineKeyboardButton("Вестерн", callback_data="western"),
                    InlineKeyboardButton("Детектив", callback_data="detective")],
                    [InlineKeyboardButton("Дитячий", callback_data="children"),
                    InlineKeyboardButton("Документальний", callback_data="documentary")],
                    [InlineKeyboardButton("Драма", callback_data="drama"),
                    InlineKeyboardButton("Екшн і Пригоди", callback_data="action_adventure")],
                    [InlineKeyboardButton("Комедія", callback_data="comedy"),
                    InlineKeyboardButton("Кримінал", callback_data="crime")],
                    [InlineKeyboardButton("Мильна опера", callback_data="soap_opera"),
                    InlineKeyboardButton("Мультфільм", callback_data="animation")],
                    [InlineKeyboardButton("Науково фантастичний", callback_data="sci_fi"),
                    InlineKeyboardButton("Новини", callback_data="news")],
                    [InlineKeyboardButton("Політика та війна", callback_data="politics_war"),
                    InlineKeyboardButton("Реаліті-шоу", callback_data="reality_show")],
                    [InlineKeyboardButton("Сімейний", callback_data="family"),
                    InlineKeyboardButton("Ток-шоу", callback_data="talk_show")]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Виберіть жанр серіалу:', reply_markup=reply_markup)

if __name__ == '__main__':
    bot = BotHandler(TOKEN)
    bot.start()
