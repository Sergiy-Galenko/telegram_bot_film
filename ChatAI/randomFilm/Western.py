import requests
import random

class Movie:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def get_random_movie(self, genre_id):
        page = random.randint(1, 500)
        url = f"{self.base_url}/discover/movie?api_key={self.api_key}&with_genres={genre_id}&page={page}"
        response = requests.get(url)
        data = response.json()

        if data['results']:
            random_movie = random.choice(data['results'])
            movie_id = random_movie['id']

            return {
                'title': random_movie['title'],
                'rating': random_movie['vote_average'],
                'poster': f"https://image.tmdb.org/t/p/original{random_movie['poster_path']}",
                'url': f"https://www.themoviedb.org/movie/{movie_id}"
            }

        return None

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'  # Замените на свой собственный API-ключ
movie = Movie(api_key)
movie_info = movie.get_random_movie(37)  # 37 это genre id для вестернов.
if movie_info:
    print(f"Title: {movie_info['title']}\nRating: {movie_info['rating']}\nPoster: {movie_info['poster']}\nURL: {movie_info['url']}")
