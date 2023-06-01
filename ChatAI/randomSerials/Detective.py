import requests
import random

class TVSeries:
    BASE_URL = "https://api.themoviedb.org/3"
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"
    SERIES_BASE_URL = "https://www.themoviedb.org/tv"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_random_series(self, genre_id):
        random_series = random.choice(requests.get(f"{self.BASE_URL}/discover/tv?api_key={self.api_key}&with_genres={genre_id}").json()['results'])
        series_data = requests.get(f"{self.BASE_URL}/tv/{random_series['id']}?api_key={self.api_key}").json()

        return {
            'title': series_data['name'],
            'poster': f"{self.IMAGE_BASE_URL}{series_data['poster_path']}",
            'number_of_episodes': series_data['number_of_episodes'],
            'url': f"{self.SERIES_BASE_URL}/{random_series['id']}"
        }

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
tv_series = TVSeries(api_key)
series = tv_series.get_random_series(9648)  # 9648 is the genre id for detective series
if series:
    print(f"Title: {series['title']}\nPoster: {series['poster']}\nNumber of episodes: {series['number_of_episodes']}\nURL: {series['url']}")
