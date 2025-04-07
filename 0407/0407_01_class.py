# 클래스 장점
# 변수, 함수 모두 포함
# 변수에 대한 값을 확인, 비교
# 캡슐화 : 변수에 직접 접근을 막을 수 있음.

# stu = [1,"홍길동", 100 ,100 , 300, 100, 0.1]
# while True:
#     stu[2] = 300
#     print("1. 학생출력")
#     choice =int(input("원하는 번호를 입력하세요.>> "))
#     if choice == 1:
#         print(stu)

# => 리스트는 값 변경이 임의로 가능하다 => 해킹에 취약하다 => class를 사용해서 변수를 보호할 수 있다.

#class 첫글자는 대문자(권장사항)

# s = Stu() # 클래스 선언
# s1 = Stu()

# # 변수넣는법
# s.no = 1
# s.name = "홍길동"
# s.kor = 100

# print(s.no)



class Stu:
    def __init__(self,no,name,kor,eng,math,tot,avg,rank): # 생성자 클래스가 선언될때 데이터를 받아서 변수에 넣는 역할을 한다.
        self.no = no
        self.name = name
        self.kor = kor
        self.__eng = eng # __는 private 변수로 외부에서 접근할 수 없다.
        self.math = math
        self.tot = tot
        self.avg = avg
        self.rank = rank
    
s = Stu(1,"홍길동",200,100,100,300,100,0.1)
print(s.no)

s.eng = 200