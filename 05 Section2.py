#짝수 홀수
'''
a = int(input("정수를 입력하세요"))

if a % 2  == 0 :
   print("짝수입니다")
else :
    print("홀수입니다")
'''
#학점계산
'''
score = int(input("점수를 입력하세요"))

if score >= 95 :
    print('A')
elif score >= 90 :
    print('A0')
elif score >= 85 :
    print('B+')
elif score >= 80 :
    print('B0')
elif score >= 75 :
    print('C+')
elif score >= 70 :
    print('C0')
elif score >= 65 :
    print('D+')
elif score >= 60 :
    print('D0')
else :
    print('F')

    print("학점입니다.")
'''

#삼항연산자
'''
jumsu = 55
res = ''
res = '합격' if jumsu >= 60 else '불합격'

print(res)
'''

import turtle

swidth, sheight = 500, 500

turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.goto(0, -sheight / 2)
turtle.pendown()
turtle.speed(20)

for radius in range(1, 250) :
    if radius % 6 == 0 :
        turtle.pencolor('#faf9f7')
    elif radius % 5 == 0 :
        turtle.pencolor('#db9ae5')
    elif radius % 4 == 0 :
        turtle.pencolor('#6492d3')
    elif radius % 3 == 0 :
        turtle.pencolor('#71bfeb')
    elif radius % 2 == 0 :
        turtle.pencolor('#956edb')
    elif radius % 1 == 0 :
        turtle.pencolor('navyblue')
    else :
        turtle.pencolor('purple')

    turtle.circle(radius)
turtle.done()
