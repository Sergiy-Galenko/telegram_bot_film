import requests
import time

TOKEN = ""
API_URL = f"https://api.telegram.org/bot{TOKEN}/"


def get_updates(offset=None):
    url = API_URL + "getUpdates?timeout=100"
    if offset:
        url += f"&offset={offset}"
    response = requests.get(url)
    return response.json()['result']


def send_message(chat_id, text, reply_markup=None):
    url = API_URL + "sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML',
        'reply_markup': reply_markup
    }
    response = requests.post(url, json=payload)
    return response.json()


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        for update in updates:
            if 'message' in update:
                chat_id = update['message']['chat']['id']
                message = update.get('message').get('text')

                if message == "/menu":
                    main_keyboard = {
                        "inline_keyboard": [
                            [{"text": "Сериалы", "callback_data": "Сериалы"},
                             {"text": "Фильмы", "callback_data": "Фильмы"},
                             {"text": "Аниме", "callback_data": "Аниме"}],
                            [{"text": "Фільм за описом", "callback_data": "Фільм за описом"}]
                        ]
                    }
                    send_message(chat_id, "Выберите категорию:", reply_markup=main_keyboard)
            elif 'callback_query' in update:
                query = update['callback_query']
                chat_id = query['message']['chat']['id']
                callback_data = query['data']

                if callback_data == 'Фильмы':
                    serials_keyboard = {
                        "inline_keyboard": [
                            [{"text": "Вестерн", "callback_data": "western"},
                             {"text": "Детектив", "callback_data": "detective"}],
                            [{"text": "Дитячий", "callback_data": "children"},
                             {"text": "Документальний", "callback_data": "documentary"}],
                            # ... add other options here in similar fashion
                        ]
                    }
                    send_message(chat_id, 'Виберіть жанр серіалу:', reply_markup=serials_keyboard)
                else:
                    send_message(chat_id, f"Ви обрали жанр: {callback_data}")

            last_update_id = update['update_id'] + 1

        time.sleep(1)


if __name__ == '__main__':
    main()
