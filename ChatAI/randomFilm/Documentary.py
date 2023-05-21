import requests
import random

class Movie:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def get_random_movie(self, genre_id):
        data = requests.get(f"{self.base_url}/discover/movie?api_key={self.api_key}&with_genres={genre_id}&page={random.randint(1, 500)}").json()

        if data['results']:
            random_movie = random.choice(data['results'])
            return {
                'title': random_movie['title'],
                'rating': random_movie['vote_average'],
                'poster': f"https://image.tmdb.org/t/p/original{random_movie['poster_path']}",
                'url': f"https://www.themoviedb.org/movie/{random_movie['id']}"
            }

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'  # Замените на свой собственный API-ключ
movie_info = Movie(api_key).get_random_movie(99)  # 99 это genre id для документальных фильмов.

if movie_info:
    print(f"Title: {movie_info['title']}\nRating: {movie_info['rating']}\nPoster: {movie_info['poster']}\nURL: {movie_info['url']}")
