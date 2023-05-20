import dp as dp
from aiogram.bot import bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, MessageHandler
import random

TOKEN = '5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo'


DEFAULT_LANG = 'en'

messages = {
    'en': {'hello': 'Hello!', 'change_lang': 'Change language'},
    'uk': {'hello': 'Привіт!', 'change_lang': 'Змінити мову'}
}

#@dp.message_handler(content_types=['text'])
#dp.add_handler(CommandHandler('start', start))

def get_keyboard():
    keyboard = [
        [InlineKeyboardButton("Change language", callback_data='change_lang')]
    ]
    return InlineKeyboardMarkup(keyboard)

def start(update, context):
    pass

def change_lang(update, context):
    update.callback_query.message.edit_text(text=messages[DEFAULT_LANG]['change_lang'], reply_markup=get_language_keyboard())

def select_language(update, context):
    query = update.callback_query
    lang = query.data
    global DEFAULT_LANG
    DEFAULT_LANG = langІ
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


def find_film(name, year):
    pass

try:

    film = find_film(name='Название фильма', year='')
except Exception as e:
    bot.send_message(chat_id='ваш_chat_id', text='Произошла ошибка: {}'.format(str(e)))

# функция для обработки сообщения юзера
def count(update, context):
    # Получаем список всех подписчиков
    subscribers = bot.get_chat_members_count(chat_id=update.effective_chat.id)
    # Записываем количество подписчиков в текстовый файл
    with open('subscribers.txt', 'a') as file:
        file.write(f'Количество подписчиков: {subscribers}\n')

# функция с номером телефона
def phone_number(update, context):
    # получатель номер телефона
    phone_number = update.message.contact.phone_number
    # получатель имя юзера
    username = update.message.contact.first_name
    # счетчик нажатия кнопки подписаться
    registr = update.message.contact.registr
    # Записываем данные в текстовый файл
    with open('subscribers.txt', 'a') as file:
        file.write(f'{username}: {phone_number}\n')

# Конфигурация логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Словарь для хранения информации о пользователях
#users = {}


#def start(update, context):
 #   user_id = update.effective_user.id
  #  if user_id not in users:
        # Новый пользователь, сохраняем информацию
   #     users[user_id] = {
    #        'login': update.effective_user.username,
     #       'phone_number': update.effective_user.phone_number,
      #      'count': 1
       # }
    #else:
        # Повторное нажатие кнопки /start, увеличиваем счетчик
     #   users[user_id]['count'] += 1

    # Записываем информацию в файл
    #with open('log.txt', 'a') as file:
     #   file.write(f"Login: {users[user_id]['login']}, Phone number: {users[user_id]['phone_number']}, "
      #             f"Count: {users[user_id]['count']}\n")





