import requests
import random

class RandomHorrorSeries:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.themoviedb.org/3'
        self.image_base_url = 'https://image.tmdb.org/t/p/w500'
        self.tmdb_tv_show_url = 'https://www.themoviedb.org/tv/'
        self.genre_id = 9648  # ID для жанра ужасов

    def get_random_horror_series(self):
        page = random.randint(1, 500)  # Выбираем случайную страницу от 1 до 500
        discover_url = f'{self.base_url}/discover/tv?api_key={self.api_key}&with_genres={self.genre_id}&page={page}'

        response = requests.get(discover_url)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                random_show = random.choice(data['results'])
                show_id = random_show['id']
                show_title = random_show['name']
                show_rating = random_show['vote_average']
                show_poster_url = f"{self.image_base_url}{random_show['poster_path']}"
                show_page_url = f"{self.tmdb_tv_show_url}{show_id}"

                # Получение информации о сериале для подсчета количества эпизодов
                tv_show_url = f'{self.base_url}/tv/{show_id}?api_key={self.api_key}'
                tv_show_response = requests.get(tv_show_url)
                if tv_show_response.status_code == 200:
                    episode_count = sum([season['episode_count'] for season in tv_show_response.json()['seasons']])
                    print(f"Рандомный сериал из категории ужасов: {show_title}\n"
                          f"Рейтинг: {show_rating}\n"
                          f"Количество эпизодов: {episode_count}\n"
                          f"Ссылка на постер: {show_poster_url}\n"
                          f"Ссылка на сериал: {show_page_url}")
                else:
                    print("Не удалось получить информацию о сериале. Проверьте ваш API ключ и соединение.")
            else:
                print("Не удалось найти сериалы на данной странице. Попробуйте еще раз.")
        else:
            print("Не удалось получить данные от TMDb. Проверьте ваш API ключ и соединение.")

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
random_horror_series = RandomHorrorSeries(api_key)
random_horror_series.get_random_horror_series()
