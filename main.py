import requests
from bs4 import BeautifulSoup

def get_movie_info(search_query):
    # Замените на URL сайта, с которым вы хотите работать
    base_url = 'https://rezka.ag/'
    search_url = f"{base_url}?q={search_query}"
    
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Замените на соответствующий селектор для названия фильма и изображения
        movie_title_selector = 'div.movie-title'
        movie_image_selector = 'img.movie-image'
        
        movie_title = soup.select_one(movie_title_selector)
        movie_image = soup.select_one(movie_image_selector)
        
        if movie_title and movie_image:
            return {
                'title': movie_title.text.strip(),
                'image': movie_image['src']
            }
        else:
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == '__main__':
    search_query = input('Введите название фильма: ')
    movie_info = get_movie_info(search_query)
    
    if movie_info:
        print(f"Название фильма: {movie_info['title']}")
        print(f"Картинка фильма: {movie_info['image']}")
    else:
        print("Фильм не найден.")
