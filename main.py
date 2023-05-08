import requests
from bs4 import BeautifulSoup

def get_movie_info(search_query):
    # Замените на URL сайта, с которым вы хотите работать
    base_url = 'https://rezka.ag/'
    search_url = f"{base_url}?q={search_query}"
    
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Замените на соответствующий селектор для названия фильма и изображения
        movie_title_selector = 'div.movie-title'
        movie_image_selector = 'img.movie-image'
        
        movie_title = soup.select_one(movie_title_selector)
        movie_image = soup.select_one(movie_image_selector)
        
        if movie_title and movie_image:
            return {
                'title': movie_title.text.strip(),
                'image': movie_image['src']
            }
        else:
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == '__main__':
    search_query = input('Введите название фильма: ')
    movie_info = get_movie_info(search_query)
    
    if movie_info:
        print(f"Название фильма: {movie_info['title']}")
        print(f"Картинка фильма: {movie_info['image']}")
    else:
        print("Фильм не найден.")
# Set your Telegram bot token received from BotFather
TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"


def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Select language", callback_data="button1"),
            InlineKeyboardButton("Button 1", callback_data="button2"),
            InlineKeyboardButton("Button 2", callback_data="button3"),
            InlineKeyboardButton("Anime", callback_data="button4"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose a button:", reply_markup=reply_markup)


def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "button1":
        lang_keyboard = [
            [
                InlineKeyboardButton("🇺🇸 English", callback_data="en"),
                InlineKeyboardButton("🇺🇦 Українська", callback_data="uk"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(lang_keyboard)
        query.edit_message_text(text="Choose a language:", reply_markup=reply_markup)
    elif query.data == "button2":
        response_text = "You pressed button 2."
        query.edit_message_text(text=response_text)
    elif query.data == "button3":
        response_text = "You pressed button 3."
        query.edit_message_text(text=response_text)
    elif query.data == "button4":
        response_text = "You pressed Anime."
        query.edit_message_text(text=response_text)


def language(update: Update, context: CallbackContext):
    user = update.message.from_user

    lang_code = user.language_code

    lang = gettext.translation("messages", "locale", [lang_code], fallback=True)
    _ = lang.gettext

    lang_keyboard = [
        [
            InlineKeyboardButton("🇺🇸 English", callback_data="en"),
            InlineKeyboardButton("🇺🇦 Українська", callback_data="uk"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(lang_keyboard)
    update.message.reply_text(_("Choose a language:"), reply_markup=reply_markup)


def main():
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))
    dispatcher.add_handler(CommandHandler("language", language))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
