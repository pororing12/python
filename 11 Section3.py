'''
inFp = None
inStr = ""

inFp = open("C:/Temp/gugucon.txt", "r")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print(inStr, end = "")

inFp.close()
'''

# 한 번에 모두 읽어 들이기
'''
inFp = None
inList = ""

#inFp = open("C:/Temp/gugucon.txt", "r")
#inList = inFp.readlines()
#print(inList)

#아예 close()함수를 사용하지 않으려면 이렇게 하면된다.
with open("C:/Temp/gugucon.txt", "r") as inFp :
    inList = inFp.readlines()
    print(inList)

inFp.close()
'''

# 한 행씩 출력
'''
inFp = None
inList, inStr = [] , ""

inFp = open("C:/Temp/gugucon.txt", "r")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end = "")

inFp.close()
'''
'''
import os

inFp = None
fName, inList, inStr = "", [],""

fName = input("파일명을 입력하세요 : ")
if os.path.exists(fName) :
    inFp = open(fName, "r")

    inList = inFp.readlines()
    for inStr in inList :
        print(inStr, end = "")

    inFp.close()

else :
    print("%s 파일이 없습니다." % fName)
'''

# 한 행씩 파일에 쓰기
'''
outFp = None
outStr = ""

outFp = open("C:/Temp/data2.txt", "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break

outFp.close()
print("--- 파일에 정상적으로 써졌음 ---")
'''

# 읽기 모드 및 쓰기 모드로 파일을 염
'''
inFp, outFp = None, None
fName, oName, inStr = "", "", ""

fName = input("소스 파일명을 입력하세요 : ")

oName = input("타깃 파일명을 입력하세요 : ")


inFp = open(fName, "r")
outFp = open(oName, "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---- 파일이 정상적으로 복사되었음 ----")
'''

inFp, outFp = None, None
inStr, outStr = "", ""
i = 0
secu = 0

secuYN = input("1. 암호화 2. 암호 해석 중 선택. 3. 종료 :")
inFname = input("입력 파일명을 입력하세요 : ")
outFname = input("출력 파일명을 입력하세요 :")

if secuYN == "1":
    secu = 100
elif secuYN == "2":
    secu = -100

inFp = open(inFname, 'r', encoding='utf-8')
outFp = open(outFname, 'w', encoding='utf-8')

while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr = ""

    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
    outStr = outStr + ch2

outFp.close()
inFp.close()
print('%s --> %s 변환완료' % (inFname, outFname))