from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

TOKEN = '5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo'

DEFAULT_LANG = 'en'

messages = {
    'en': {'hello': 'Hello!', 'change_lang': 'Change language'},
    'uk': {'hello': 'Привіт!', 'change_lang': 'Змінити мову'}
}

def get_keyboard():
    keyboard = [
        [InlineKeyboardButton("Change language", callback_data='change_lang')]
    ]
    return InlineKeyboardMarkup(keyboard)

def start(update, context):
    update.message.reply_text(messages[DEFAULT_LANG]["hello"], reply_markup=get_keyboard())

def change_lang(update, context):
    update.callback_query.message.edit_text(text=messages[DEFAULT_LANG]['change_lang'], reply_markup=get_language_keyboard())

def select_language(update, context):
    query = update.callback_query
    lang = query.data
    global DEFAULT_LANG
    DEFAULT_LANG = lang
    query.message.edit_text(text=messages[DEFAULT_LANG]['hello'], reply_markup=get_keyboard())

def get_language_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English", callback_data='en'),
            InlineKeyboardButton("🇺🇦 Українська", callback_data='uk')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(change_lang, pattern='^change_lang$'))
    dispatcher.add_handler(CallbackQueryHandler(select_language, pattern='^(en|uk)$'))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

    def news(update, context):
        news_url = "https://example.com/news"
        message = "Останні оновлення бота".format(news_url)
        keyboard = [[InlineKeyboardButton("Читати", url=news_url)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text=message, reply_markup=reply_markup)

#_________Второй вариант кода_________
#def start(update, context):
 #   user_id = update.message.from_user.id
  #  language = get_user_language_from_database(user_id)
   # if not language:
     #   update.message.reply_text("Выберите язык:", reply_markup=ReplyKeyboardMarkup([["Английский", "Украинский"]]))
      #  return LANGUAGE
    #else:
      #  send_news(update, context, language)
       # return ConversationHandler.END

#def set_language(update, context):
 #   user_id = update.message.from_user.id
  #  language = update.message.text.lower()
   # save_user_language_to_database(user_id, language)
  #  send_news(update, context, language)
   # return ConversationHandler.END

#def send_news(update, context, language):
 #   if language == "английский":
  #      news_text = "Here are the latest news:"
   #     read_button_text = "Read"
    #    news_url = "ссылка"
   # elif language == "украинский":
     #   news_text = "Ось останні новини:"
     #   read_button_text = "Читати"
     #   news_url = "ссылка"
    #else:
    #   news_text = "Here are the latest news:"
     #   read_button_text = "Read"
      #  news_url = "ссылка"
#
 #   keyboard = [[InlineKeyboardButton(read_button_text, url=news_url)]]
  #  reply_markup = InlineKeyboardMarkup(keyboard)
   # update.message.reply_text(news_text, reply_markup=reply_markup)

#conv_handler = ConversationHandler(
 #   entry