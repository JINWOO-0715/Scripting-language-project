from ReadFile import *
movie = Movie()
def SearchButtonAction():
    movie_ranking= movie.crawl_movie()
    print(movie_ranking['rank'],
          movie_ranking['movieNm'],
          movie_ranking['showTm'],
          len(movie_ranking['actors']),
          len(movie_ranking['showTypes']))
def SearchLibrary():
    pass