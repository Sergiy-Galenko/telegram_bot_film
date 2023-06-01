import requests
import random

class TVSeries:
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_random_series(self, genre_id):
        try:
            response = requests.get(f"{self.BASE_URL}/discover/tv", params={
                'api_key': self.api_key,
                'with_genres': genre_id
            })
            response.raise_for_status()
            data = response.json()

            if not data['results']:
                print("No series found.")
                return None

            series = random.choice(data['results'])

            series_response = requests.get(f"{self.BASE_URL}/tv/{series['id']}", params={'api_key': self.api_key})
            series_response.raise_for_status()
            series_data = series_response.json()

            return {
                'title': series_data['name'],
                'poster': f"https://image.tmdb.org/t/p/original{series_data['poster_path']}",
                'number_of_episodes': series_data['number_of_episodes'],
                'url': f"https://www.themoviedb.org/tv/{series_data['id']}"
            }
        except (requests.RequestException, ValueError) as error:
            print(f"Error fetching series details: {error}")
            return None

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
tv_series = TVSeries(api_key)
series = tv_series.get_random_series(10759)  # 10759 is the genre id for action & adventure series

if series:
    print(f"Title: {series['title']}\nPoster: {series['poster']}\nNumber of episodes: {series['number_of_episodes']}\nURL: {series['url']}")
