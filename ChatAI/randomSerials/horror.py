import requests
import random

class RandomTVSeries:
    def __init__(self, api_key, genre_id):
        self.api_key = api_key
        self.genre_id = genre_id
        self.base_url = 'https://api.themoviedb.org/3'
        self.image_base_url = 'https://image.tmdb.org/t/p/w500'
        self.tmdb_tv_show_url = 'https://www.themoviedb.org/tv/'

    def get_random_series(self):
        if (random_show := random.choice(requests.get(
                f'{self.base_url}/discover/tv?api_key={self.api_key}&with_genres={self.genre_id}&page={random.randint(1, 500)}'
            ).json().get('results', []))):
            tv_show_response = requests.get(
                f'{self.base_url}/tv/{random_show["id"]}?api_key={self.api_key}'
            ).json()
            print(f"""
            Рандомный сериал из категории {self.genre_id}: {random_show['name']}
            Рейтинг: {random_show['vote_average']}
            Количество эпизодов: {sum([season['episode_count'] for season in tv_show_response['seasons']])}
            Ссылка на постер: {self.image_base_url}{random_show['poster_path']}
            Ссылка на сериал: {self.tmdb_tv_show_url}{random_show['id']}
            """)
        else:
            print("Не удалось найти сериалы на данной странице. Попробуйте еще раз.")

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
genre_id = 9648  # ID для жанра ужасов
RandomTVSeries(api_key, genre_id).get_random_series()
