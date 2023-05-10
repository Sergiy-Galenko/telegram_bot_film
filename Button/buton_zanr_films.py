import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import vibor

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

def film(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == 'Фильмы':
        keyboard = [[InlineKeyboardButton("Комедії", callback_data='Комедії'), 
                    InlineKeyboardButton("Жахи", callback_data='Жахи')],
                    [InlineKeyboardButton("Драми", callback_data='Драми'), 
                    InlineKeyboardButton("Фантастика", callback_data='Фантастика')],
                    [InlineKeyboardButton("Трилери", callback_data='Трилери'), 
                    InlineKeyboardButton("Бойовики", callback_data='Бойовики')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Виберіть жанр фільму:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    genre = query.data
    query.edit_message_text(text=f"Ви обрали жанр: {genre}")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('film', film))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

#українські назви
historical_button = InlineKeyboardButton("Історичний", callback_data="historical")
action_button = InlineKeyboardButton("Бойовик", callback_data="action")
western_button = InlineKeyboardButton("Вестерн", callback_data="western")
military_button = InlineKeyboardButton("Військовий", callback_data="military")
detective_button = InlineKeyboardButton("Детектив", callback_data="detective")
documentary_button = InlineKeyboardButton("Документальний", callback_data="documentary")
drama_button = InlineKeyboardButton("Драма", callback_data="drama")
horror_button = InlineKeyboardButton("Жахи", callback_data="horror")
comedy_button = InlineKeyboardButton("Комедія", callback_data="comedy")
crime_button = InlineKeyboardButton("Кримінал", callback_data="crime")
melodrama_button = InlineKeyboardButton("Мелодрама", callback_data="melodrama")
music_button = InlineKeyboardButton("Музика", callback_data="music")
animation_button = InlineKeyboardButton("Мультфільм", callback_data="animation")
adventure_button = InlineKeyboardButton("Пригоди", callback_data="adventure")
family_button = InlineKeyboardButton("Сімейний", callback_data="family")
tv_movie_button = InlineKeyboardButton("Телефільм", callback_data="tv_movie")
thriller_button = InlineKeyboardButton("Трилер", callback_data="thriller")
fantastic_button = InlineKeyboardButton("Фантастика", callback_data="fantastic")
fantasy_button = InlineKeyboardButton("Фентезі", callback_data="fantasy")

#англійскі назви
action_button = InlineKeyboardButton("Action", callback_data="action")
adventure_button = InlineKeyboardButton("Adventure", callback_data="adventure")
animation_button = InlineKeyboardButton("Animation", callback_data="animation")
comedy_button = InlineKeyboardButton("Comedy", callback_data="comedy")
crime_button = InlineKeyboardButton("Crime", callback_data="crime")
documentary_button = InlineKeyboardButton("Documentary", callback_data="documentary")
drama_button = InlineKeyboardButton("Drama", callback_data="drama")
family_button = InlineKeyboardButton("Family", callback_data="family")
fantasy_button = InlineKeyboardButton("Fantasy", callback_data="fantasy")
history_button = InlineKeyboardButton("History", callback_data="history")
horror_button = InlineKeyboardButton("Horror", callback_data="horror")
music_button = InlineKeyboardButton("Music", callback_data="music")
mystery_button = InlineKeyboardButton("Mystery", callback_data="mystery")
romance_button = InlineKeyboardButton("Romance", callback_data="romance")
sf_button = InlineKeyboardButton("Science Fiction", callback_data="science_fiction")
tv_movie_button = InlineKeyboardButton("TV Movie", callback_data="tv_movie")
thriller_button = InlineKeyboardButton("Thriller", callback_data="thriller")
war_button = InlineKeyboardButton("War", callback_data="war")
western_button = InlineKeyboardButton("Western", callback_data="western")