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
kids_series_instance = RandomKidsSeries(api_key)
random_kids_series = kids_series_instance.get_random_kids_series()

if random_kids_series:
    print(f"Title: {random_kids_series['title']}")
    print(f"Poster: {random_kids_series['poster']}")
    print(f"Number of episodes: {random_kids_series['number_of_episodes']}")
    print(f"URL: {random_kids_series['url']}")
