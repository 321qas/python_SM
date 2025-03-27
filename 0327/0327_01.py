# num1 = int(input("숫자를 입력하세요: "))
# num2 = int(input("숫자를 입력하세요: "))
# print("입력된 숫자 : {},{} / 합계 : {}".format(num1,num2,num1+num2))

#학생성적 프로그램
#이름 국어 영어 수락 입력받아 합계 평균 출력 구현

print("-"*50)
print("학생성적 프로그램")
print("-"*50)
name = input("이름을 입력하세요: ")
a = int(input("국어 성적을 입력하세요 : "))
b = int(input("영어 성적을 입력하세요 : "))
c = int(input("수학 성적을 입력하세요 : "))
print("-"*50)
print("이름\t국어\t영어\t수학")
print("-"*50)
print("{}\t{}\t{}\t{}".format(name,a,b,c))
print("-"*50)
print("합계 : {} 평균 : {:.1f}".format(a+b+c, (a+b+c)/3))
print("-"*50)
