import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import vibor

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

def anime(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Кодомо", callback_data="kodomo"),
                 InlineKeyboardButton("Сьодзьо", callback_data="shoujo")],
                 [InlineKeyboardButton("Дзьосэй", callback_data="josei"),
                InlineKeyboardButton("Сьонэн", callback_data="shonen")],
                [InlineKeyboardButton("Сэйнэн", callback_data="seinen"),
                InlineKeyboardButton("Традиційні жанри", callback_data="tradition")],
                [InlineKeyboardButton("Апокаліптика", callback_data="apocalyptic"),
                InlineKeyboardButton("Безумство", callback_data="madness")],
                [InlineKeyboardButton("Біопанк", callback_data="biopunk"),
                InlineKeyboardButton("Бойовик", callback_data="action")],
                [InlineKeyboardButton("Бойові мистецтва", callback_data="martial_arts"),
                InlineKeyboardButton("Вампіри", callback_data="vampire")],
                [InlineKeyboardButton("Військовий", callback_data="military"),
                InlineKeyboardButton("Гарем", callback_data="harem")],
                [InlineKeyboardButton("Демони", callback_data="demons"),
                InlineKeyboardButton("Детектив", callback_data="detective")],
                [InlineKeyboardButton("Добутсу", callback_data="doujinshi"),
                InlineKeyboardButton("Драма", callback_data="drama")],
                [InlineKeyboardButton("Ігри", callback_data="games"),
                InlineKeyboardButton("Ідоли", callback_data="idol")],
                [InlineKeyboardButton("Ікудзі", callback_data="ikuzi"),
                InlineKeyboardButton("Ісекай", callback_data="isekai")],
                [InlineKeyboardButton("Історичний", callback_data="historical"),
                InlineKeyboardButton("Кайто", callback_data="kaito")],
                [InlineKeyboardButton("Кіберпанк", callback_data="cyberpunk"),
                InlineKeyboardButton("Комедія", callback_data="comedy")],
                [InlineKeyboardButton("Космічна опера", callback_data="space_opera"),
                InlineKeyboardButton("Космос", callback_data="space")],
                [InlineKeyboardButton("Магія", callback_data="magic"),
                InlineKeyboardButton("Махо-сёдзё", callback_data="maho_shojo")],
                [InlineKeyboardButton("Машини", callback_data="machines"),
                InlineKeyboardButton("Меха", callback_data="mecha")],
                [InlineKeyboardButton("Містика", callback_data="mystic"),
                InlineKeyboardButton("Моє", callback_data="personal")],
                [InlineKeyboardButton("Музика", callback_data="music"),
                InlineKeyboardButton("Мильна опера", callback_data="soap_opera")],
                [InlineKeyboardButton("Отаку", callback_data="otaku"),
                InlineKeyboardButton("Парапсихологія", callback_data="parapsychology")],
                [InlineKeyboardButton("Пародія", callback_data="parody"),
                InlineKeyboardButton("Паропанк/Стімпанк", callback_data="steampunk")],
                [InlineKeyboardButton("Повсякденність", callback_data="slice_of_life"),
                InlineKeyboardButton("Поліцейський бойовик", callback_data="police_action")],
                [InlineKeyboardButton("Поліція", callback_data="police"),
                InlineKeyboardButton("Постапокаліптика", callback_data="post_apocalyptic")],
                [InlineKeyboardButton("Пригоди", callback_data="adventure"),
                InlineKeyboardButton("Психологічний", callback_data="psychological")],
                [InlineKeyboardButton("Психологічний трилер", callback_data="psychological_thriller"),
                InlineKeyboardButton("Реверс-гарем", callback_data="reverse_harem")],
                [InlineKeyboardButton("Романтика", callback_data="romance"),
                InlineKeyboardButton("Самураї", callback_data="samurai")],
                [InlineKeyboardButton("Самурайський бойовик", callback_data="samurai_action"),
                InlineKeyboardButton("Сверхприродне", callback_data="supernatural")],
                [InlineKeyboardButton("Сёдзё-ай", callback_data="shoujo_ai"),
                InlineKeyboardButton("Сёнэн-ай", callback_data="shounen_ai")],
                [InlineKeyboardButton("Казка", callback_data="fairy_tale"),
                InlineKeyboardButton("Спокон", callback_data="epic")],
                [InlineKeyboardButton("Сэнтай", callback_data="sentai"),
                InlineKeyboardButton("Токусацу", callback_data="tokusatsu")],
                [InlineKeyboardButton("Трилер", callback_data="thriller"),
                InlineKeyboardButton("Жахи", callback_data="horror")],
                [InlineKeyboardButton("Фантастика", callback_data="science_fiction"),
                InlineKeyboardButton("Фентезі", callback_data="fantasy")],
                [InlineKeyboardButton("Школа", callback_data="school"),
                InlineKeyboardButton("Шкільний детектив", callback_data="school_detective")],
                [InlineKeyboardButton("Екшн", callback_data="action")]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Виберіть жанр аніме:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    genre = query.data
    query.edit_message_text(text=f"Ви обрали жанр: {genre}")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('anime', anime))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

#англійскі назви
kodomo_button = InlineKeyboardButton("Kodomo", callback_data="kodomo")
shojo_button = InlineKeyboardButton("Shojo", callback_data="shojo")
josei_button = InlineKeyboardButton("Josei", callback_data="josei")
shonen_button = InlineKeyboardButton("Shonen", callback_data="shonen")
seinen_button = InlineKeyboardButton("Seinen", callback_data="seinen")
apocalyptic_button = InlineKeyboardButton("Apocalyptic", callback_data="apocalyptic")
madness_button = InlineKeyboardButton("Madness", callback_data="madness")
biopunk_button = InlineKeyboardButton("Biopunk", callback_data="biopunk")
action_button = InlineKeyboardButton("Action", callback_data="action")
fighting_art_button = InlineKeyboardButton("Fighting Art", callback_data="fighting_art")
vampires_button = InlineKeyboardButton("Vampires", callback_data="vampires")
military_button = InlineKeyboardButton("Military", callback_data="military")
harem_button = InlineKeyboardButton("Harem", callback_data="harem")
demon_button = InlineKeyboardButton("Demons", callback_data="demons")
detective_button = InlineKeyboardButton("Detective", callback_data="detective")
animal_button = InlineKeyboardButton("Animals", callback_data="animals")
drama_button = InlineKeyboardButton("Drama", callback_data="drama")
games_button = InlineKeyboardButton("Games", callback_data="games")
idol_button = InlineKeyboardButton("Idols", callback_data="idols")
ikuj_button = InlineKeyboardButton("Ikuji", callback_data="ikuj")
isekai_button = InlineKeyboardButton("Isekai", callback_data="isekai")
historical_button = InlineKeyboardButton("Historical", callback_data="historical")
kaito_button = InlineKeyboardButton("Kaito", callback_data="kaito")
cyberpunk_button = InlineKeyboardButton("Cyberpunk", callback_data="cyberpunk")
comedy_button = InlineKeyboardButton("Comedy", callback_data="comedy")
space_opera_button = InlineKeyboardButton("Space Opera", callback_data="space_opera")
space_button = InlineKeyboardButton("Space", callback_data="space")
magic_button = InlineKeyboardButton("Magic", callback_data="magic")
maho_shojo_button = InlineKeyboardButton("Maho-shojo", callback_data="maho_shojo")
cars_button = InlineKeyboardButton("Cars", callback_data="cars")
furs_button = InlineKeyboardButton("Furs", callback_data="furs")
mysticism_button = InlineKeyboardButton("Mysticism", callback_data="mysticism")
my_button = InlineKeyboardButton("My", callback_data="my")
music_button = InlineKeyboardButton("Music", callback_data="music")
military_opera_button = InlineKeyboardButton("Military Opera", callback_data="military_opera")
otaku_button = InlineKeyboardButton("Otaku", callback_data="otaku")
parapsychology_button = InlineKeyboardButton("Parapsychology", callback_data="parapsychology")
parody_button = InlineKeyboardButton("Parody", callback_data="parody")
steampunk_button = InlineKeyboardButton("Steampunk", callback_data="steampunk")
everyday_life_button = InlineKeyboardButton("Everyday Life", callback_data="everyday_life")
police_fighter_button = InlineKeyboardButton("Police Fighter", callback_data="police_fighter")
police_button = InlineKeyboardButton("Police", callback_data="police")
post_apocalyptic_button = InlineKeyboardButton("Post-apocalyptic", callback_data="post_apocalyptic")
slice_of_life_button = InlineKeyboardButton("Slice of Life", callback_data="slice_of_life")
psychological_button = InlineKeyboardButton("Psychological", callback_data="psychological")
psychological_thriller_button = InlineKeyboardButton("Psychological Thriller", callback_data="psychological_thriller")
reverse_harem_button = InlineKeyboardButton("Reverse Harem", callback_data="reverse_harem")
romance_button = InlineKeyboardButton("Romance", callback_data="romance")
samurai_button = InlineKeyboardButton("Samurai", callback_data="samurai")
samurai_fighter_button = InlineKeyboardButton("Samurai Fighter (Chambara)", callback_data="samurai_fighter")
supernatural_button = InlineKeyboardButton("Supernatural", callback_data="supernatural")
shojo_ai_button = InlineKeyboardButton("Shojo-ai", callback_data="shojo_ai")
shounen_ai_button = InlineKeyboardButton("Shounen-ai", callback_data="shounen_ai")
kazka_button = InlineKeyboardButton("Kazka", callback_data="kazka")
spokon_button = InlineKeyboardButton("Spokon", callback_data="spokon")
sentai_button = InlineKeyboardButton("Sentai", callback_data="sentai")
tokusatsu_button = InlineKeyboardButton("Tokusatsu", callback_data="tokusatsu")
thriller_button = InlineKeyboardButton("Thriller", callback_data="thriller")
crime_button = InlineKeyboardButton("Crime", callback_data="crime")
fantastic_button = InlineKeyboardButton("Fantastic", callback_data="fantastic")
fantasy_button = InlineKeyboardButton("Fantasy", callback_data="fantasy")
school_button = InlineKeyboardButton("School", callback_data="school")
school_detective_button = InlineKeyboardButton("School Detective", callback_data="school_detective")
action_button = InlineKeyboardButton("Action", callback_data="action")