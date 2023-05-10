import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import vibor

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

def film(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Комедії", callback_data='Comedies'), 
                InlineKeyboardButton("Жахи", callback_data='Horrors')],
                [InlineKeyboardButton("Драми", callback_data='Drami'), 
                InlineKeyboardButton("Фантастика", callback_data='Fantastic')],
                [InlineKeyboardButton("Трилери", callback_data='Trilery'), 
                InlineKeyboardButton("Бойовики", callback_data='fighters')]
                [InlineKeyboardButton("Історичний", callback_data="historical"), 
                InlineKeyboardButton("Бойовик", callback_data="action")]
                [InlineKeyboardButton("Вестерн", callback_data="western"),
                InlineKeyboardButton("Військовий", callback_data="military")]
                [InlineKeyboardButton("Детектив", callback_data="detective"),
                InlineKeyboardButton("Документальний", callback_data="documentary")]
                [InlineKeyboardButton("Драма", callback_data="drama"),
                InlineKeyboardButton("Жахи", callback_data="horror")]
                [InlineKeyboardButton("Комедія", callback_data="comedy"),
                InlineKeyboardButton("Кримінал", callback_data="crime")]
                [InlineKeyboardButton("Мелодрама", callback_data="melodrama"),
                InlineKeyboardButton("Музика", callback_data="music")]
                [InlineKeyboardButton("Мультфільм", callback_data="animation"),
                InlineKeyboardButton("Пригоди", callback_data="adventure")]
                [InlineKeyboardButton("Сімейний", callback_data="family"),
                InlineKeyboardButton("Телефільм", callback_data="tv_movie")]
                [InlineKeyboardButton("Трилер", callback_data="thriller"),
                InlineKeyboardButton("Фантастика", callback_data="fantastic")]
                [InlineKeyboardButton("Фентезі", callback_data="fantasy")]]

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