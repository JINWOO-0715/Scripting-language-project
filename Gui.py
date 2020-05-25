from tkinter import *
from tkinter import font
import tkinter.messagebox

window = Tk()
window.geometry("800x700")

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="[서울시 영화 검색 App]")
    MainText.pack()
    MainText.place(x=250)


def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "영화관")
    SearchListBox.insert(2, "영화차트")
    SearchListBox.insert(3, "영화검색")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=180, y=48)



InitTopText()
InitSearchListBox()
InitInputLabel()
window.mainloop()


