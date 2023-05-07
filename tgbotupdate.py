import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

TOKEN = 'your_token_here'

DEFAULT_LANG = 'en'

bot = telegram.Bot(token=TOKEN)

# Функция, которая будет вызываться при старте бота
def start(update, context, massages=None):
    # Отправляем приветственное сообщение на языке по умолчанию
    update.message.reply_text(massages[DEFAULT_LANG][""], reply_markup=get_keyboard())

def change_lang(update, context, massages=None):
    # Отправляем меню с выбором языка
    update.callback_query.message.edit_text(text=massages[DEFAULT_LANG]['change_lang'], reply_markup=get_language_keyboard())

# Функция, которая будет вызываться при выборе языка из меню
def select_language(update, context, massages=None):
    # Получаем выбранный язык из callback_data
    query = update.callback_query
    lang = query.data

    # Обновляем язык по умолчанию
    global DEFAULT_LANG
    DEFAULT_LANG = lang

    # Отправляем сообщение на новом языке
    query.message.edit_text(text=massages[DEFAULT_LANG]['hello'], reply_markup=get_keyboard())

# Функция для создания клавиатуры с выбором языка
def get_language_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English", callback_data='en'),
            InlineKeyboardButton("🇺🇦 Українська", callback_data='uk')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# функция кнопки "змінити мову"
def get_keyboard(massages=None):
    keyboard = [[InlineKeyboardButton(massages[DEFAULT_LANG]['change_lang'], callback_data='change_lang')]]
    return InlineKeyboardMarkup(keyboard)

# функция интерфейса
def create_interface():
    # кнопка що нового
    keyboard = [[InlineKeyboardButton("Что нового?", url="https://example.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение в канал с кнопкой "Что нового"
    bot.send_message(chat_id="@MovieIntellect_bot", text="", reply_markup=reply_markup)

# Вызываем функцию для создания интерфейса пользователя
create_interface()

# Создаем экземпляр класса Updater и передаем ему токен
updater = Updater(TOKEN, use_context=True)

# регистр обработки команд
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(change_lang, pattern='change_lang'))
updater.dispatcher.add_handler(CallbackQueryHandler(select_language))

# цикл приема и обработки команд
updater.start_polling()
updater.idle
#131