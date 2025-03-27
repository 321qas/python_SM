#이름입력, 국어, 영어, 수학 점수를 입력받아 총점, 평균을 계산하고 출력하는 프로그램을 작성하시오.


"""
name = input("이름을 입력하세요 : ")
a = int(input("국어 점수를 입력하세요 : "))
b = int(input("영어 점수를 입력하세요 : "))
c = int(input("수학 점수를 입력하세요 : "))

d = a + b + c
e = d / 3

print("이름 : ",name, "총점 : ",d, "평균 : ","%.1f" % e)
"""


print("안녕하세요 \n홍길동입니다.\t만나서 반갑습니다.")

#format() 문자형태 함수
a = 100
b = 50
print("%d / %d = %.2f" % (a,b,a/b))
str_print = "{} / {} = {:.2f}".format(a,b,a/b)
str_print2 = f"{a} / {b} = {a/b:.2f}"
print(str_print)
print(str_print2)
#f함수 = format함수
#f함수는 문자열을 출력할때 변수를 {}로 감싸고, 변수명을 {}안에 넣어서 출력한다.