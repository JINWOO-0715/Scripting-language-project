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


ServiceKey = 'ThtNwocpn%2FHryqtYMOFgt9hVYGst0U%2Fk5JRdSPLODsXctdvMDEx9eob%2FiwjafVsIzR4Rsla36FRt6rI46rXwsA%3D%3D'
url = 'http://openapi.seoul.go.kr:8088/sample/xml/movieTheatersBizInfo/1/5/'
api_key_decode = unquote(url)
params = '&pageNO=1&numOfRows=10&spclAdmTyCd=A0'
queryParams = '?' + urlencode(
    {
        quote_plus('serviceKey'): api_key_decode,
        quote_plus('pageNo'): 1,
        quote_plus('numOfRows') : 10,
    }
)
request = urllib.request.Request(api_key_decode)

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
