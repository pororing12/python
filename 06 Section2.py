'''
for i in range(1, 6, 1) :
    print("%d" % i, end = " ")
'''
'''
i, hap = 0, 0
num = 0

num = int(input("갑을 입력하세요 : "))
for i in range(1, num + 1, 1) :
    hap += i
print("1에서 %d까지의 합계 : %d" % (num, hap))
'''

num, i, Line = 0, 0, ""

for i in range(2, 10) :
    Line = Line + ("# %d\t단 #\t\t" % i)

print(Line)

for i in range(2, 10) :
    Line = ""
    for num in range(2, 10) :
        Line = Line + str("%2d X %2d = %2d\t" % (num, i, num * i ))
    print(Line)
