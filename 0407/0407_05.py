class Student:
    
    phone = "" # 인스턴스 변수
    count = 0 # 클래스 변수

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = 0
        self.avg = 0
        self.rank = 0
        Student.count += 1 

    def calc_total(self):
        self.total = self.kor + self.eng + self.math

    def calc_avg(self): 
        self.calc_total() # total 계산 후
        self.avg = self.total / 3

    def s_print(self):
        self.calc_avg() # 출력 전 평균 계산
        print(self.name, self.kor, self.eng, self.math, self.total, self.avg, self.rank)

s = Student("홍길동", 100, 100, 100)
s.s_print()
print("현재 생성된 학생 수 : ", Student.count)
s2 = Student("이순신", 90, 90, 90)
s2.s_print()
print("현재 생성된 학생 수 : ", Student.count)
