import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

class BotHandler:
    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('serials', self.serials))
        self.updater.dispatcher.add_handler(CallbackQueryHandler(self.button))

    def start(self) -> None:
        self.updater.start_polling()
        self.updater.idle()

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

    def button(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        genre = query.data
        query.edit_message_text(text=f"Ви обрали жанр: {genre}")

if __name__ == '__main__':
    bot = BotHandler(TOKEN)
    bot.start()


#англійскі назви
#InlineKeyboardButton("Western", callback_data="western")
#InlineKeyboardButton("Detective", callback_data="detective")
#InlineKeyboardButton("Childish", callback_data="childish")
#InlineKeyboardButton("Documentary", callback_data="documentary")
#InlineKeyboardButton("Drama", callback_data="drama")
#InlineKeyboardButton("Action & Fit", callback_data="action_fit")
#InlineKeyboardButton("Comedy", callback_data="comedy")
#InlineKeyboardButton("Crime", callback_data="crime")
#InlineKeyboardButton("Milna opera", callback_data="milna_opera")
#InlineKeyboardButton("Cartoon", callback_data="cartoon")
#InlineKeyboardButton("Science Fiction", callback_data="science_fiction")
#InlineKeyboardButton("Novini", callback_data="news")
#InlineKeyboardButton("Politics and War", callback_data="politics_war")
#InlineKeyboardButton("Reality Show", callback_data="reality_show")
#InlineKeyboardButton("Family", callback_data="family")
#InlineKeyboardButton("Talk Show", callback_data="talk_show")