from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

def start(update, context):
    # Создаем клавиатуру с двумя кнопками
    keyboard = [
        [InlineKeyboardButton("1", callback_data='1'),
         InlineKeyboardButton("2", callback_data='2'),
         InlineKeyboardButton("Вибрати колір", callback_data='color')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с вариантами выбора
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

# Обработчик нажатия на кнопку
def button(update, context):
    query = update.callback_query
    query.answer()
    # Определяем, на какую кнопку нажал пользователь
    if query.data == '1':
        query.edit_message_text('Привет')
    elif query.data == '2':
        query.edit_message_text('Пока')
    elif query.data == 'color':
        color_keyboard = [[InlineKeyboardButton("Червоний", callback_data='red'),
                           InlineKeyboardButton("Синій", callback_data='blue')]]

        color_markup = InlineKeyboardMarkup(color_keyboard)

        query.edit_message_text('Виберіть колір:', reply_markup=color_markup)

def color_button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'red':
        query.edit_message_text('Ви вибрали червоний колір')
    elif query.data == 'blue':
        query.edit_message_text('Ви вибрали синій колір')

# Основная функция
def main():
    # Создаем экземпляр Updater и передаем токен бота
    updater = Updater('YOUR_TOKEN_HERE', use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики команды /start и нажатия на кнопку
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button, pattern='^(1|2|color)$'))
    dp.add_handler(CallbackQueryHandler(color_button, pattern='^(red|blue)$'))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
