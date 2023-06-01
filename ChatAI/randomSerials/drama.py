import requests
import random

class SeriesFetcher:
    BASE_URL = "https://api.themoviedb.org/3"
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"
    SERIES_BASE_URL = "https://www.themoviedb.org/tv"

    def __init__(self, api_key, genre):
        self.api_key = api_key
        self.genre = genre

    def get_random_series(self):
        random_series = random.choice(requests.get(f"{self.BASE_URL}/discover/tv?api_key={self.api_key}&with_genres={self.genre}").json()['results'])
        series_data = requests.get(f"{self.BASE_URL}/tv/{random_series['id']}?api_key={self.api_key}").json()
        return {
            'title': series_data['name'],
            'poster': f"{self.IMAGE_BASE_URL}{series_data['poster_path']}",
            'number_of_episodes': series_data['number_of_episodes'],
            'url': f"{self.SERIES_BASE_URL}/{random_series['id']}"
        }

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
genre = 18  # Genre ID for Drama
fetcher = SeriesFetcher(api_key, genre)
series = fetcher.get_random_series()

if series:
    print(f"Title: {series['title']}\nPoster: {series['poster']}\nNumber of episodes: {series['number_of_episodes']}\nURL: {series['url']}")
