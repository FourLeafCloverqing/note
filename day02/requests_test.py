import time
from typing import List, Dict
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}


def get_movie_by_page(page):
    url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={(page - 1) * 20}'
    print('正在获取第{}页的数据...'.format(page))
    response = requests.get(url, headers=headers)
    response_json = response.json()

    subjects: List[Dict] = response_json.get('subjects')
    for movie in subjects:
        title = movie.get('title')
        url = movie.get('url')
        is_new = movie.get('is_new')
        rate = movie.get('rate')
        cover = movie.get('cover')
        print(f'movie name is {title}, rate: {rate}, image: {cover}')


if __name__ == '__main__':
    for page in range(1, 9):
        get_movie_by_page(page)
        time.sleep(3)
