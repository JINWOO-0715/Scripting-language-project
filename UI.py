from tkinter import *
from tkinter import font
import tkinter.ttk
from ReadFile import *
from Naver_Crowling import *
from pandas import DataFrame
import pandas
import matplotlib.pyplot as plt
import numpy
from Map import *


def callback(event):
    print("clicked at", event.x, event.y)


window = Tk()
window.title("서울시 영화 정보 검색")

window.bind("<Button-1>", callback)

notebook = tkinter.ttk.Notebook(window, width=800, height=600)
notebook.pack()

image = []
image.append(PhotoImage(file='resource/output/rank_icon.png'))  # 0
image.append(PhotoImage(file='resource/output/big_search.png'))  # 1
image.append(PhotoImage(file='resource/output/big_map.png'))  # 2
image.append(PhotoImage(file='resource/output/gmail-icon.png'))  # 3
image.append(PhotoImage(file='resource/output/boxoffice.png'))  # 4
image.append(PhotoImage(file='resource/output/graph.png'))  # 5
image.append(PhotoImage(file='resource/output/small_search.png'))  # 6
image.append(PhotoImage(file='resource/output/small_map.png'))  # 7
movie_ranking = Movie().crawl_movie()
movie_map = Seoul().crawl_movie()

# 검색 버튼 기능
def SearchButtonAction():
    s = day_InputLabel.get()
    movie_ranking = Movie().crawl_movie(s)

    movie_ranking_list_box.delete(0, 9)
    for i in movie_ranking:
        movie_ranking_list_box.insert(10, "[" + i['rank'] + "위]" + i['movieNm'])


# 함수 - 영화 상세 정보  함수
def SearchMovieStory():
    movie_imformation_text.configure(state='normal')
    num = movie_ranking_list_box.curselection()
    i = int(num[0])
    movie_imformation_text.delete('1.0', END)
    movie_imformation_text.insert(INSERT, movie_ranking[i]['movieNm'])
    movie_imformation_text.insert(INSERT, "\n")
    movie_imformation_text.insert(INSERT, "개봉일: ")
    movie_imformation_text.insert(INSERT, movie_ranking[i]['movieCd'])
    movie_imformation_text.insert(INSERT, " ")
    movie_imformation_text.insert(INSERT, "\n")
    movie_imformation_text.insert(INSERT, "누적 관람객: ")
    movie_imformation_text.insert(INSERT, movie_ranking[i]['audiAcc'] + "명")
    movie_imformation_text.insert(INSERT, "\n")
    movie_imformation_text.insert(INSERT, "당일 관람객: ")
    movie_imformation_text.insert(INSERT, movie_ranking[i]['audiCnt'] + "명")
    movie_imformation_text.insert(INSERT, "\n")
    items = searchByTitle(movie_ranking[i]['movieNm'])
    Mstory, userscore, spscore = findItemByInput(items)
    movie_imformation_text.insert(INSERT, "기자 평론가 평점: ")
    movie_imformation_text.insert(INSERT, spscore)
    movie_imformation_text.insert(INSERT, "\n")
    movie_imformation_text.insert(INSERT, "관람객 평점: ")
    movie_imformation_text.insert(INSERT, userscore)
    movie_imformation_text.insert(INSERT, "\n")
    movie_imformation_text.insert(INSERT, "줄거리 : %s" % Mstory)


# 랭킹 페이지 생성 밑으로 랭킹 관련
movie_ranking_frame = Frame(window)
notebook.add(movie_ranking_frame, text="페이지1", image=image[0])
movie_ranking_frame.configure(bg='#F79F81')

# 박스오피스 그림 라벨
label1 = Label(window, image=image[4], bg='#F79F81')
label1.pack(side=RIGHT)
label1.place(x=500, y=0)


# 폰트
TempFont = font.Font(movie_ranking_frame, size=20, weight='bold', family='Malgun Gothic')

# 왼쪽의 일간 박스 오피스 글씨
movie_ranking_Text = Label(movie_ranking_frame, font=TempFont, text="[일간 박스오피스]")
movie_ranking_Text.pack()
movie_ranking_Text.place(x=10)
movie_ranking_Text.configure(bg='#F79F81')

# 날짜 입력 받기
day_InputLabel = Entry(movie_ranking_frame, font=TempFont, width=20, borderwidth=10, relief='ridge')
day_InputLabel.pack()
day_InputLabel.place(x=280, y=0)
day_InputLabel.configure(bg='#F79F81')

# 검색 버튼 생성
SearchButton = Button(movie_ranking_frame, font=TempFont, text="검색", command=SearchButtonAction, image=image[6],bg='#F6D8CE')
SearchButton.pack()
SearchButton.place(x=650, y=3)

# 리스트박스 - 영화 랭킹
movie_ranking_list_box = None
TempFont = font.Font(movie_ranking_frame, size=10, weight='bold', family='Malgun Gothic')
movie_ranking_list_box = Listbox(movie_ranking_frame, font=TempFont, activestyle='none',
                                 width=21, height=11, borderwidth=20, relief='ridge')
movie_ranking_list_box.pack()
movie_ranking_list_box.place(x=10, y=140)
movie_ranking_list_box.configure(bg='#F6D8CE')
for i in movie_ranking:
    movie_ranking_list_box.insert(10, "[" + i['rank'] + "위]" + i['movieNm'])

# 버튼 - 상세검색
TempFont = font.Font(movie_ranking_frame, size=12, weight='bold', family='Malgun Gothic')
MovieStorySearchButton = Button(movie_ranking_frame, font=TempFont, text="상세검색", command=SearchMovieStory)
MovieStorySearchButton.pack(side=LEFT)
MovieStorySearchButton.place(x=120, y=410)

# 영화 포스터 라벨 아직 안됨  파일 인식 불가
movie_poster = Label(movie_ranking_frame, width=200, height=200, borderwidth=20, image=image[4], relief='ridge',
                     font=TempFont)
movie_poster.pack()
movie_poster.place(x=250, y=140)
label1.configure(bg='#F6D8CE')

# 텍스트 - 영화 상세 정보 담는 텍스트함
TempFont = font.Font(movie_ranking_frame, size=10, weight='bold', family='Malgun Gothic')
movie_imformation_text = Text(movie_ranking_frame, width=21, height=11, borderwidth=20, relief='ridge',
                              font=TempFont, bg='#F6D8CE')
movie_imformation_text.pack()
movie_imformation_text.place(x=550, y=140)
movie_imformation_text.configure(state='disabled')


def makegraph():
    plt.rc('font', family='Malgun Gothic')
    plt.rc('axes', unicode_minus=False)
    plt.rcParams["font.size"] = 10
    plt.rcParams['xtick.labelsize'] = 10.
    plt.rcParams['ytick.labelsize'] = 10.
    df = DataFrame(movie_ranking)
    df = df.filter(items=['rnum','movieNm', 'audiAcc', 'audiCnt'])
    df = df.astype({'audiAcc': int, 'audiCnt': int})

    plt.figure()
    X = numpy.arange(10)
    plt.bar(X + 0.3, df['audiCnt'], color='g', width=0.25, label='금일관람객')
    plt.bar(df['rnum']+'위', df['audiAcc'], color='r', width=0.25, label='누적관람객')
    for x, y in enumerate(list(df['audiAcc'])):
        txt = "%d" % y
        plt.text(x, y, txt, fontsize=10, color='#000000',
                 horizontalalignment='center', verticalalignment='bottom')
    for x, y in enumerate(list(df['audiCnt'])):
        txt = "%d" % y
        plt.text(x + 0.25, y, txt, fontsize=10, color='#000000',
                 horizontalalignment='center', verticalalignment='bottom')

    plt.legend()
    plt.title("관람객 그래프")
    plt.xlabel('영화')
    plt.ylabel('관객수')

    # plt.bar(df['movieNm'],df['audiCnt'])
    plt.show()


# 버튼 - 그래프
MovieStorySearchButton = Button(movie_ranking_frame, image=image[5], command=makegraph ,bg='#F6D8CE')
MovieStorySearchButton.pack()
MovieStorySearchButton.place(x=720, y=3)

# 페이지-영화 상세 정보 생성
movie_information_frame = Frame(window)
notebook.add(movie_information_frame, text="페이지2", image=image[1])
movie_information_frame.configure(bg='#F79F81')

label1 = Label(movie_information_frame, text="영화 상세 정보 생성", fg='red', font=TempFont)
label1.pack()

# 페이지 -영화관 지도 생성
movie_map_frame = Frame(window)
notebook.add(movie_map_frame, image=image[2])
movie_map_frame.configure(bg='#F79F81')

def showmap():
    pass
def searchmap():
    m = map_InputLabel.get()
    movie_map.filter(items=['번호', '소재지전체주소', '좌표정보(X)', '좌표정보(Y)'])
    contains_korea_or_japan = movie_map['ADDR_OLD'].str.contains("%s"%m)
    print(contains_korea_or_japan)
    subset_df = movie_map[contains_korea_or_japan]
    print(subset_df)
# 폰트
TempFont = font.Font(movie_map_frame, size=20, weight='bold', family='Malgun Gothic')

# 왼쪽의 서울시 영화관 찾기 글씨
movie_ranking_Text = Label(movie_map_frame, font=TempFont, text="[서울시 영화관 찾기]")
movie_ranking_Text.pack()
movie_ranking_Text.place(x=10)
movie_ranking_Text.configure(bg='#F79F81')

#지역 입력받기
map_InputLabel = Entry(movie_map_frame, font=TempFont, width=20, borderwidth=10, relief='ridge')
map_InputLabel.pack()
map_InputLabel.place(x=280, y=0)
map_InputLabel.configure(bg='#F79F81')

#지역 검색 버튼
map_SearchButton = Button(movie_map_frame, font=TempFont, text="검색", command=searchmap, image=image[6],bg='#F6D8CE')
map_SearchButton.pack()
map_SearchButton.place(x=650, y=3)

#지도출력 버튼
MovieStorySearchButton = Button(movie_map_frame, image=image[7], command=showmap ,bg='#F6D8CE')
MovieStorySearchButton.pack()
MovieStorySearchButton.place(x=720, y=3)



# 페이지 - 메일 & 텔레그램
movie_mail_frame = Frame(window)
notebook.add(movie_mail_frame, image=image[3])
movie_mail_frame.configure(bg='#F79F81')

label1 = Label(movie_mail_frame, text="메일 텔레그램", fg='red', font='helvetica 48')
label1.pack()




window.mainloop()

