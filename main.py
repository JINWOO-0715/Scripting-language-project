# -*- coding: utf-8 -*-

import urllib.request as ul
import xmltodict
import json
import sys
import io
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests

movie_rank_service_key = requests.utils.unquote('c0a4510afa510bfe1e4fd885097ad953')

movie_rank_url ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml'
movie_rank_Params = '?' + urlencode(
    {
        quote_plus('key'): movie_rank_service_key, # 서비스키
        quote_plus('targetDt'): 20200523, # 조회 날짜
        quote_plus('itemPerPage') : 10, # 페이지 수
        quote_plus('repNationCd'): '', # K: 한국영화 조회 F:외국영화 default:전체
        quote_plus('wideAreaCd'): '' #“0105000000” 로서 조회된 지역코드입니다. (default : 전체)
    }
)

request = urllib.request.Request(movie_rank_url+movie_rank_Params)

response_body = urlopen(request).read()
response = urllib.request.urlopen(request)
rescode = response.getcode()


if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))
    #rD = xmltodict.parse(response_body)
    #rDJ = json.dumps(rD)
    #rDD = json.loads(rDJ)

else:
    print("Error Code:" + rescode)
