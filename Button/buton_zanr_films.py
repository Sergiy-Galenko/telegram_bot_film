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

    def film(self, update: Update, context: CallbackContext) -> None:
        keyboard = [[InlineKeyboardButton("Комедії", callback_data='Комедії'), 
                    InlineKeyboardButton("Жахи", callback_data='Жахи')],
                    [InlineKeyboardButton("Драми", callback_data='Драми'), 
                    InlineKeyboardButton("Фантастика", callback_data='Фантастика')],
                    [InlineKeyboardButton("Трилери", callback_data='Трилери'),
                    InlineKeyboardButton("Бойовики", callback_data='Бойовики')],
                    [InlineKeyboardButton("Історичний", callback_data="Історичний"), 
                    InlineKeyboardButton("Вестерн", callback_data="Вестерн")],
                    [InlineKeyboardButton("Військовий", callback_data="Військовий"),
                    InlineKeyboardButton("Кримінал", callback_data="Кримінал")],
                    [InlineKeyboardButton("Детектив", callback_data="Детектив"),
                    InlineKeyboardButton("Документальний", callback_data="Документальний")],
                    [InlineKeyboardButton("Мелодрама", callback_data="Мелодрама"),
                    InlineKeyboardButton("Музика", callback_data="Музика")],
                    [InlineKeyboardButton("Мультфільм", callback_data="Мультфільм"),
                    InlineKeyboardButton("Пригоди", callback_data="Пригоди")],
                    [InlineKeyboardButton("Сімейний", callback_data="Сімейний"),
                    InlineKeyboardButton("Телефільм", callback_data="Телефільм")],
                    [InlineKeyboardButton("Фентезі", callback_data="Фентезі")]]

        update.message.reply_text('Виберіть жанр фільму:', reply_markup=InlineKeyboardMarkup(keyboard))

    def button(self, update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text=f"Ви обрали жанр: {query.data}")

    def main(self, film, button):
        updater = Updater('5499590162:AAFyno0cbsJw12j_mfftTuX9dxebttvJPEM', use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('film', film))
        dp.add_handler(CallbackQueryHandler(button))
        updater.start_polling()
        updater.idle()

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