# newButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    keyboard = [[InlineKeyboardButton("1", callback_data='1'),
                 InlineKeyboardButton("2", callback_data='2')],
                [InlineKeyboardButton("Вибрати колір", callback_data='color')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == '1':
        query.message.reply_text('Привет')
    elif query.data == '2':
        query.message.reply_text('Пока')
    elif query.data == 'color':
        color_keyboard = [[InlineKeyboardButton("Червоний", callback_data='red'),
                           InlineKeyboardButton("Синій", callback_data='blue')]]

        color_markup = InlineKeyboardMarkup(color_keyboard)

        query.message.reply_text('Виберіть колір:', reply_markup=color_markup)

def color_button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'red':
        query.message.reply_text('Ви вибрали червоний колір')
    elif query.data == 'blue':
        query.message.reply_text('Ви вибрали синій колір')

def main():
    updater = Updater('TOKEN')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CallbackQueryHandler(color_button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
