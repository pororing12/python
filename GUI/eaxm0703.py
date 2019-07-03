#music player
'''
import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
window = Tk()
window.wm_title("MUSIC PLAYER")
window.minsize(500, 500)

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(window, textvariable = v, width = 80)
index = 0
count = 0

global ctr
ctr = 0



label = Label(window, text = "hello world")
label.pack()

window.mainloop()
'''

#OOP tkinter

'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

from tkinter import *
from tkinter import Menu


window = Tk()
window.title("Welcome구이")

def menu_new (event = None ) :
    print("menu new clicked")

def menu_help (event = None) :
    print("menu help")

menu = Menu(window)

file_menu = Menu(menu)
file_menu.add_command(label = "NEW", accelerator = "(Ctrl+N)", underline = 0, command = menu_new)
file_menu.add_separator()
menu.add_cascade(label = 'file', menu = file_menu)

help_menu = Menu(menu)
help_menu.add_command(label = "About", accelerator = "(Ctrl+h)", command = menu_help)
help_menu.add_separator()
menu.add_cascade(label = 'Help', menu = help_menu)

window.config(menu = menu)

window.bind("<Control-n>", menu_new)
window.bind("<Control-h>", menu_help)
window.mainloop()

