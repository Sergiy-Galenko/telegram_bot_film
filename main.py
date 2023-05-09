import requests
from bs4 import BeautifulSoup
import random
import http.client

from fake_useragent import UserAgent

http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
http.client.HTTPConnection._http_vsn = 10

BASE_URL = 'https://rezka.ag/films/action/page/'
IMAGE_BASE_URL = 'https://rezka.ag'

def get_random_action_movie():
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    # Получаем случайную страницу из списка боевиков
    random_page = random.randint(1, 50)
    url = f'{BASE_URL}{random_page}/'
    
    success = False
    while not success:
        try:
            response = requests.get(url, headers=headers)
            success = True
        except:
            pass

    soup = BeautifulSoup(response.text, 'html.parser')

    # Выбираем случайный фильм из списка на странице
    movie_blocks = soup.find_all('div', class_='b-content__inline_item')
    random_movie_block = random.choice(movie_blocks)
    movie_link = random_movie_block.find('a', class_='b-content__inline_item-link')

    title = movie_link['title']
    movie_url = movie_link['href']
    image_url = IMAGE_BASE_URL + random_movie_block.find('img')['src']
    rating = random_movie_block.find('div', class_='b-inline__rating').text.strip()

    return {
        'title': title,
        'url': movie_url,
        'image': image_url,
        'rating': rating,
    }

if __name__ == '__main__':
    random_action_movie = get_random_action_movie()
    print('Название:', random_action_movie['title'])
    print('Ссылка:', random_action_movie['url'])
    print('Изображение:', random_action_movie['image'])
    print('Рейтинг:', random_action_movie['rating'])
