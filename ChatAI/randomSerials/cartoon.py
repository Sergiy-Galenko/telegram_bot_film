import requests
import random

class TVSeries:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_random_series(self, genre_id):
        data = requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key={self.api_key}&with_genres={genre_id}").json()
        if data['results']:
            series_data = requests.get(f"https://api.themoviedb.org/3/tv/{random.choice(data['results'])['id']}?api_key={self.api_key}").json()
            return {
                'title': series_data['name'],
                'poster': f"https://image.tmdb.org/t/p/original{series_data['poster_path']}",
                'number_of_episodes': series_data['number_of_episodes'],
                'url': f"https://www.themoviedb.org/tv/{series_data['id']}"
            }

tv_series = TVSeries('5c45b86ac58a42d9cfc4d98bedca011d')
series = tv_series.get_random_series(16)
if series:
    print(f"Title: {series['title']}\nPoster: {series['poster']}\nNumber of episodes: {series['number_of_episodes']}\nURL: {series['url']}")
