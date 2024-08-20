import requests
import os
import json
import time
from tqdm import tqdm

API_KEY = os.getenv('MOVIE_API_KEY')

def save_json(data, file_path):

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def req(url):
    r = requests.get(url)
    j = r.json()
    return j

def save_movies(year, per_page=10, sleep_time=1):
    file_path = f'data/movies/year={year}/data.json'

    url_base = f"https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={API_KEY}&openStartDt={year}&openEndDt={year}"
    
    r = req(url_base + "&curPage=1")
    tot_cnt = r['movieListResult']['totCnt']
    total_pages = (tot_cnt // per_page) + 1

    all_data = []
    for page in tqdm(range(1, total_pages + 1)):
        time.sleep(sleep_time)
        r = req(url_base + f"&curPage={page}")
        d = r['movieListResult']['movieList']
        all_data.extend(d)

    save_json(all_data, file_path)
    return True
