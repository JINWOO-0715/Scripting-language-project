from tkinter import *


class MyFrame(Frame):
    def __init__(self, master):
        img = PhotoImage(file='resource/test.png')
        lbl = Label(image=img)
        lbl.image = img  # 레퍼런스 추가
        lbl.place(x=0, y=0)


def main():
    root = Tk()
    root.title('이미지 보기')
    root.geometry('500x400+10+10')
    myframe = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()

from tkinter import *
import tkinter.ttk

window=Tk()
window.title("tkinter notebook")

notebook=tkinter.ttk.Notebook(window, width=800, height=600)
notebook.pack()


frame1=Frame(window)
notebook.add(frame1, text="페이지1",image=img2)


label1=Label(frame1, text="페이지1의 내용", fg='red', font='helvetica 48')
label1.pack()


img3 = PhotoImage(file='resource/output/rank_icon.png')
frame2=Frame(window)
notebook.add(frame2, text="페이지2" ,image=img3)

label2=Label(frame2, text="페이지2의 내용", fg='blue', font='helvetica 48')
label2.pack()


img = PhotoImage(file='resource/output/gmail-icon.png')


frame3=Frame(window)
notebook.add(frame3, text="페이지3",image=img)

label3=Label(frame3, text="페이지3의 내용", fg='green', font='helvetica 48')
label3.pack()


img4 = PhotoImage(file='resource/output/map.png')

frame4=Frame(window)
notebook.insert(2, frame4, text="페이지4",image=img4)

label4=Label(frame4, text="페이지4의 내용", fg='yellow', font='helvetica 48')
label4.pack()

window.mainloop()