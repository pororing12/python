'''
fruit = ['사과', '배', '참외', '수박']
print(fruit)
fruit.append('귤')
print(fruit)

if '딸기' in fruit :
    print("딸기가 있네요")
else :
    print("딸기가 없네요~")
'''
##Code05 - 10
'''
import random

numbers = []
for num in range(0, 10) :
    numbers.append(random.randrange(0, 10))

print("생성된 리스트", numbers)

for num in range(0, 10) :
    if num not in numbers :
        print("숫자 %d는 리스트에 없네요."% num)
'''
Select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

Select = int(input("1. 입력한 수식 계산, 2.두 수 사이의 합계 : "))

if Select == 1 :
    numStr = input("*** 수식을 입력하세요")
    answer = eval(numStr)
    print("%s 결과는 %5.1f 입니다." % (numStr, answer))

elif Select == 2:
    num1 = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요 : "))
    for i in range(num1, num2 + 1) :
        answer = answer + i
    print("%d + ... + %d는 %d입니다." % (num1, num2, answer))
else :
    print("1또는 2를 입력해야 합니다.")