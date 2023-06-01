import requests, random

class SeriesFetcher:
    def __init__(self, api_key, genre_id):
        self.api_key, self.genre_id = api_key, genre_id

    def get_random_series(self):
        random_show = random.choice(requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key={self.api_key}&with_genres={self.genre_id}&page={random.randint(1, 500)}").json().get('results', []))
        if random_show:
            tv_show_response = requests.get(f"https://api.themoviedb.org/3/tv/{random_show['id']}?api_key={self.api_key}").json()
            return random_show['name'], random_show['vote_average'], sum([season['episode_count'] for season in tv_show_response['seasons']]), f"https://image.tmdb.org/t/p/w500{random_show['poster_path']}", f"https://www.themoviedb.org/tv{random_show['id']}"

api_key, genre_id = '5c45b86ac58a42d9cfc4d98bedca011d', 10765
series = SeriesFetcher(api_key, genre_id).get_random_series()

print(f"Рандомный сериал из категории фантастики: {series[0]}\nРейтинг: {series[1]}\nКоличество эпизодов: {series[2]}\nСсылка на постер: {series[3]}\nСсылка на сериал: {series[4]}" if series else "Не удалось получить данные от TMDb. Проверьте ваш API ключ и соединение.")
