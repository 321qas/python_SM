# 순서, 이름, 국어, 영어, 수학, 합계, 평균, 등수를 변수로 두고
# 학생 객체를 생성하여 학생 정보를 저장하고 출력하는 프로그램

count = 1


def __init__(self,no,name,kor,eng,math,total,avg,rank):
    self.no = no
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    count += 1

def __str__(self):
    return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"

class Students:
    def __init__(self):
        self.students = []

    def add(self,s):
    