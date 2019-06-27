'''
std = {'학번' : 1000, '이름' : '홍길동', '학과' : '컴퓨터공학과'}
print(std['학과'])
print(std.get('학번'))
print(std.keys())
print(std.values())
print(std.items())
print('이름' in std)
'''
'''

singer = {}

singer['이름'] = '트와이스'
singer['구성원 수 '] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

for k in singer.keys() :
    print('%s ==> %s' % (k, singer[k]))
print(singer.items())
'''

'''
import operator

trainDic = {'Thomas' : '토마스', 'Edward' : '에드워드', 'Henry' : '헨리', 'Gothen' : '고든', 'James' : '제임스'}

trainList = sorted(trainDic.items(), key = operator.itemgetter(1))

print(trainList)
'''
'''
food = {"떡볶이" : "오뎅",
        "짜장면" : "단무지",
        "라면" : "김치",
        "피자" : "피클",
        "맥주" : "땅콩",
        "치킨" : "치킨무",
        "삼겹살" : "상추"};

while (True) :
    myfood = input(str(list(food.keys())) + "주 좋아하는 음식은?")
    if myfood in food :
        print("%s 궁합 음식은 %s입니다." % (myfood, food.get(myfood)))
    elif myfood == "끝" :
        break
    else :
        print("그런음식이 없습니다. 확인해 보세요")
'''
animal = {"닭" : "병아리",
        "개" : "강아지",
        "곰" : "능소니",
        "고등어" : "피클",
        "명태" : "노가리",
        "말" : "말",
        "호랑이" : "개호주"};

while (True) :
    soanimal = input(str(list(animal.keys())) + "중 새끼 이름을 알고 싶은 동물은?")
    if soanimal in animal :
        print("<%s>의 새끼는 <%s>입니다." % (soanimal, animal.get(soanimal)))
    elif soanimal == "끝" :
        break
    else :
        print("그런동물이 없습니다. 확인해 보세요")