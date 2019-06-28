'''
aa = [10, 20, 30, 40, 50]
print(aa[1:3])

ss = '파이썬최고'
print(len(ss))

ss = '파이썬은완전재미있어요'
sslen = len(ss)


for i in range(0, sslen) :
    if i % 2 ==0 :
        print(ss[i], end = "")
    else :
        print("#", end = "")



inStr, outStr = "", ""
count, i = 0, 0
inStr = input("문자열을 입력하세요")
count = len(inStr)

for i in range(0, count) :
    outStr += inStr[count - (i + 1)]
print("내용을 거꾸로 출력 --> %s" % outStr)
'''
