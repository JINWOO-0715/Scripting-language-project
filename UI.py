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

#박스오피스 그림 라벨
label1=Label(window, text="랭킹 페이지", fg='red', font='helvetica 48' , image =image[4])
label1.pack(side = RIGHT)
label1.place(x=500, y=0)
label1.configure(bg = '#F6D8CE' )

#랭킹 페이지 생성
movie_ranking_frame=Frame(window)
notebook.add(movie_ranking_frame, text="페이지1",image=image[0])
movie_ranking_frame.configure(bg = '#F79F81')

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
def SearchButtonAction():
    pass
SearchButton = Button(movie_ranking_frame, font=TempFont, text="검색", command=SearchButtonAction ,image=image[1])
SearchButton.pack()

SearchButton.place(x=650, y=0)

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



window.mainloop()