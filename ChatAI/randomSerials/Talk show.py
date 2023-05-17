import requests
import random

class RandomTalkShowSeries:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_random_talk_show_series(self):
        url = f"https://api.themoviedb.org/3/search/tv?api_key={self.api_key}&query=talk"
        response = requests.get(url)
        data = response.json()

        if data['results']:
            talk_shows = [series for series in data['results'] if 'Talk Show' in series.get('genres', [])]
            if talk_shows:
                random_series = random.choice(talk_shows)
                series_id = random_series['id']

                series_details_url = f"https://api.themoviedb.org/3/tv/{series_id}?api_key={self.api_key}"
                series_data = requests.get(series_details_url).json()

                return {
                    'title': series_data['name'],
                    'poster': f"https://image.tmdb.org/t/p/original{series_data['poster_path']}",
                    'number_of_episodes': series_data['number_of_episodes'],
                    'url': f"https://www.themoviedb.org/tv/{series_id}"
                }

        return None

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
random_talk_show_series = RandomTalkShowSeries(api_key)
series = random_talk_show_series.get_random_talk_show_series()
if series:
    for key, value in series.items():
        print(f"{key.capitalize()}: {value}")
