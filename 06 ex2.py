import turtle
import random

## 전역 변수 선언 부분 ##
swidth, sheight, pSize = 300, 300, 3

## 메인 코드 부분 ##
if __name__ == "__main__":
    turtle.title('거북이 소라 그리기')
    turtle.shape('turtle')
    turtle.pensize(pSize)
    turtle.setup(width=swidth + 30, height=sheight + 30)
    turtle.screensize(swidth, sheight)
    turtle.speed(20)

dist = 5
for i in range(1, 80) :
        r = random.random()
        g = random.random()
        b = random.random()
        turtle.pencolor((r, g, b))
        turtle.forward(dist)
        turtle.left(70)
        dist += 1
