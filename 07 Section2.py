'''
aa = []

for i in range(0, 10) :
    aa.append(0)
    hap = 0

for i in range(0, 10) :
    aa[i] = int(input(str(i + 1) + "번째 숫자 :"))

for i in range(0, 10) :
    hap = hap + aa[i]
print("합계 ==> %d" % hap)
'''
'''

aa = []
bb = []
value = 0

for i in range(0, 200) :
    aa.append(value)
    value *= 3

for i in range(0, 200) :
    bb.append(aa[99 - i])

print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." % (bb[0], bb[199]))
'''
'''
aa = [10, 20, 30,40]
print("aa[-1]은 %d, a[-2]는 %d" % (aa[-1], aa[-2]))
'''
'''
aa = [10, 20, 30, 40, 50]
aa = []
aa = None
print(aa)
'''

myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)

myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)

print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop()후의 리스트 : %s" %myList)

myList.sort()
print("sort() 후의 리스트 : %s" % myList)

myList.reverse()
print("reverse()후의 리스트 : %s" % myList)

print("20값의 위치 : %d" % myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s" % myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s" % myList)

myList.extend([77, 88, 77])
print("extend([77, 88, 77] 후의 리스트 : %s" % myList)

myList = [30, 10, 20]
newList = sorted(myList)
print("sorted() 후의 myList : %s :" % myList)
print("sorted() 후의 newList : %s: " % newList)

print("77값의 개수 : %d" % myList.count(77))