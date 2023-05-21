import requests, random

class RandomWesternSeries:
    def __init__(self, api_key): self.api_key = api_key
    def get_random_western_series(self):
        data = requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key={self.api_key}&with_genres=37").json()
        if data['results']:
            random_series = random.choice(data['results'])
            series_data = requests.get(f"https://api.themoviedb.org/3/tv/{random_series['id']}?api_key={self.api_key}").json()
            return {
                'title': series_data['name'],
                'poster': f"https://image.tmdb.org/t/p/original{series_data['poster_path']}",
                'number_of_episodes': series_data['number_of_episodes'],
                'url': f"https://www.themoviedb.org/tv/{random_series['id']}"
            }
        return None

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
series = RandomWesternSeries(api_key).get_random_western_series()
if series: [print(f"{key.capitalize()}: {value}") for key, value in series.items()]
