from ReadFile import *
from Main import *

movie = Movie()

def SearchButtonAction(m):
    movie_ranking= movie.crawl_movie()
    for i in movie_ranking:
        main.ReturnMovieRankingText.insert(
            i['rank'], i['movieNm'], i['showTm'], len(i['actors']), len(i['showTypes'])
        )

def SearchLibrary():
    pass

SearchButtonAction()