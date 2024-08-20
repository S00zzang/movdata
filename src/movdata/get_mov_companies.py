import requests
import os
import json
import time
from tqdm import tqdm

API_KEY = os.getenv('MOVIE_API_KEY')

# 전체 동작 Proccess
def load_movie_companies(per_page = 10, sleep_time = 1):

    companies = []

    # API 호출로 totCnt를 얻어 전체 Page 계산
    tot_cnt = request_companies(1)['companyListResult']['totCnt']
    tot_pages = int(tot_cnt // per_page) + 1

    # 데이터 추출
    for idx in tqdm(range(1, tot_pages + 1)):
        # time.sleep(sleep_time)
        data = request_companies(idx)['companyListResult']['companyList']
        companies.extend(data)

    save_companies_set(data)

    return True

# 영화사 호출
def request_companies(page):
    api_url = f"http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json?key={API_KEY}"
    api_url += f"&curPage={page}"
    compaines_data = requests.get(api_url).json()
    return compaines_data

# 전체 영화사 저장
def save_companies_set(data):
    file_path = "data/movies-companies/data.json"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
