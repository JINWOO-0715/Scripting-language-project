# -*- coding: utf-8 -*-

import urllib.request as ul
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
from datetime import datetime ,timedelta

import pandas as pd

# 출력 확인 완료
class Movie():
    def crawl_movie(self , date=(datetime.today() - timedelta(1)).strftime('%Y%m%d')):
        self.movie_rank_service_key = requests.utils.unquote('c0a4510afa510bfe1e4fd885097ad953')
        self.movie_rank_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
        self.now_defalut = date
        self.movie_rank_Params = '?' + urlencode(
            {
                quote_plus('key'): self.movie_rank_service_key,  # 서비스키
                quote_plus('targetDt'):self.now_defalut,  # 조회 날짜
                quote_plus('itemPerPage'): 10,  # 페이지 수
                quote_plus('repNationCd'): '',  # K: 한국영화 조회 F:외국영화 default:전체
                quote_plus('wideAreaCd'): ''  # “0105000000” 로서 조회된 지역코드입니다. (default : 전체)
            }
        )
        request = urllib.request.Request(self.movie_rank_url + self.movie_rank_Params)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        #잘돌아가나 확인용
        if rescode == 200:
            responseData = response.read()
            result = json.loads(responseData)
            movieInfo = result['boxOfficeResult']['dailyBoxOfficeList']
            return  movieInfo
        else:
            print("Error Code:" + rescode)


class Seoul():

    def __init__(self):
        self.df= pd.read_excel('영화상영관.xlsx',sheet_name='영화상영관_1')


    def crawl_movie(self):
        return self.df
