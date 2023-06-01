import requests
import random

class TVSeries:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_random_series(self, genre_id):
        url = f"https://api.themoviedb.org/3/discover/tv?api_key={self.api_key}&with_genres={genre_id}&page={random.randint(1, 500)}"
        data = requests.get(url).json()
        if not data['results']: return None
        random_show = random.choice(data['results'])
        show_id = random_show['id']
        show_data = requests.get(f"https://api.themoviedb.org/3/tv/{show_id}?api_key={self.api_key}").json()
        return {
            'title': show_data['name'],
            'rating': random_show['vote_average'],
            'number_of_episodes': sum(season['episode_count'] for season in show_data['seasons']),
            'poster': f"https://image.tmdb.org/t/p/w500{random_show['poster_path']}",
            'url': f"https://www.themoviedb.org/tv/{show_id}"
        }

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
series = TVSeries(api_key).get_random_series(35)  # 35 is the genre id for comedy series
if series:
    print(f"Title: {series['title']}\nRating: {series['rating']}\nNumber of episodes: {series['number_of_episodes']}\nPoster: {series['poster']}\nURL: {series['url']}")
