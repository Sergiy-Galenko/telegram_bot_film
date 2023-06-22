import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

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

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    pass

@dp.callback_query_handler(text='change_lang')
async def change_lang(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages[DEFAULT_LANG]['change_lang'], reply_markup=get_language_keyboard())

@dp.callback_query_handler(lambda c: c.data and c.data in ['en', 'uk'])
async def select_language(call: types.CallbackQuery):
    global DEFAULT_LANG
    DEFAULT_LANG = call.data
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages[DEFAULT_LANG]['hello'], reply_markup=get_keyboard())

def get_language_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English", callback_data='en'),
            InlineKeyboardButton("🇺🇦 Українська", callback_data='uk')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()

@dp.message_handler(commands=['news'])
async def news(message: types.Message):
    news_url = "https://example.com/news"
    message = "Останні оновлення бота".format(news_url)
    keyboard = [[InlineKeyboardButton("Читати", url=news_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await bot.send_message(chat_id=message.chat.id, text=message, reply_markup=reply_markup)

def find_film(name, year):
    pass

@dp.message_handler(commands=['find_film'])
async def find_film_handler(message: types.Message):
    try:
        film = find_film(name='Название фильма', year='')
    except Exception as e:
        await bot.send_message(chat_id=message.chat.id, text='Произошла ошибка: {}'.format(str(e)))

@dp.message_handler(commands=['count'])
async def count(message: types.Message):
    subscribers = await bot.get_chat_members_count(chat_id=message.chat.id)
    with open('subscribers.txt', 'a') as file:
        file.write(f'Количество подписчиков: {subscribers}\n')

@dp.message_handler(content_types=['contact'])
async def phone_number(message: types.Message):
    phone_number = message.contact.phone_number
    username = message.contact.first_name
    with open('subscribers.txt', 'a') as file:
        file.write(f'{username}: {phone_number}\n')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)


"""
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
"""






