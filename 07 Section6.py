'''
foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sides = ['오뎅', '단무지', '김치']
for food, side in zip(foods, sides) :
    print(food, '==>', side)
dic = dict(zip(foods, sides))
tupList = list(zip(foods, sides))
print(tupList)
print(dic)
'''
'''
oldList = ['짜장면', '탕수육', '군만두']
newList = oldList
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)
'''

myData = {1,1,1,2,2,2,3,3,3}
myData.add(1)
print(myData)