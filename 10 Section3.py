'''
from tkinter import *
window = Tk()

btnList = [None] * 3

for i in range(0, 3) :
    btnList[i] = Button(window, text = "버튼" + str(i + 1))

for btn in btnList :
    btn.pack(side = TOP, fill = X, ipadx = 20, ipady = 20 )

window.mainloop()
'''
'''
from tkinter import *
import random

## 변수 선언 부분 ##
btnList = [""] * 9
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"]
photoList=[None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

for i in range(0, 9) :

    photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])
    random.shuffle(photoList)



for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
'''

from tkinter import *
from time import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

photoList = [None] * 9
num = 0

def clickNext() :
    global num
    num += 1
    if num  > 8 :
        num = 0
    photo = PhotoImage(file = "gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file = "gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickText() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file = "gif/" + fnameList[""])
    pLabel.configure(image = photo)
    pLabel.image = photo


window  = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnText = Label(window, text = "", command = clickText)
btnNext = Button(window, text = "다음>>", command = clickNext)


photo = PhotoImage(file = "gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()