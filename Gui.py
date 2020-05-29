from tkinter import *
from tkinter import font
from ReadFile import *
import tkinter.messagebox

DataList = []


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x800")
        self.InitTopText()
        self.InitSearchListBox()
        self.InitInputLabel()
        self.InitSearchButton()
        self.InitRenderText()
        self.InputLabel

    def InitTopText(self):
        TempFont = font.Font(self.window, size=20, weight='bold', family='Consolas')
        self.MainText = Label(self.window, font=TempFont, text="[서울시 영화관 검색 App]")
        self.MainText.pack()
        self.MainText.place(x=250)

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

    def InitInputLabel(self):
        TempFont = font.Font(self.window, size=15, weight='bold', family='Consolas')
        self.InputLabel = Entry(self.window, font=TempFont, width=22, borderwidth=12, relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=180, y=50)

    def InitSearchButton(self):
        TempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
        SearchButton = Button(self.window, font=TempFont, text="검색", command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=480, y=52)

    def InitMailButton(self):
        TempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
        SearchButton = Button(self.window, font=TempFont, text="메일")
        SearchButton.pack()
        SearchButton.place(x=520, y=52)

    def InitRenderText(self):
        RenderTextScrollbar = Scrollbar(self.window)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(self.window, size=10, family='Consolas')


#지도 그릴 텍스트
        self.movie_ranking_text = Text(self.window, width=40, height=20, borderwidth=12, relief='ridge',
                                  yscrollcommand=RenderTextScrollbar.set)
        self.movie_ranking_text.pack()
        self. movie_ranking_text.place(x=400, y=140)
        RenderTextScrollbar.config(command=self.movie_ranking_text.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        self.movie_ranking_text.configure(state='disabled')

        # 영화 텍스트
        self.movie_ranking_text = Text(self.window, width=40, height=20, borderwidth=12, relief='ridge',
                                  yscrollcommand=RenderTextScrollbar.set)
        self.movie_ranking_text.pack()
        self.movie_ranking_text.place(x=10, y=140)
        RenderTextScrollbar.config(command=self.movie_ranking_text.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        self. movie_ranking_text.configure(state='disabled')


        self.movie_imformation_text = Text(self.window, width=40, height=20, borderwidth=12, relief='ridge',
                                      yscrollcommand=RenderTextScrollbar.set)
        self. movie_imformation_text.pack()
        self.movie_imformation_text.place(x=10, y=450)
        RenderTextScrollbar.config(command=self.movie_ranking_text.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        self.movie_imformation_text.configure(state='disabled')

        self. movie_favorites_list_text = Text(self.window, width=40, height=20, borderwidth=12, relief='ridge',
                                         yscrollcommand=RenderTextScrollbar.set)
        self. movie_favorites_list_text.pack()
        self.movie_favorites_list_text.place(x=400, y=450)
        RenderTextScrollbar.config(command=self.movie_ranking_text.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        self.movie_favorites_list_text.configure(state='disabled')

    def SearchButtonAction(self):


        movie_ranking = Movie().crawl_movie(int(self.InputLabel.get()))
        self.movie_ranking_text.configure(state='normal')
        for i in movie_ranking:
            self.movie_ranking_text.insert(INSERT,(i['rank'], i['movieNm'], i['openDt'], i['audiAcc']))
            self.movie_ranking_text.insert(INSERT, "\n")

        pass

    def SearchLibrary(self):
        pass

    def RunGui(self):

        self.window.mainloop()
