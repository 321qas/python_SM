a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))
str_1 = "{} + {} = {}".format(a,b,a+b)
str_2 = "{} - {} = {}".format(a,b,a-b)
str_3 = "{} * {} = {}".format(a,b,a*b)
str_4 = "{} / {} = {:.2f}".format(a,b,a/b)

print("",str_1,"\n",str_2,"\n",str_3,"\n",str_4)

c = int(input("국어 점수를 입력 : "))
d = int(input("영어 점수를 입력 : "))
e = int(input("수학 점수를 입력 : "))
f = c + d + e
g = f / 3
str_5 = "({} + {} + {}) / {} = {:.2f}(평균)".format(c,d,e,3,g)
print("평균 = 총점 / 과목수\n",str_5)
 
# print("총점 : ",f, "평균 : ", "%.1f" % g)

