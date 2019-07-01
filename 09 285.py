##날짜 세기 및 요일 구하기
from time import *
from datetime import *

def countDays(date1, date2) :
    retdays = 0
    year, month, day = date1.split('/')
    sDay = date(int(year), int(month), int(day))
    year, month, day = date2.split('/')
    eDay = date(int(year), int(month), int(day))
    diffDays = eDay - sDay
    retDays = diffDays.days
    return retDays

def getDay(t) :
    weeks  = ['월','화','수','목','금','토','일']
    return weeks[t.tm_wday]

startDate, curDate, tm = '', '', None

if __name__ == "__main__" :

    startDate = input('시작 날짜(연/월/일) -->')
    tm = localtime()
    curDate = str(tm.tm_year) + '/' + str(tm.tm_mon) + '/' + str(tm.tm_mday)
    print(startDate, '부터 오늘(', curDate,') 까지는', countDays(startDate, curDate), '일이 지났습니다')
    print('그리고 오늘은', getDay(tm), '요일입니다.')