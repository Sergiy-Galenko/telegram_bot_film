import requests
import random

class TVSeries:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"
        self.image_base_url = 'https://image.tmdb.org/t/p/w500'
        self.tmdb_tv_show_url = 'https://www.themoviedb.org/tv/'

    def get_random_series(self, genre_id):
        page = random.randint(1, 500)  # Random page from 1 to 500
        discover_url = f'{self.base_url}/discover/tv?api_key={self.api_key}&with_genres={genre_id}&page={page}'

        response = requests.get(discover_url)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                random_show = random.choice(data['results'])
                show_id = random_show['id']
                show_title = random_show['name']
                show_rating = random_show['vote_average']
                show_poster_url = f"{self.image_base_url}{random_show['poster_path']}"
                show_page_url = f"{self.tmdb_tv_show_url}{show_id}"

                # Get show details to count the number of episodes
                tv_show_url = f'{self.base_url}/tv/{show_id}?api_key={self.api_key}'
                tv_show_response = requests.get(tv_show_url)
                if tv_show_response.status_code == 200:
                    episode_count = sum([season['episode_count'] for season in tv_show_response.json()['seasons']])
                    return {
                        'title': show_title,
                        'rating': show_rating,
                        'number_of_episodes': episode_count,
                        'poster': show_poster_url,
                        'url': show_page_url
                    }
                else:
                    print("Не удалось получить информацию о сериале. Проверьте ваш API ключ и соединение.")
            else:
                print("Не удалось найти сериалы на данной странице. Попробуйте еще раз.")
        else:
            print("Не удалось получить данные от TMDb. Проверьте ваш API ключ и соединение.")
        return None

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
tv_series = TVSeries(api_key)
series = tv_series.get_random_series(35)  # 35 is the genre id for comedy series
if series:
    print(f"Title: {series['title']}\nRating: {series['rating']}\nNumber of episodes: {series['number_of_episodes']}\nPoster: {series['poster']}\nURL: {series['url']}")
