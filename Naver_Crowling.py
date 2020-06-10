# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import json
import re
import requests

# 네이버 검색 Open API 사용 요청시 얻게되는 정보를 입력합니다
naver_client_id = "mHqayEjLQi3Y5vpMchIt"
naver_client_secret = "BxD49l5brh"


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)

    return cleantext

#네이버 영화 제목 찾기 (코드)
def searchByTitle(title):
    myurl = 'https://openapi.naver.com/v1/search/movie.json?query=' + quote(title)
    request = urllib.request.Request(myurl)
    request.add_header("X-Naver-Client-Id", naver_client_id)
    request.add_header("X-Naver-Client-Secret", naver_client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        d = json.loads(response_body.decode('utf-8'))
        if (len(d['items']) > 0):
            return d['items']
        else:
            return None

    else:
        print("Error Code:" + rescode)

#제목 부제목 개봉일 배우 링크 유저평점 이건 네이버 영화 정보 찾기
def findItemByInput(items):
    for index, item in enumerate(items):
        navertitle = cleanhtml(item['title'])
        naversubtitle = cleanhtml(item['subtitle'])
        naverpubdate = cleanhtml(item['pubDate'])
        naveractor = cleanhtml(item['actor'])
        naverlink = cleanhtml(item['link'])
        naveruserScore = cleanhtml(item['userRating'])


        navertitle1 = navertitle.replace(" ", "")
        navertitle1 = navertitle1.replace("-", ",")
        navertitle1 = navertitle1.replace(":", ",")

        # 기자 평론가 평점을 얻어 옵니다
        #spScore = getSpecialScore(naverlink)
        #spStory = getStroy(naverlink)
        spMStory = getMStroy(naverlink)
        # 네이버가 다루는 영화 고유 ID를 얻어 옵니다다
        naverid = re.split("code=", naverlink)[1]

        # 영화의 타이틀 이미지를 표시합니다
        # if (item['image'] != None and "http" in item['image']):
        #    response = requests.get(item['image'])
        #    img = Image.open(BytesIO(response.content))
        #    img.show()

        print(index, navertitle) #naversubtitle,naverpubdate ,naveractor,naveruserScore, spScore)


def getInfoFromNaver(searchTitle):
    items = searchByTitle(searchTitle)
    if (items != None):
        findItemByInput(items)
    else:
        print("No result")


def get_soup(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    return soup


# 기자 평론가 평점을 얻어 옵니다
def getSpecialScore(URL):
    soup = get_soup(URL)
    scorearea = soup.find_all('div', "spc_score_area")
    newsoup = BeautifulSoup(str(scorearea), 'lxml')
    score = newsoup.find_all('em')
    if (score and len(score) > 5):
        scoreis = score[1].text + score[2].text + score[3].text + score[4].text
        return float(scoreis)
    else:
        return 0.0
def getStroy(URL):
    soup = get_soup(URL)
    scorearea = soup.find_all('div', 'story_area')
    newsoup = BeautifulSoup(str(scorearea), 'lxml')
    head_story =newsoup.find('h5')
    if head_story != None:
        head_story = newsoup.find('h5').text
    # if main_story != None:
    #     for i in main_story:
    #         i. newsoup.find('p').text

def getMStroy(URL):
    soup = get_soup(URL)
    scorearea = soup.find_all('div', 'story_area')
    newsoup = BeautifulSoup(str(scorearea), 'lxml')
    content_infos =[]
    contents_texts = newsoup.select('div.story_area > p.con_tx')
    if len(contents_texts) == 0:
        content_infos.append("줄거리 오류")
    else:
        for contents in contents_texts:
            temp = contents.text
            temp = temp.replace('\r', '')
            temp = temp.replace('\xa0', '')
            content_infos.append(temp)
    print(content_infos)




    # if main_story != None:
    #     for i in main_story:
    #         i. newsoup.find('p').text

getInfoFromNaver(u"언더워터")