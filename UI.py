from tkinter import *
from tkinter import font
import tkinter.ttk
from ReadFile import *
from Naver_Crowling import *
from pandas import DataFrame
import pandas
import matplotlib.pyplot as plt
import numpy

def callback(event):
    print("clicked at", event.x, event.y)


window=Tk()
window.title("서울시 영화 정보 검색")

window.bind("<Button-1>" , callback)

notebook=tkinter.ttk.Notebook(window, width=800, height=600 )
notebook.pack()

image = []
image.append( PhotoImage(file='resource/output/rank_icon.png'))
image.append( PhotoImage(file='resource/output/search.png'))
image.append( PhotoImage(file='resource/output/map.png'))
image.append( PhotoImage(file='resource/output/gmail-icon.png'))
image.append( PhotoImage(file='resource/output/boxoffice.png'))

movie_ranking = Movie().crawl_movie()
movie_map = Seoul().crawl_movie()


#검색 버튼 기능
def SearchButtonAction():
    s = day_InputLabel.get()
    movie_ranking = Movie().crawl_movie(s)

    movie_ranking_list_box.delete(0,9)
    for i in movie_ranking:
        movie_ranking_list_box.insert(10, "[" + i['rank'] + "위]" + i['movieNm'])

#함수 - 영화 상세 정보  함수
def SearchMovieStory():
    movie_imformation_text.configure(state='normal')
    num = movie_ranking_list_box.curselection()
    i=int(num[0])
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
    image.append('%s.jpg', % movie_ranking[i]['movieNm'])
    label1 = Label(window, image=image[5])
    label1.pack(side=RIGHT)
    label1.place(x=500, y=0)
    label1.configure(bg='#F6D8CE')

#박스오피스 그림 라벨


#랭킹 페이지 생성
movie_ranking_frame=Frame(window)
notebook.add(movie_ranking_frame, text="페이지1",image=image[0])
movie_ranking_frame.configure(bg = '#F79F81')

# 페이지-영화 상세 정보 생성
movie_information_frame=Frame(window)
notebook.add(movie_information_frame, text="페이지2" ,image=image[1])
label1=Label(movie_information_frame, text="영화 상세 정보 생성", fg='red', font='helvetica 48')
label1.pack()


# 페이지 -영화관 지도 생성
movie_map_frame =Frame(window)
notebook.add(movie_map_frame,image=image[2])
label1=Label(movie_map_frame, text="영화관 지도", fg='red', font='helvetica 48')
label1.pack()


#페이지 - 메일 & 텔레그램
movie_mail_frame =Frame(window)
notebook.add(movie_mail_frame,image=image[3])
label1=Label(movie_mail_frame, text="메일 텔레그램", fg='red', font='helvetica 48')
label1.pack()


#폰트
TempFont = font.Font(movie_ranking_frame, size=20, weight='bold', family='Malgun Gothic')


#왼쪽의 일간 박스 오피스 글씨
movie_ranking_Text = Label(movie_ranking_frame, font = TempFont , text = "[일간 박스오피스]")
movie_ranking_Text.pack()
movie_ranking_Text.place(x=10)
movie_ranking_Text.configure(bg = '#F79F81')

#날짜 입력 받기
day_InputLabel = Entry(movie_ranking_frame, font=TempFont, width=20, borderwidth=10, relief='ridge')
day_InputLabel.pack()
day_InputLabel.place(x=280 , y =0)
day_InputLabel.configure(bg = '#F79F81')



#검색 버튼 생성
SearchButton = Button(movie_ranking_frame, font=TempFont, text="검색", command=SearchButtonAction ,image=image[1])
SearchButton.pack()
SearchButton.place(x=650, y=0)

#리스트박스 - 영화 랭킹
movie_ranking_list_box = None
TempFont = font.Font(movie_ranking_frame, size=10, weight='bold', family='Malgun Gothic')
movie_ranking_list_box = Listbox(movie_ranking_frame, font=TempFont, activestyle='none',
                                 width=21, height=11, borderwidth=20, relief='ridge')
movie_ranking_list_box.pack()
movie_ranking_list_box.place(x=10, y=140)
movie_ranking_list_box.configure(bg='#F6D8CE')
for i in movie_ranking:
    movie_ranking_list_box.insert(10, "[" + i['rank'] + "위]" + i['movieNm'])



#영화 포스터 라벨

movie_poster=Label(movie_ranking_frame , width=200, height=200, borderwidth=20,  image =image[0] ,relief='ridge' , font=TempFont)
movie_poster.pack()
movie_poster.place(x=250 , y=140)
label1.configure(bg = '#F6D8CE' )


#버튼 - 상세검색
TempFont = font.Font(movie_ranking_frame, size=12, weight='bold', family='Consolas')
MovieStorySearchButton = Button(movie_ranking_frame, font=TempFont, text="상세검색", command=SearchMovieStory)
MovieStorySearchButton.pack(side =LEFT)
MovieStorySearchButton.place(x=120, y=410)


#텍스트 - 영화 상세 정보 담는 텍스트함
TempFont = font.Font(movie_ranking_frame, size=10, weight='bold', family='Malgun Gothic')
movie_imformation_text = Text(movie_ranking_frame, width=21, height=11, borderwidth=20, relief='ridge',
                                   font=TempFont)
movie_imformation_text.pack()
movie_imformation_text.place(x=550, y=140)
movie_imformation_text.configure(state='disabled')








window.mainloop()