import requests
import random

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
base_url = 'https://api.themoviedb.org/3'
image_base_url = 'https://image.tmdb.org/t/p/w500'
tmdb_movie_url = 'https://www.themoviedb.org/movie/'
genre_id = 53  # ID для жанра триллеров
page = random.randint(1, 500)  # Выбираем случайную страницу от 1 до 500

url = f'{base_url}/discover/movie?api_key={api_key}&with_genres={genre_id}&page={page}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data['results']:
        random_movie = random.choice(data['results'])
        movie_id = random_movie['id']
        movie_title = random_movie['title']
        movie_rating = random_movie['vote_average']
        movie_poster_path = random_movie['poster_path']
        movie_poster_url = f"{image_base_url}{movie_poster_path}"
        movie_page_url = f"{tmdb_movie_url}{movie_id}"
        print(f"Рандомный фильм из категории триллеров: {movie_title}\n"
              f"Рейтинг: {movie_rating}\n"
              f"Ссылка на постер: {movie_poster_url}\n"
              f"Ссылка на фильм: {movie_page_url}")
    else:
        print("Не удалось найти фильмы на данной странице. Попробуйте еще раз.")
else:
    print("Не удалось получить данные от TMDb. Проверьте ваш API ключ и соединение.")

