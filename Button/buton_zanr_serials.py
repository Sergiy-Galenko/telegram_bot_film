import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import vibor

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

def serials(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Комедії", callback_data='Комедії'), 
                InlineKeyboardButton("Жахи", callback_data='Жахи')],
                [InlineKeyboardButton("Драми", callback_data='Драми'), 
                InlineKeyboardButton("Фантастика", callback_data='Фантастика')],
                [InlineKeyboardButton("Трилери", callback_data='Трилери'), 
                InlineKeyboardButton("Бойовики", callback_data='Бойовики')]]

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

# українські назви
western_button = InlineKeyboardButton("Вестерн", callback_data="western")
detective_button = InlineKeyboardButton("Детектив", callback_data="detective")
children_button = InlineKeyboardButton("Дитячий", callback_data="children")
documentary_button = InlineKeyboardButton("Документальний", callback_data="documentary")
drama_button = InlineKeyboardButton("Драма", callback_data="drama")
action_adventure_button = InlineKeyboardButton("Екшн і Пригоди", callback_data="action_adventure")
comedy_button = InlineKeyboardButton("Комедія", callback_data="comedy")
crime_button = InlineKeyboardButton("Кримінал", callback_data="crime")
soap_opera_button = InlineKeyboardButton("Мильна опера", callback_data="soap_opera")
animation_button = InlineKeyboardButton("Мультфільм", callback_data="animation")
sci_fi_button = InlineKeyboardButton("Науково фантастичний", callback_data="sci_fi")
news_button = InlineKeyboardButton("Новини", callback_data="news")
politics_war_button = InlineKeyboardButton("Політика та війна", callback_data="politics_war")
reality_show_button = InlineKeyboardButton("Реаліті-шоу", callback_data="reality_show")
family_button = InlineKeyboardButton("Сімейний", callback_data="family")
talk_show_button = InlineKeyboardButton("Ток-шоу", callback_data="talk_show")

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