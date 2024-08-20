from movdata.ml import save_movies
from movdata.get_mov_detail import load_movie_list, make_movie_info_data
from movdata.get_mov_companies import load_movie_companies

def test_load_companies():
    assert load_movie_companies()
