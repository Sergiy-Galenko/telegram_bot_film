import requests, random

class Movie:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def get_random_movie(self, genre_id):
        url = f"{self.base_url}/discover/movie?api_key={self.api_key}&with_genres={genre_id}&page={random.randint(1, 500)}"
        data = requests.get(url).json()
        if data['results']:
            movie = random.choice(data['results'])
            return {
                'title': movie['title'],
                'rating': movie['vote_average'],
                'poster': f"https://image.tmdb.org/t/p/original{movie['poster_path']}",
                'url': f"https://www.themoviedb.org/movie/{movie['id']}"
            }

movie_info = Movie('5c45b86ac58a42d9cfc4d98bedca011d').get_random_movie(10752)
if movie_info: print(f"Title: {movie_info['title']}\nRating: {movie_info['rating']}\nPoster: {movie_info['poster']}\nURL: {movie_info['url']}")
