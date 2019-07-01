'''
from tkinter import *
from tkinter import messagebox
def myFunc() :
    messagebox.showinfo("강아지 버튼", "고양이 귀엽죠?")

window = Tk()

photo = PhotoImage(file = "gif/cat.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.title("윈도우 창 연습")
window.resizable(width = FALSE, height = FALSE)
window.mainloop()
'''
'''
from tkinter import*
from tkinter import messagebox
window = Tk()

def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졋어요")
    else :
        messagebox.showinfo("", "체크버튼이 커졌어요")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()
'''

from tkinter import *
window = Tk()

def myFunc() :
    if var.get() == 1 :
        label1.configure(text = "파이썬")
    elif var.get() == 2 :
        label1.configure(text = "C++")
    else :
        label1.configure(text = "java")

var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text =  "C++", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc)

label1 = Label(window, text  = "선택한 언어",  fg = "red")

rb1.pack(side = LEFT)
rb2.pack(side = LEFT)
rb3.pack(side = LEFT)
label1.pack()

window.mainloop()