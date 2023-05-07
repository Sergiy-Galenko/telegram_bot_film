import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Встановлюємо рівень логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Задаємо токен вашого бота, отриманого від BotFather
TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

# Функція, що викликається при команді /start
def zanr(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Комедії", callback_data='Комедії'),
         InlineKeyboardButton("Жахи", callback_data='Жахи')],
        [InlineKeyboardButton("Драми", callback_data='Драми'),
         InlineKeyboardButton("Фантастика", callback_data='Фантастика')],
        [InlineKeyboardButton("Трилери", callback_data='Трилери'),
         InlineKeyboardButton("Бойовики", callback_data='Бойовики')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Виберіть жанр фільму:', reply_markup=reply_markup)


# Функція, що викликається при натисканні на кнопки
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # Отримуємо текст кнопки, на яку натиснули
    genre = query.data

    # Відправляємо повідомлення про вибір жанру
    query.edit_message_text(text=f"Ви обрали жанр: {genre}")


def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    # Додаємо обробники команд та натискання кнопок
    updater.dispatcher.add_handler(CommandHandler('zanr', zanr))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Запускаємо бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
