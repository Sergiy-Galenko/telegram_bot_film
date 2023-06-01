import requests, random

class RandomTalkShowSeries:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_random_talk_show_series(self):
        data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={self.api_key}&query=talk").json()
        if data['results']:
            talk_shows = [series for series in data['results'] if 'Talk Show' in series.get('genres', [])]
            if talk_shows:
                series = random.choice(talk_shows)
                series_data = requests.get(f"https://api.themoviedb.org/3/tv/{series['id']}?api_key={self.api_key}").json()
                return {
                    'title': series_data['name'],
                    'poster': f"https://image.tmdb.org/t/p/original{series_data['poster_path']}",
                    'number_of_episodes': series_data['number_of_episodes'],
                    'url': f"https://www.themoviedb.org/tv/{series['id']}"
                }

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
if (series := RandomTalkShowSeries(api_key).get_random_talk_show_series()): [print(f"{k.capitalize()}: {v}") for k, v in series.items()]
