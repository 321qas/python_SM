"""
a = 100
b = 50
# 두 변수의 값 교체

c = a
a = b
b = c

#or
a, b = b, a
print(a,b)
"""

#입력

#print(input("숫자를 입력하세요 :"))
a = (input("숫자를 입력하세요 : "))
b = (input("숫자를 입력하세요 : "))
#타입변경
a = int(a)
b = int(b)
print(a+b)
