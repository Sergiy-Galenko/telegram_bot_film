import requests, random

class Movie:
    def __init__(self, api_key): self.api_key, self.base_url = api_key, "https://api.themoviedb.org/3"
    def get_random_movie(self, genre_id):
        data = requests.get(f"{self.base_url}/discover/movie?api_key={self.api_key}&with_genres={genre_id}&page={random.randint(1, 500)}").json()
        if not data['results']: return None
        random_movie = random.choice(data['results'])
        return {'title': random_movie['title'], 'rating': random_movie['vote_average'],
                'poster': f"https://image.tmdb.org/t/p/original{random_movie['poster_path']}",
                'url': f"https://www.themoviedb.org/movie/{random_movie['id']}"}

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
movie_info = Movie(api_key).get_random_movie(28)  # 28 is the genre id for Action Movies
if movie_info: print(f"Title: {movie_info['title']}\nRating: {movie_info['rating']}\nPoster: {movie_info['poster']}\nURL: {movie_info['url']}")
