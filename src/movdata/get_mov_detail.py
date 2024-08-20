import requests
import os
import json
import time
from tqdm import tqdm

def load_movie_list(year):
    load_path = f"data/movies/year={year}/data.json"
    with open(load_path, 'r', encoding='utf-8') as file:
        load_data = json.load(file)
    return load_data

def make_movie_info_data(year):
    # JSON 데이터를 읽는다.
    load_data = load_movie_list(year)

    # 영화 리스트를 for문으로 돌면서 각각의 데이터의 상세 정보를 추출
    all_movie_info_data = []
    for movie in tqdm(load_data):
        movie_cd = movie['movieCd']
        movie_info = get_info_data(movie_cd)
        if movie_info:
            all_movie_info_data.append(movie_info)

    # 추출한 데이터를 저장
    save_data_info_set(year, all_movie_info_data)

    return True

def save_data_info_set(year, data):
    os.makedirs(f"data/movies_info/year={year}", exist_ok=True)
    write_path = f"data/movies_info/year={year}/data.json"
    with open(write_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# 하나의 영화의 상세 정보를 가져온다.
def get_info_data(movie_cd):
    api_url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={os.getenv('MOVIE_API_KEY')}"
    api_url += f"&movieCd={movie_cd}"

    response_data = requests.get(api_url).json()

    return response_data
