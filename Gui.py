from tkinter import *
from tkinter import font
from ReadFile import *
import tkinter.messagebox
import Gmail
from Naver_Crowling import *

DataList = []


def callback(event):
    print("clicked at", event.x, event.y)


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x800")
        self.window.bind("<Button-1>" , callback)
        self.movie_ranking = Movie().crawl_movie()

        self.InitTopText()
        self.InitSearchListBox()
        self.InitInputLabel()
        self.InitSearchButton()
        self.InitMovieRankingText()
        self.InitMovieRankingListBox()

        # gmail 추가
        self.InitMailButton()
        self.InitInputGmail()

#탑 텍스트 초기화
    def InitTopText(self):
        TempFont = font.Font(self.window, size=20, weight='bold', family='Consolas')
        self.MainText = Label(self.window, font=TempFont, text="[서울시 영화관 검색 App]")
        self.MainText.pack()
        self.MainText.place(x=250)
# 찾기 버튼
    def InitSearchListBox(self):
        global SearchListBox
        ListBoxScrollbar = Scrollbar(self.window)
        ListBoxScrollbar.pack()
        ListBoxScrollbar.place(x=150, y=50)

        TempFont = font.Font(self.window, size=15, weight='bold', family='Consolas')
        SearchListBox = Listbox(self.window, font=TempFont, activestyle='none',
                                width=10, height=1, borderwidth=12, relief='ridge',
                                yscrollcommand=ListBoxScrollbar.set)
        SearchListBox.insert(1, "영화차트")
        SearchListBox.insert(2, "영화검색")
        SearchListBox.insert(3, "영화관")
        SearchListBox.pack()
        SearchListBox.place(x=10, y=50)
        ListBoxScrollbar.config(command=SearchListBox.yview)
# 검색어 입력라벨
    def InitInputLabel(self):
        TempFont = font.Font(self.window, size=15, weight='bold', family='Consolas')
        self.InputLabel = Entry(self.window, font=TempFont, width=22, borderwidth=12, relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=180, y=50)
#검색버튼 초기화
    def InitSearchButton(self):
        TempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
        SearchButton = Button(self.window, font=TempFont, text="검색", command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=480, y=52)

    def InitMovieRankingListBox(self):
        self.movie_ranking_list_box =None
        self.movie_ranking_list_box_scrollbar = Scrollbar(self.window)
        self.movie_ranking_list_box_scrollbar.pack()
        self.movie_ranking_list_box_scrollbar.place(x=200, y=140)

        TempFont = font.Font(self.window, size=15, weight='bold', family='Consolas')
        self.movie_ranking_list_box = Listbox(self.window, font=TempFont, activestyle='none',
                                width=25, height=10, borderwidth=12, relief='ridge')

        self.movie_ranking_list_box.pack()
        self.movie_ranking_list_box.place(x=10, y=140)
        self.movie_ranking_list_box_scrollbar.config(command=self.movie_ranking_list_box.yview)
        for i in self.movie_ranking:
            self.movie_ranking_list_box.insert(10,"["+i['rank']+"위]" + i['movieNm'])

    def InitMovieRankingText(self):
        self.movie_information_scrollbar = Scrollbar(self.window)
        self.movie_information_scrollbar.pack()
        self.movie_information_scrollbar.place(x=500, y=450)
        TempFont = font.Font(self.window, size=10, family='Consolas')
        # 영화 텍스트
        self.movie_imformation_text = Text(self.window, width=40, height=20, borderwidth=12, relief='ridge',
                                           yscrollcommand= self.movie_information_scrollbar.set)
        self.movie_imformation_text.pack()
        self.movie_imformation_text.place(x=10, y=450)
        self.movie_information_scrollbar.config(command=self.movie_imformation_text.yview)
        self.movie_information_scrollbar.pack(side=RIGHT, fill=BOTH)
        self. movie_imformation_text.configure(state='disabled')

        #self. movie_favorites_list_text = Text(self.window, width=40, height=20, borderwidth=12, relief='ridge')

    def find(self):
        num =self.movie_ranking_list_box.curselection()
        return num[0]


    def SearchButtonAction(self):# 랭킹 출력함수
        self.movie_imformation_text.configure(state='normal')
        i =int( self.find())

        self.movie_imformation_text.delete('1.0',END)
        self.movie_imformation_text.insert(INSERT, self.movie_ranking[i]['movieNm'])
        self.movie_imformation_text.insert(INSERT, ": ")
        self.movie_imformation_text.insert(INSERT, "\n")
        self.movie_imformation_text.insert(INSERT, "개봉일: ")
        self.movie_imformation_text.insert(INSERT, self.movie_ranking[i]['movieCd'])
        self.movie_imformation_text.insert(INSERT, " ")
        self.movie_imformation_text.insert(INSERT, "\n")
        self.movie_imformation_text.insert(INSERT, "누적 관람객: ")
        self.movie_imformation_text.insert(INSERT, self.movie_ranking[i]['audiAcc'])
        self.movie_imformation_text.insert(INSERT, "\n")
        self.movie_imformation_text.insert(INSERT, "당일 관람객: ")
        self.movie_imformation_text.insert(INSERT, self.movie_ranking[i]['audiCnt'])


    def SearchLibrary(self):
        pass


    def RunGui(self):
        self.window.mainloop()


    def InitMailButton(self):
        TempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
        SearchButton = Button(self.window, font=TempFont, text="메일", command=self.SendMail)
        SearchButton.pack()
        SearchButton.place(x=520, y=52)

    def InitInputGmail(self):
        self.address = StringVar()
        TempFont = font.Font(self.window, size=15, weight='bold', family='Consolas')
        GmailLabel = Entry(self.window, textvariable=self.address, font=TempFont, width=14, borderwidth=12, relief='ridge')
        GmailLabel.pack()
        GmailLabel.place(x=580, y=50)

    def SendMail(self):
        address = str(self.address.get())
        Gmail.SendMail(address, self.movie_ranking)


