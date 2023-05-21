import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

class BotHandler:
    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('film', self.film))
        self.updater.dispatcher.add_handler(CallbackQueryHandler(self.button))

    def start(self):
        self.updater.start_polling()
        self.updater.idle()

    def film(self, update: Update, context: CallbackContext):
        genres = ['Комедії', 'Жахи', 'Драми', 'Фантастика', 'Трилери', 'Бойовики', 'Історичний',
                  'Вестерн', 'Військовий', 'Кримінал', 'Детектив', 'Документальний', 'Мелодрама',
                  'Музика', 'Мультфільм', 'Пригоди', 'Сімейний', 'Телефільм', 'Фентезі']

        keyboard = [[InlineKeyboardButton(genres[i], callback_data=genres[i]),
                     InlineKeyboardButton(genres[i + 1], callback_data=genres[i + 1])]
                    for i in range(0, len(genres), 2)]

        update.message.reply_text('Виберіть жанр фільму:', reply_markup=InlineKeyboardMarkup(keyboard))

    def button(self, update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text=f"Ви обрали жанр: {query.data}")

if __name__ == '__main__':
    BotHandler(TOKEN).start()



#англійскі назви
#action_button = InlineKeyboardButton("Action", callback_data="action")
#adventure_button = InlineKeyboardButton("Adventure", callback_data="adventure")
#animation_button = InlineKeyboardButton("Animation", callback_data="animation")
#comedy_button = InlineKeyboardButton("Comedy", callback_data="comedy")
#crime_button = InlineKeyboardButton("Crime", callback_data="crime")
#documentary_button = InlineKeyboardButton("Documentary", callback_data="documentary")
#drama_button = InlineKeyboardButton("Drama", callback_data="drama")
#family_button = InlineKeyboardButton("Family", callback_data="family")
#fantasy_button = InlineKeyboardButton("Fantasy", callback_data="fantasy")
#history_button = InlineKeyboardButton("History", callback_data="history")
#horror_button = InlineKeyboardButton("Horror", callback_data="horror")
#music_button = InlineKeyboardButton("Music", callback_data="music")
#mystery_button = InlineKeyboardButton("Mystery", callback_data="mystery")
#romance_button = InlineKeyboardButton("Romance", callback_data="romance")
#sf_button = InlineKeyboardButton("Science Fiction", callback_data="science_fiction")
#tv_movie_button = InlineKeyboardButton("TV Movie", callback_data="tv_movie")
#thriller_button = InlineKeyboardButton("Thriller", callback_data="thriller")
#war_button = InlineKeyboardButton("War", callback_data="war")
#western_button = InlineKeyboardButton("Western", callback_data="western")