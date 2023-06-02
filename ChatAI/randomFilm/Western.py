import requests, random

class Movie:
    BASE_URL = "https://api.themoviedb.org/3"
    def __init__(self, api_key):
        self.api_key = api_key
    def get_random_movie(self, genre_id):
        try:
            response = requests.get(f"{self.BASE_URL}/discover/movie", params={'api_key': self.api_key, 'with_genres': genre_id, 'page': random.randint(1, 500)})
            movie = random.choice(response.json()['results'])
            return {'title': movie['title'], 'rating': movie['vote_average'], 'poster': f"https://image.tmdb.org/t/p/original{movie['poster_path']}", 'url': f"https://www.themoviedb.org/movie/{movie['id']}"}
        except Exception as e: print(f"Error fetching movie details: {e}")

movie_info = Movie('5c45b86ac58a42d9cfc4d98bedca011d').get_random_movie(37)
if movie_info: print(f"Title: {movie_info['title']}\nRating: {movie_info['rating']}\nPoster: {movie_info['poster']}\nURL: {movie_info['url']}")
