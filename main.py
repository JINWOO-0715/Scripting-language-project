# -*- coding: utf-8 -*-

import urllib.request as ul
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import xmltodict
import urllib
import requests
import json

# 출력 확인 완료
class Movie():

    def crawl_movie(self):
        self.movie_rank_service_key = requests.utils.unquote('c0a4510afa510bfe1e4fd885097ad953')
        self. movie_rank_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml'
        self.movie_rank_Params = '?' + urlencode(
            {
                quote_plus('key'): self.movie_rank_service_key,  # 서비스키
                quote_plus('targetDt'): 20200523,  # 조회 날짜
                quote_plus('itemPerPage'): 10,  # 페이지 수
                quote_plus('repNationCd'): '',  # K: 한국영화 조회 F:외국영화 default:전체
                quote_plus('wideAreaCd'): ''  # “0105000000” 로서 조회된 지역코드입니다. (default : 전체)
            }
        )
        request = urllib.request.Request(self.movie_rank_url + self.movie_rank_Params)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            print(response_body.decode())



        else:
            print("Error Code:" + rescode)


class Seoul():

    def __init__(self):
        self.movie_rank_service_key = requests.utils.unquote('77585a5357706a773737617a624a4a')
        self.movie_rank_url = 'http://openapi.seoul.go.kr:8088/%s/%s/movieTheatersBizInfo/1/5/'%(self.movie_rank_service_key ,
                                                                                                 'xml')
        self.movie_rank_Params = '?' + urlencode(
            {
                quote_plus('KEY'): self.movie_rank_service_key,  # 서비스키
                quote_plus('TYPE'): 'xml',  # 조회 날짜
                quote_plus('SERVICE'): 'movieTheatersBizInfo',  # 페이지 수
                quote_plus('START_INDEX'): '1',  # K: 한국영화 조회 F:외국영화 default:전체
                quote_plus('END_INDEX'): '5'  # “0105000000” 로서 조회된 지역코드입니다. (default : 전체)
            }
        )

    def crawl_movie(self):
        request = urllib.request.Request(self.movie_rank_url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            print(response_body.decode())
        else:
            print("Error Code:" + rescode)

Seoul().crawl_movie()