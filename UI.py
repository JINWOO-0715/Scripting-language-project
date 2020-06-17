from tkinter import *
from tkinter import font
import tkinter.ttk
from ReadFile import *
from Naver_Crowling import *
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from Map import *
from PIL import Image, ImageTk
import Gmail


def callback(event):
    print("clicked at", event.x, event.y)


window = Tk()
window.title("영화 정보 검색")

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
image.append(PhotoImage(file='resource/output/small_bookmark.png'))  # 8
image.append(PhotoImage(file='resource/output/small_gmail.png'))  # 9
image.append(PhotoImage(file='resource/output/remove_icon.png'))  # 10


movie_ranking = Movie().crawl_movie()
movie_map = Seoul().crawl_movie()


# 검색 버튼 기능
def SearchButtonAction():
    global movie_ranking_list_box, movie_ranking
    s = day_InputLabel.get()
    movie_ranking = Movie().crawl_movie(s)
    movie_ranking_list_box.delete(0, movie_ranking_list_box.size())
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

    # 영화 포스터 라벨
    im = Image.open('%s.jpg' % movie_ranking[i]['movieNm'])
    im = im.resize((150, 200))
    movie_poster.img = ImageTk.PhotoImage(im)
    movie_poster['image'] = movie_poster.img


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
SearchButton = Button(movie_ranking_frame, font=TempFont, text="검색", command=SearchButtonAction, image=image[6],
                      bg='#F6D8CE')
SearchButton.pack()
SearchButton.place(x=650, y=3)

# 리스트박스 - 영화 랭킹
movie_ranking_list_box = None
TempFont = font.Font(movie_ranking_frame, size=10, weight='bold', family='Malgun Gothic')
movie_ranking_list_box = Listbox(movie_ranking_frame, font=TempFont, activestyle='none',
                                 width=22, height=11, borderwidth=20, relief='ridge')
movie_ranking_list_box.pack()
movie_ranking_list_box.place(x=10, y=140)
movie_ranking_list_box.configure(bg='#F6D8CE')
for i in movie_ranking:
    movie_ranking_list_box.insert(10, "[" + i['rank'] + "위]" + i['movieNm'])

# 버튼 - 상세검색
TempFont = font.Font(movie_ranking_frame, size=12, weight='bold', family='Malgun Gothic')
MovieStorySearchButton = Button(movie_ranking_frame, font=TempFont, text="상세검색", command=SearchMovieStory)
MovieStorySearchButton.pack(side=LEFT)
MovieStorySearchButton.place(x=80, y=400)

# 영화포스터
movie_poster = Label(movie_ranking_frame, width=150, height=200, borderwidth=20, relief='ridge')
movie_poster.place(x=250, y=140)
im = Image.open('resource/output/small_bookmark.png')
im = im.resize((150, 200))
movie_poster.img = ImageTk.PhotoImage(im)
movie_poster['image'] = movie_poster.img

# 텍스트 - 영화 상세 정보 담는 텍스트함
TempFont = font.Font(movie_ranking_frame, size=10, weight='bold', family='Malgun Gothic')
movie_imformation_text = Text(movie_ranking_frame, width=35, height=12, borderwidth=20, relief='ridge',
                              font=TempFont, bg='#F6D8CE')
movie_imformation_text.pack()
movie_imformation_text.place(x=460, y=140)
movie_imformation_text.configure(state='disabled')


def makegraph():
    plt.rc('font', family='Malgun Gothic')
    plt.rc('axes', unicode_minus=False)
    plt.rcParams["font.size"] = 10
    plt.rcParams['xtick.labelsize'] = 10.
    plt.rcParams['ytick.labelsize'] = 10.
    df = DataFrame(movie_ranking)
    df = df.filter(items=['rnum', 'movieNm', 'audiAcc', 'audiCnt'])
    df = df.astype({'audiAcc': int, 'audiCnt': int})

    plt.figure()
    X = numpy.arange(10)
    plt.bar(X + 0.3, df['audiCnt'], color='g', width=0.25, label='금일관람객')
    plt.bar(df['rnum'] + '위', df['audiAcc'], color='r', width=0.25, label='누적관람객')
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
MovieStorySearchButton = Button(movie_ranking_frame, image=image[5], command=makegraph, bg='#F6D8CE')
MovieStorySearchButton.pack()
MovieStorySearchButton.place(x=720, y=3)












# 페이지-영화 상세 정보 생성
movie_information_frame = Frame(window)
notebook.add(movie_information_frame, text="페이지2", image=image[1])
movie_information_frame.configure(bg='#F79F81')

# 폰트
TempFont = font.Font(movie_information_frame, size=20, weight='bold', family='Malgun Gothic')
search_movie_list = []


def search_movie():
    global movie_Text, search_movie_list
    search_movie_list.clear()
    search_movie_list = getData2(movie_InputLabel.get())
    movie_list_box.delete(0, movie_list_box.size())
    for i in range(len(search_movie_list)):
        movie_list_box.insert(10, search_movie_list[i]['title'])

save_bookmark = pd.read_csv('sample.csv')

def bookmark():
    global save_bookmark,cnt
    num = movie_list_box.curselection()
    i = int(num[0])
    save_bookmark= save_bookmark.append(search_movie_list[i] ,ignore_index=True)
    save_bookmark.to_csv('sample.csv')
    save_bookmark = pd.read_csv('sample.csv')
    bookmark_movie_list_box.delete(0,bookmark_movie_list_box.size())
    for i in range(len(save_bookmark)):
        bookmark_movie_list_box.insert(10, save_bookmark.iloc[i]['title'])


def SearchMovieInfo():
    global ima, movie_information_poster
    num = movie_list_box.curselection()
    i = int(num[0])
    movie_list_score_show_box.configure(state='normal')
    movie_list_score_show_box.delete('1.0', END)
    movie_list_score_show_box.insert(INSERT, search_movie_list[i]['title'])
    movie_list_score_show_box.insert(INSERT, "\n")
    movie_list_score_show_box.insert(INSERT, "개봉일: ")
    movie_list_score_show_box.insert(INSERT, search_movie_list[i]['개봉일'])
    movie_list_score_show_box.insert(INSERT, " ")
    movie_list_score_show_box.insert(INSERT, "\n")
    movie_list_score_show_box.insert(INSERT, "배우: ")
    movie_list_score_show_box.insert(INSERT, search_movie_list[i]['배우'])
    movie_list_score_show_box.insert(INSERT, "\n")
    movie_list_score_show_box.insert(INSERT, "유저평점: ")
    movie_list_score_show_box.insert(INSERT, search_movie_list[i]['유저평점'])
    movie_list_score_show_box.insert(INSERT, "\n")
    movie_list_score_show_box.insert(INSERT, "기자 평론가 평점: ")
    movie_list_score_show_box.insert(INSERT, search_movie_list[i]['기자평점'])
    movie_list_story_show_box.configure(state='normal')
    movie_list_story_show_box.delete('1.0', END)
    movie_list_story_show_box.insert(INSERT, "줄거리 : %s \n" % search_movie_list[i]['줄거리'])
    movie_list_score_show_box.insert(INSERT, "\n")
    movie_list_story_show_box.insert(INSERT, "네이버 링크 : %s" % search_movie_list[i]['링크'])

    ima = Image.open('%s.jpg' % search_movie_list[i]['title'])
    ima = ima.resize((160, 210))
    movie_information_poster.img = ImageTk.PhotoImage(ima)
    movie_information_poster['image'] = movie_information_poster.img


# 왼쪽의  영화 찾기 글씨
movie_Text = Label(movie_information_frame, font=TempFont, text="[영화 찾기]")
movie_Text.pack()
movie_Text.place(x=10)
movie_Text.configure(bg='#F79F81')

# 영화 리스트 박스
TempFont = font.Font(movie_information_frame, size=10, weight='bold', family='Malgun Gothic')

movie_list_box = Listbox(movie_information_frame, font=TempFont, activestyle='none',
                         width=30, height=18, borderwidth=20, relief='ridge')
movie_list_box.pack()
movie_list_box.place(x=10, y=120)
movie_list_box.configure(bg='#F6D8CE')

# 영화 입력 받기 라벨
TempFont = font.Font(movie_information_frame, size=20, weight='bold', family='Malgun Gothic')
movie_InputLabel = Entry(movie_information_frame, font=TempFont, width=20, borderwidth=10, relief='ridge')
movie_InputLabel.pack()
movie_InputLabel.place(x=280, y=0)
movie_InputLabel.configure(bg='#F79F81')

# 영화 정보 상세 검색 버튼
TempFont = font.Font(movie_information_frame, size=12, weight='bold', family='Malgun Gothic')
MovieStorySearchButton = Button(movie_information_frame, font=TempFont, text="상세검색", command=SearchMovieInfo)
MovieStorySearchButton.pack(side=LEFT)
MovieStorySearchButton.place(x=120, y=500)

# 영화 검색 버튼
movie_SearchButton = Button(movie_information_frame, font=TempFont, text="검색", command=search_movie, image=image[6],
                            bg='#F6D8CE')
movie_SearchButton.pack()
movie_SearchButton.place(x=650, y=3)

# 북마크  버튼
MovieBookMarkButton = Button(movie_information_frame, image=image[8], command=bookmark, bg='#F6D8CE')
MovieBookMarkButton.pack()
MovieBookMarkButton.place(x=720, y=3)

# 영화 정보 포스터 박스
movie_information_poster = Label(movie_information_frame, width=160, height=210, borderwidth=20, relief='ridge')
movie_information_poster.place(x=310, y=110)
ima = Image.open('resource/output/small_bookmark.png')
ima = ima.resize((160, 210))
movie_information_poster.img = ImageTk.PhotoImage(ima)
movie_information_poster['image'] = movie_information_poster.img

# 영화 평점 정보 출력 박스
TempFont = font.Font(movie_information_frame, size=15, weight='bold', family='Malgun Gothic')
movie_list_score_show_box = Text(movie_information_frame, width=18, height=7, borderwidth=20, relief='ridge',
                                 font=TempFont, bg='#F6D8CE')
movie_list_score_show_box.pack()
movie_list_score_show_box.place(x=530, y=110)
movie_list_score_show_box.configure(state='disabled')

# 영화 줄거리 정보 출력 박스
TempFont = font.Font(movie_information_frame, size=11, weight='bold', family='Malgun Gothic')
movie_list_story_show_box = Text(movie_information_frame, width=48, height=7, borderwidth=20, relief='ridge',
                                 font=TempFont, bg='#F6D8CE')
movie_list_story_show_box.pack()
movie_list_story_show_box.place(x=310, y=370)
movie_list_story_show_box.configure(state='disabled')












# 페이지 -영화관 지도 생성
movie_map_frame = Frame(window)
notebook.add(movie_map_frame, image=image[2])
movie_map_frame.configure(bg='#F79F81')
select_map_list = None


def showmap():
    global select_map_list
    num = map_list_box.curselection()
    i = int(num[0])
    x = select_map_list['좌표정보(X)'].iloc[i]
    y = select_map_list['좌표정보(Y)'].iloc[i]
    Pressed(x, y)


def searchmap():
    global select_map_list
    m = map_InputLabel.get()
    movie_map.filter(items=['번호', '소재지전체주소', '사업장명', '좌표정보(X)', '좌표정보(Y)'])
    contains_korea_or_japan = movie_map['소재지전체주소'].str.contains("%s" % m)
    subset_df = movie_map[contains_korea_or_japan]
    subset_df = subset_df.filter(items=['소재지전체주소', '사업장명', '좌표정보(X)', '좌표정보(Y)'])
    map_list_box.delete(0, map_list_box.size())
    select_map_list = subset_df

    for i in range(len(subset_df)):
        map_list_box.insert(10, subset_df['사업장명'].iloc[i] + "-" + subset_df['소재지전체주소'].iloc[i])


# 맵 리스트 박스
TempFont = font.Font(movie_map_frame, size=10, weight='bold', family='Malgun Gothic')

map_list_box = Listbox(movie_map_frame, font=TempFont, activestyle='none',
                       width=52, height=18, borderwidth=20, relief='ridge')
map_list_box.pack()
map_list_box.place(x=10, y=120)
map_list_box.configure(bg='#F6D8CE')

# 폰트
TempFont = font.Font(movie_map_frame, size=20, weight='bold', family='Malgun Gothic')

# 왼쪽의  영화관 찾기 글씨
movie_ranking_Text = Label(movie_map_frame, font=TempFont, text="[영화관 찾기]")
movie_ranking_Text.pack()
movie_ranking_Text.place(x=10)
movie_ranking_Text.configure(bg='#F79F81')

# 지역 입력받기
map_InputLabel = Entry(movie_map_frame, font=TempFont, width=20, borderwidth=10, relief='ridge')
map_InputLabel.pack()
map_InputLabel.place(x=280, y=0)
map_InputLabel.configure(bg='#F79F81')

# 지역 검색 버튼
map_SearchButton = Button(movie_map_frame, font=TempFont, text="검색", command=searchmap, image=image[6], bg='#F6D8CE')
map_SearchButton.pack()
map_SearchButton.place(x=650, y=3)

# 지도출력 버튼
MovieStorySearchButton = Button(movie_map_frame, image=image[7], command=showmap, bg='#F6D8CE')
MovieStorySearchButton.pack()
MovieStorySearchButton.place(x=720, y=3)











# 페이지 - 메일 & 텔레그램
movie_mail_frame = Frame(window)
notebook.add(movie_mail_frame, image=image[3])
movie_mail_frame.configure(bg='#F79F81')



def InitInputGmail():
    global address
    address = StringVar()
    TempFont = font.Font(movie_mail_frame, size=20, weight='bold', family='Malgun Gothic')
    GmailLabel = Entry(movie_mail_frame, textvariable=address, font=TempFont, width=20, borderwidth=10, relief='ridge')
    GmailLabel.pack()
    GmailLabel.place(x=280, y=0)
    GmailLabel.configure(bg='#F79F81')

def SendMail():
    global movie_ranking, address
    address = str(address.get())
    Gmail.SendMail(address, movie_ranking)

InitInputGmail()

# 폰트
TempFont = font.Font(movie_mail_frame, size=20, weight='bold', family='Malgun Gothic')

# 왼쪽의  북마크 글씨
movie_ranking_Text = Label(movie_mail_frame, font=TempFont, text="북마크 \n 메일보내기")

movie_ranking_Text.pack()
movie_ranking_Text.place(x=10)
movie_ranking_Text.configure(bg='#F79F81')

def bookmark_remove():
    global save_bookmark
    num = bookmark_movie_list_box.curselection()
    n = int(num[0])
    save_bookmark= save_bookmark.drop(n,0)
    save_bookmark.to_csv('sample.csv')
    save_bookmark = pd.read_csv('sample.csv')
    bookmark_movie_list_box.delete(0,bookmark_movie_list_box.size())

    for i in range(len(save_bookmark)):
        bookmark_movie_list_box.insert(10, save_bookmark.iloc[i]['title'])

def bookmark_show():
    global bookmark_ima , bookmark_movie_information_poster
    num = bookmark_movie_list_box.curselection()
    i = int(num[0])
    bookmark_movie_list_score_show_box.configure(state='normal')
    bookmark_movie_list_score_show_box.delete('1.0', END)
    bookmark_movie_list_score_show_box.insert(INSERT, save_bookmark.iloc[i]['title'])
    bookmark_movie_list_score_show_box.insert(INSERT, "\n")
    bookmark_movie_list_score_show_box.insert(INSERT, "개봉일: ")
    bookmark_movie_list_score_show_box.insert(INSERT, save_bookmark.iloc[i]['개봉일'])
    bookmark_movie_list_score_show_box.insert(INSERT, " ")
    bookmark_movie_list_score_show_box.insert(INSERT, "\n")
    bookmark_movie_list_score_show_box.insert(INSERT, "배우: ")
    bookmark_movie_list_score_show_box.insert(INSERT, save_bookmark.iloc[i]['배우'])
    bookmark_movie_list_score_show_box.insert(INSERT, "\n")
    bookmark_movie_list_score_show_box.insert(INSERT, "유저평점: ")
    bookmark_movie_list_score_show_box.insert(INSERT, save_bookmark.iloc[i]['유저평점'])
    bookmark_movie_list_score_show_box.insert(INSERT, "\n")
    bookmark_movie_list_score_show_box.insert(INSERT, "기자 평론가 평점: ")
    bookmark_movie_list_score_show_box.insert(INSERT, save_bookmark.iloc[i]['기자평점'])

    bookmark_movie_list_story_show_box.configure(state='normal')
    bookmark_movie_list_story_show_box.delete('1.0', END)
    bookmark_movie_list_story_show_box.insert(INSERT, "줄거리 : %s \n" % save_bookmark.iloc[i]['줄거리'])
    bookmark_movie_list_story_show_box.insert(INSERT, "\n")
    bookmark_movie_list_story_show_box.insert(INSERT, "네이버 링크 : %s" % save_bookmark.iloc[i]['링크'])

    bookmark_ima = Image.open('%s.jpg' % save_bookmark.iloc[i]['title'])
    bookmark_ima = bookmark_ima.resize((160, 210))
    bookmark_movie_information_poster.img = ImageTk.PhotoImage(bookmark_ima)
    bookmark_movie_information_poster['image'] = bookmark_movie_information_poster.img




# 메일 보내기 버튼
mail_send_button = Button(movie_mail_frame, font=TempFont, text="검색", command=SendMail, image=image[9], bg='#F6D8CE')
mail_send_button.pack()
mail_send_button.place(x=650, y=3)

# 북마크 찾기 버튼
bookmark_search_button= Button(movie_mail_frame, image=image[6], command=bookmark_show, bg='#F6D8CE')
bookmark_search_button.pack()
bookmark_search_button.place(x=80, y=500)

# 북마크 제거 버튼
bookmark_remove_button= Button(movie_mail_frame, image=image[10], command=bookmark_remove, bg='#F6D8CE')
bookmark_remove_button.pack()
bookmark_remove_button.place(x=200, y=500)


# 북마크 리스트 박스
TempFont = font.Font(movie_mail_frame, size=10, weight='bold', family='Malgun Gothic')

bookmark_movie_list_box = Listbox(movie_mail_frame, font=TempFont, activestyle='none',
                         width=30, height=18, borderwidth=20, relief='ridge')
bookmark_movie_list_box.pack()
bookmark_movie_list_box.place(x=10, y=120)
bookmark_movie_list_box.configure(bg='#F6D8CE')

for i in range(len(save_bookmark)):
    bookmark_movie_list_box.insert(10, save_bookmark.iloc[i]['title'])


# 북마크 영화 정보 포스터 박스
bookmark_movie_information_poster = Label(movie_mail_frame, width=160, height=210, borderwidth=20, relief='ridge')
bookmark_movie_information_poster.place(x=310, y=110)
bookmark_ima = Image.open('resource/output/small_bookmark.png')
bookmark_ima = bookmark_ima.resize((160, 210))
bookmark_movie_information_poster.img = ImageTk.PhotoImage(bookmark_ima)
bookmark_movie_information_poster['image'] = movie_information_poster.img


# 북마크 영화 평점 정보 출력 박스
TempFont = font.Font(movie_information_frame, size=15, weight='bold', family='Malgun Gothic')
bookmark_movie_list_score_show_box = Text(movie_mail_frame, width=18, height=7, borderwidth=20, relief='ridge',
                                 font=TempFont, bg='#F6D8CE')
bookmark_movie_list_score_show_box.pack()
bookmark_movie_list_score_show_box.place(x=530, y=110)
bookmark_movie_list_score_show_box.configure(state='disabled')


# 북마크 영화 줄거리 정보 출력 박스
TempFont = font.Font(movie_information_frame, size=11, weight='bold', family='Malgun Gothic')
bookmark_movie_list_story_show_box = Text(movie_mail_frame, width=48, height=7, borderwidth=20, relief='ridge',
                                 font=TempFont, bg='#F6D8CE')
bookmark_movie_list_story_show_box.pack()
bookmark_movie_list_story_show_box.place(x=310, y=370)
bookmark_movie_list_story_show_box.configure(state='disabled')

window.mainloop()
