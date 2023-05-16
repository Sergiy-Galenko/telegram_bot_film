import requests
import random

class SeriesFetcher:
    BASE_URL = "https://api.themoviedb.org/3"
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
    SERIES_BASE_URL = "https://www.themoviedb.org/tv"

    def __init__(self, api_key, genre_id):
        self.api_key = api_key
        self.genre_id = genre_id

    def get_random_series(self):
        page = random.randint(1, 500)
        discover_url = f"{self.BASE_URL}/discover/tv?api_key={self.api_key}&with_genres={self.genre_id}&page={page}"

        response = requests.get(discover_url)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                random_show = random.choice(data['results'])
                show_id = random_show['id']

                tv_show_url = f"{self.BASE_URL}/tv/{show_id}?api_key={self.api_key}"
                tv_show_response = requests.get(tv_show_url)
                if tv_show_response.status_code == 200:
                    episode_count = sum([season['episode_count'] for season in tv_show_response.json()['seasons']])
                    return {
                        'title': random_show['name'],
                        'rating': random_show['vote_average'],
                        'episode_count': episode_count,
                        'poster_url': f"{self.IMAGE_BASE_URL}{random_show['poster_path']}",
                        'show_url': f"{self.SERIES_BASE_URL}{show_id}"
                    }
        return None

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
genre_id = 10765  # ID для жанра фантастики

fetcher = SeriesFetcher(api_key, genre_id)
series = fetcher.get_random_series()

if series:
    print(f"Рандомный сериал из категории фантастики: {series['title']}\n"
          f"Рейтинг: {series['rating']}\n"
          f"Количество эпизодов: {series['episode_count']}\n"
          f"Ссылка на постер: {series['poster_url']}\n"
          f"Ссылка на сериал: {series['show_url']}")
else:
    print("Не удалось получить данные от TMDb. Проверьте ваш API ключ и соединение.")
