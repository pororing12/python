'''
myList = [1, 2, 3, 4, 5]
'3,4 줄 합친 Code == {myList = list(map(lambda num : num + 10, myList))}'
add10 = lambda num : num + 10
myList = list(map(add10, myList))
print(myList)
'''
'='
'''
myList = 1, 2, 3, 4, 5]
def add10(num) :
    return num + 10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])
print(myList)
'''
'''
def selfCall() :
    print('하', end = '')
    selfCall()
selfCall()
'''

'''
def factorial(num) :
    if num <= 1 :
        return num
    else :
        return num * factorial(num - 1)
print(factorial(24))
'''
'''
def genFunc() :
    yield 1
    yield 2
    yield 3
print(list(genFunc()))
'''
'''
def genFunc(num) :
    for i in range(0, num) :
        yield i
        print('제네레이터 진행 중 ')
for data in genFunc(5) :
    print(data)
'''

