#산술 연산을 하는 문자열과 숫자의 상호 변환
'''
s1, s2, s3 = "100", "100.23", "999999999999999999999999999"
print(int(s1) + 1, float(s2) + 1, int(s3) + 1)
'''

#산술연산자와 대입연산자
'''
a  = 100; b = 100.123
print(str(a) + '1', str(b) + '1')
a = 10
a += 3
print(a)
'''
##거스름돈
'''
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = int(input("교환할 돈은 얼마\n"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("500원 짜리 ==>", "%d개" % c500)
print("100원 짜리 ==>", "%d개" % c100)
print("50원 짜리 ==>",  "%d개" % c50)
print("10원 짜리 ==>",  "%d개" % c10)
print(" 바꾸지 못한 잔돈 ==> %d원\n" % money)
'''