import requests, random

class RandomKidsSeries:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_random_kids_series(self):
        data = requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key={self.api_key}&with_genres=10762").json()
        if data['results']:
            series = random.choice(data['results'])
            series_data = requests.get(f"https://api.themoviedb.org/3/tv/{series['id']}?api_key={self.api_key}").json()
            return {
                'title': series_data['name'],
                'poster': f"https://image.tmdb.org/t/p/original{series_data['poster_path']}",
                'number_of_episodes': series_data['number_of_episodes'],
                'url': f"https://www.themoviedb.org/tv/{series['id']}"
            }

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
if (series := RandomKidsSeries(api_key).get_random_kids_series()):
    print(f"Title: {series['title']}\nPoster: {series['poster']}\nNumber of episodes: {series['number_of_episodes']}\nURL: {series['url']}")
