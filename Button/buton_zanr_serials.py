import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import vibor

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

def serials(update: Update, context: CallbackContext) -> None:
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

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    genre = query.data
    query.edit_message_text(text=f"Ви обрали жанр: {genre}")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('serials', serials))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

#англійскі назви
western_button = InlineKeyboardButton("Western", callback_data="western")
detective_button = InlineKeyboardButton("Detective", callback_data="detective")
childish_button = InlineKeyboardButton("Childish", callback_data="childish")
documentary_button = InlineKeyboardButton("Documentary", callback_data="documentary")
drama_button = InlineKeyboardButton("Drama", callback_data="drama")
action_fit_button = InlineKeyboardButton("Action & Fit", callback_data="action_fit")
comedy_button = InlineKeyboardButton("Comedy", callback_data="comedy")
crime_button = InlineKeyboardButton("Crime", callback_data="crime")
milna_opera_button = InlineKeyboardButton("Milna opera", callback_data="milna_opera")
cartoon_button = InlineKeyboardButton("Cartoon", callback_data="cartoon")
science_fiction_button = InlineKeyboardButton("Science Fiction", callback_data="science_fiction")
news_button = InlineKeyboardButton("Novini", callback_data="news")
politics_war_button = InlineKeyboardButton("Politics and War", callback_data="politics_war")
reality_show_button = InlineKeyboardButton("Reality Show", callback_data="reality_show")
family_button = InlineKeyboardButton("Family", callback_data="family")
talk_show_button = InlineKeyboardButton("Talk Show", callback_data="talk_show")