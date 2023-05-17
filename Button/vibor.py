import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Import your SeriesFetcher class here
from series_fetcher import SeriesFetcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"
API_KEY = "5c45b86ac58a42d9cfc4d98bedca011d"

# Configure your genres and their IDs here
GENRES = {
    "Сериалы": 18,
    "Фильмы": 28,
    "Аниме": 16
}

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

<<<<<<< Updated upstream
    def menu(self, update: Update, context: CallbackContext):
        keyboard = [[InlineKeyboardButton("Сериалы", callback_data='Сериалы'),
                     InlineKeyboardButton("Фильмы", callback_data='Фильмы'),
                    InlineKeyboardButton("Аниме", callback_data='Аниме')],
                    [InlineKeyboardButton("Фільм за описом", callback_data='Фільм за описом')]]
=======
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    genre = query.data

    # Create a SeriesFetcher instance and get a random series
    fetcher = SeriesFetcher(API_KEY, GENRES[genre])
    series = fetcher.get_random_series()

    if series:
        result_text = f"Title: {series['title']}\nPoster: {series['poster']}\nNumber of episodes: {series['number_of_episodes']}\nURL: {series['url']}"
    else:
        result_text = "Не удалось найти сериал."

    query.edit_message_text(text=f"Ви обрали жанр: {genre}\n\n{result_text}")
>>>>>>> Stashed changes

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Выберите категорию:', reply_markup=reply_markup)

    def button(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        genre = query.data
        query.edit_message_text(text=f"Ви обрали жанр: {genre}")

if __name__ == '__main__':
<<<<<<< Updated upstream
    bot = BotHandler(TOKEN)
    bot.start()
=======
    main()
>>>>>>> Stashed changes
