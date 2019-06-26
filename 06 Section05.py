'''
a, b , ch = 0, 0, ""
while True :
    a = input("더할 첫 번째 수를 입력하세요")
    if (a == "$") :
        break

    b = int(input("더할 두  번째 수를 입력하세요"))
    ch = input("계산할 연산자를 입력하세요")

    if (ch == "+") :
        print("%d + %d = %d" % (a, b, a + b))
    elif (ch == "-"):
         print("%d - %d = %d" % (a, b, a - b))
    elif (ch == "*"):
         print("%d * %d = %d" % (a, b, a * b))
    elif (ch == "/"):
         print("%d / %d = %d" % (a, b, a / b))
    elif (ch == "%"):
         print("%d % %d = %d" % (a, b, a % b))
    elif (ch == "**"):
         print("%d ** %d = %d" % (a, b, a**b))
    else :
        ("연산자를 잘못 입력하셧습니다")
print("$을 입력해 반복문을 탈출했습니다")
'''
'''
hap, i = 0, 0

for i in range(1, 101) :
    if i % 3 == 0 :
        continue

    hap += i

print("1~100의 합계(3의 배수 제외) : %d" % hap)
'''

i, k = 0, 0

i = 0
while i < 9 :
    if i < 5 :
        k = 0
        while k < 4 - i:
            print( '  ', end = '')
            k += 1
        k = 0
        while k < i * 2 + 1 :
            print('\u2605', end = '')
            k += 1
    else :
        k = 0
        while k < i - 4 :
            print('  ', end = '')
            k += 1
        k = 0
        while k < (9 - i) * 2 - 1 :
            print('\u2605', end = '')
            k += 1

    print()
    i += 1