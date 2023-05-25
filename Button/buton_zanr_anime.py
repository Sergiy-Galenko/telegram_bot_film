import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "5845703570:AAFlOF_HbqpJtWfrplzbpBIh0lpmCyucPHo"

class AnimeBotHandler:
    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('anime', self.anime))
        self.updater.dispatcher.add_handler(CallbackQueryHandler(self.button))

    def start(self) -> None:
        self.updater.start_polling()
        self.updater.idle()

    def anime(self, update: Update, context: CallbackContext) -> None:
        keyboard = [[InlineKeyboardButton("Кодомо", callback_data="Кодомо"),
                     InlineKeyboardButton("Сьодзьо", callback_data="Сьодзьо")],
                    [InlineKeyboardButton("Дзьосэй", callback_data="Дзьосэй"),
                     InlineKeyboardButton("Сьонэн", callback_data="Сьонэн")],
                    [InlineKeyboardButton("Сэйнэн", callback_data="Сэйнэн"),
                     InlineKeyboardButton("Традиційні жанри", callback_data="Традиційні жанри")],
                    [InlineKeyboardButton("Апокаліптика", callback_data="Апокаліптика"),
                     InlineKeyboardButton("Безумство", callback_data="Безумство")],
                    [InlineKeyboardButton("Біопанк", callback_data="Біопанк"),
                     InlineKeyboardButton("Бойовик", callback_data="Бойовик")],
                    [InlineKeyboardButton("Бойові мистецтва", callback_data="Бойові мистецтва"),
                     InlineKeyboardButton("Вампіри", callback_data="Вампіри")],
                    [InlineKeyboardButton("Військовий", callback_data="Військовий"),
                     InlineKeyboardButton("Гарем", callback_data="Гарем")],
                    [InlineKeyboardButton("Демони", callback_data="Демони"),
                     InlineKeyboardButton("Детектив", callback_data="Детектив")],
                    [InlineKeyboardButton("Добутсу", callback_data="Добутсу"),
                     InlineKeyboardButton("Драма", callback_data="Драма")],
                    [InlineKeyboardButton("Ігри", callback_data="Ігри"),
                     InlineKeyboardButton("Ідоли", callback_data="Ідоли")],
                    [InlineKeyboardButton("Ікудзі", callback_data="Ікудзі"),
                     InlineKeyboardButton("Ісекай", callback_data="Ісекай")],
                    [InlineKeyboardButton("Історичний", callback_data="Історичний"),
                     InlineKeyboardButton("Кайто", callback_data="Кайто")],
                    [InlineKeyboardButton("Кіберпанк", callback_data="Кіберпанк"),
                     InlineKeyboardButton("Комедія", callback_data="Комедія")],
                    [InlineKeyboardButton("Космічна опера", callback_data="Космічна опера"),
                     InlineKeyboardButton("Космос", callback_data="Космос")],
                    [InlineKeyboardButton("Магія", callback_data="Магія"),
                     InlineKeyboardButton("Махо-сёдзё", callback_data="Махо-сёдзё")],
                    [InlineKeyboardButton("Машини", callback_data="Машини"),
                     InlineKeyboardButton("Меха", callback_data="Меха")],
                    [InlineKeyboardButton("Містика", callback_data="Містика"),
                     InlineKeyboardButton("Моє", callback_data="Моє")],
                    [InlineKeyboardButton("Музика", callback_data="Музика"),
                     InlineKeyboardButton("Мильна опера", callback_data="Мильна опера")],
                    [InlineKeyboardButton("Отаку", callback_data="Отаку"),
                     InlineKeyboardButton("Парапсихологія", callback_data="Парапсихологія")],
                    [InlineKeyboardButton("Пародія", callback_data="Пародія"),
                     InlineKeyboardButton("Паропанк/Стімпанк", callback_data="Паропанк")],
                    [InlineKeyboardButton("Повсякденність", callback_data="Повсякденність"),
                     InlineKeyboardButton("Поліцейський бойовик", callback_data="Поліцейський бойовик")],
                    [InlineKeyboardButton("Поліція", callback_data="Поліція"),
                     InlineKeyboardButton("Постапокаліптика", callback_data="Постапокаліптика")],
                    [InlineKeyboardButton("Пригоди", callback_data="Пригоди"),
                     InlineKeyboardButton("Психологічний", callback_data="Психологічний")],
                    [InlineKeyboardButton("Психологічний трилер", callback_data="Психологічний трилер"),
                     InlineKeyboardButton("Реверс-гарем", callback_data="Реверс-гарем")],
                    [InlineKeyboardButton("Романтика", callback_data="Романтика"),
                     InlineKeyboardButton("Самураї", callback_data="Самураї")],
                    [InlineKeyboardButton("Самурайський бойовик", callback_data="Самурайський бойовик"),
                     InlineKeyboardButton("Сверхприродне", callback_data="Сверхприродне")],
                    [InlineKeyboardButton("Сёдзё-ай", callback_data="Сёдзё-ай"),
                     InlineKeyboardButton("Сёнэн-ай", callback_data="Сёнэн-ай")],
                    [InlineKeyboardButton("Казка", callback_data="Казка"),
                     InlineKeyboardButton("Спокон", callback_data="Спокон")],
                    [InlineKeyboardButton("Сэнтай", callback_data="Сэнтай"),
                     InlineKeyboardButton("Токусацу", callback_data="Токусацу")],
                    [InlineKeyboardButton("Трилер", callback_data="Трилер"),
                     InlineKeyboardButton("Жахи", callback_data="Жахи")],
                    [InlineKeyboardButton("Фантастика", callback_data="Фантастика"),
                     InlineKeyboardButton("Фентезі", callback_data="Фентезі")],
                    [InlineKeyboardButton("Школа", callback_data="Школа"),
                     InlineKeyboardButton("Шкільний детектив", callback_data="Шкільний детектив")],
                    [InlineKeyboardButton("Екшн", callback_data="Екшн")]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Виберіть жанр аніме:', reply_markup=reply_markup)

    def button(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        genre = query.data
        query.edit_message_text(text=f"Ви обрали жанр: {genre}")

    def main(self, anime, button):
        updater = Updater('5499590162:AAFyno0cbsJw12j_mfftTuX9dxebttvJPEM', use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('anime', anime))
        dp.add_handler(CallbackQueryHandler(button))
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    bot = AnimeBotHandler(TOKEN)
    bot.start()


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