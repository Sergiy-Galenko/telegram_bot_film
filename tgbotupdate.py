from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = 'your_token_here'

DEFAULT_LANG = 'en'

# Функция, которая будет вызываться при старте бота
def get_keyboard(messages):
    pass


def start(update, context, messages):
    # Отправляем приветственное сообщение на языке по умолчанию
    update.message.reply_text(messages[DEFAULT_LANG][""], reply_markup=get_keyboard(messages))

def change_lang(update, context, messages):

    update.callback_query.message.edit_text(text=messages[DEFAULT_LANG]['change_lang'], reply_markup=get_language_keyboard())

# Функция, которая будет вызываться при выборе языка из меню
def select_language(update, context, messages):

    query = update.callback_query
    lang = query.data

    # Обновляем язык по умолчанию
    global DEFAULT_LANG
    DEFAULT_LANG = lang

    # Отправляем сообщение на новом языке
    query.message.edit_text(text=messages[DEFAULT_LANG]['hello'], reply_markup=get_keyboard(messages))

# Функция для создания клавиатуры с выбором языка
def get_language_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English", callback_data='en'),
            InlineKeyboardButton("🇺🇦 Українська", callback_data='uk')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
