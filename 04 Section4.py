if(1234) : print("참이면 보여요")
if(0) : print("거짓이면 안 보여요")

##마음대로 움직이는 거북이
import turtle
import random

swidth, sheight, pSize, exitCount = 300, 300, 3, 0
##변수 7개에 0값을으로 초기화
r, g, b, angle, dist, curX, curY = [0] * 7

##메인코드 부분
turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth,sheight)

while True :
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 150)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    if(-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2) :
        pass
    else :
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitCount += 1
        if exitCount >= 5 :
            break

turtle.done()