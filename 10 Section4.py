'''
from tkinter import *
from tkinter import messagebox

def clickLeft(evet) :
    messagebox.showinfo("마우스", "개에서 마우스가 클릭됨")

window = Tk()

photo = PhotoImage(file = "gif/dog.gif")
label1 = Label(window, image =photo)

label1.bind("<Button>", clickLeft)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()
'''

'''
from tkinter import *

def clickMoust(event) :
    txt = ""
    if event.num == 1 :
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3 :
        txt += "마우스 오른쪽 버튼이 ("

    txt += str(event.y) + "," + str(event.x) + ")에서 클릭됨"
    label1.configure(text = txt)




window  = Tk()
window.geometry("400x400")

label1 = Label(window, text = "이곳이 바뀜")

window.bind("<Button>", clickMoust)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()
'''

from tkinter import *
from tkinter import messagebox

def keyEvent(event) :
    txt = "눌린 키 : shift + "
    if event.keycode == 37:
        txt += "왼쪽 화살표"
    elif event.keycode == 38 :
        txt += "위쪽 화살표"
    elif event.keycode == 39 :
        txt += "오른쪽 화살표"
    elif event.keycode == 40 :
        txt += "아래쪽 화살표"

    messagebox.showinfo("키보드 이벤트",keyEvent)

window = Tk()

window.bind("<Key>", keyEvent)
window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)

window.mainloop()