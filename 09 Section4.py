

'''
def multi(v1, v2) :
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

myList = []
hap, sub = 0, 0

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
print("multi()에서 돌려준 값 ==> %d, %d" % (hap, sub))
'''

'''
def para_func(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = 0) :
    result = 0
    result = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10
    return result

hap = 0

for i in range(0, 10) :    
    hap = para_func(10, 20)
    print("매개변수가 %d개인 함수를 호출한 결과--> %d" % (i,hap))
hap = para_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과--> %d" % hap)
'''
'''
def dic_func(**para) :
    for k in para.keys() :
        print("%s --> %d명입니다. " % (k, para[k]))

dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)
'''

import random

def getNumber() :
    return random.randrange(1, 46)

lotto = []
num = 0

print("$$ 로또 추첨을 시작합니다. $$\n");

while True :
    num = getNumber()

    if lotto.count(num) == 0 :
        lotto.append(num)
    if len(lotto) >= 6 :
        break

print("추첨된 로또 번호 ==>", end = " ")
lotto.sort()
for i in range(0, 6) :
    print("%d" % lotto[i], end = " ")