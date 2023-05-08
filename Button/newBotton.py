from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

# Обработчик команды "/start"
def start(update, context):
    # Создаем клавиатуру с двумя кнопками
    keyboard = [
        [InlineKeyboardButton("1", callback_data='1'),
         InlineKeyboardButton("2", callback_data='2')]
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
        query.message.reply_text('Привет')
    elif query.data == '2':
        query.message.reply_text('Пока')

# Основная функция
def main():
    # Создаем экземпляр Updater и передаем токен бота
    updater = Updater('YOUR_TOKEN_HERE', use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики команды /start и нажатия на кнопку
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
