'''
ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있는지는 않죠 . ^^'
print(ss.count('공부'))
print(ss.find('물론'), ss.rfind('다'), ss.find('공부', 5), ss.find('없다'))
print(ss.index('공부'), ss.rindex('공부'))
'''

'''
ss = input("입력문자열 ==>")
print("출력문자열 ==>", end = "")

if ss.startswith('(') == False :
    print("(", end = "")

print(ss, end = "")
if ss. startswith(')') == False :
    print(")", end = "")
'''

'''
ss = '  파  이  썬  '
print(ss.strip())
print(ss.rstrip())
print(ss.lstrip())
'''
'''
ss = '---파---이---썬'
print(ss.strip('-'))
ss = '<<<파<<이>>썬>>>>'
print(ss.strip('<>'))
'''

'''
ss = 'Python을 열심히 공부 중'
print(ss.split())
ss = '하나:둘:셋'
print(ss.split(':'))
ss = '하나\n둘\n셋'
print(ss.splitlines())
ss = '#'
print(ss.join('no2'))
'''
'''
ss = input("날짜(연/월/일) 입력 ==>")

ssList = ss.split('/')
print("입력한 날짜의 10년 후 ==> ", end = "")
print(str(int(ssList[0]) + 10) + "년", end = "")
print(ssList[1] + "월", end = "")
print(ssList[2] + "일", end = "")
'''
'''
before = ['2019', '12', '31']
ss = list(map(int, before))
print(ss)
'''

'''
def addition(n) :
    return n + n
numbers = (1, 2, 3, 4)
result = map (addition, numbers)
print(list(result))
'''

'''
a = '1234'
print(a.isspace())


inStr = input("문자열 입력")
outStr = ""
if inStr.isalpha() == True :
    print("글자")
elif inStr.isdigit() == True :
    print("숫자")
elif inStr.isalnum() == True :
    print("글자 + 숫자")
else :
    print("모르겠습니다")
'''

import turtle
import random
from tkinter.simpledialog import *

inStr = ''
swidth, sheight = 300, 300
tX, tY, txtSize = [0] * 3

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 슬 문자열을 입력')

for ch in inStr :
    tX = random.randrange(-swidth / 2, swidth / 2)
    tY = random.randrange(-sheight / 2, sheight / 2)
    r = random.random(); g = random.random(); b = random.random()
    txtSize = random.randrange(10, 50)

    turtle.goto(tX, tY)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font = ('맑은 고딕', txtSize, 'bold'))

turtle.done()