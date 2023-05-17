import requests
import random

class TVSeries:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def get_random_series(self, genre_id):
        url = f"{self.base_url}/discover/tv?api_key={self.api_key}&with_genres={genre_id}"
        response = requests.get(url)
        data = response.json()

        if data['results']:
            random_series = random.choice(data['results'])
            series_id = random_series['id']

            series_details_url = f"{self.base_url}/tv/{series_id}?api_key={self.api_key}"
            series_data = requests.get(series_details_url).json()

            return {
                'title': series_data['name'],
                'poster': f"https://image.tmdb.org/t/p/original{series_data['poster_path']}",
                'number_of_episodes': series_data['number_of_episodes'],
                'url': f"https://www.themoviedb.org/tv/{series_id}"
            }

        return None

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
tv_series = TVSeries(api_key)
series = tv_series.get_random_series(9648)  # 9648 is the genre id for detective series
if series:
    print(f"Title: {series['title']}\nPoster: {series['poster']}\nNumber of episodes: {series['number_of_episodes']}\nURL: {series['url']}")
