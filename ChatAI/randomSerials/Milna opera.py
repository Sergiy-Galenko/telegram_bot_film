import requests
import random

def get_random_soap_series(api_key):
    url = f"https://api.themoviedb.org/3/discover/tv?api_key={api_key}&with_genres=10766"
    response = requests.get(url)
    data = response.json()

    if data['results']:
        random_series = random.choice(data['results'])
        series_id = random_series['id']

        series_details_url = f"https://api.themoviedb.org/3/tv/{series_id}?api_key={api_key}"
        series_data = requests.get(series_details_url).json()

        return {
            'title': series_data['name'],
            'poster': f"https://image.tmdb.org/t/p/original{series_data['poster_path']}",
            'number_of_episodes': series_data['number_of_episodes'],
            'url': f"https://www.themoviedb.org/tv/{series_id}"
        }

    return None

api_key = '5c45b86ac58a42d9cfc4d98bedca011d'
series = get_random_soap_series(api_key)
if series:
    for key, value in series.items():
        print(f"{key.capitalize()}: {value}")
