# 함수사용
# - 1. 중복된 코드의 재사용
# - 2. 소스의 가독성 증대



# 화면출력 함수선언
def stu_print():
    print("[ 학생성적 프로그램 ]")
    print("-" * 40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("0. 프로그램 종료")
    print("-" * 40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    return choice


# 학생성적입력 함수선언
def stu_input(count, students):
    no = count
    name = input(f"{no}번 학생이름을 입력하세요.>> ")
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    total = kor + eng + math
    avg = total / 3
    rank = 0
    students.append({"no": no, "name": name, "kor": kor, "eng": eng, "math": math, "total": total, "avg": avg, "rank": rank})
    print(f"{no}번 {name}학생이 등록되었습니다.")
    print()
    count += 1
    return count

# 학생성적출력 함수선언
def stu_output(title, students):
    print("[ 학생성적 출력 ]")
    print("-" * 60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-" * 60)
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()

# 등수처리 함수선언
def stu_rank(students):
    print("[ 등수처리 ]")
    for s in students:
        num = 1
        for ss in students:
            if s['total'] < ss['total']:  # 등수비교
                num += 1  # 등수1증가
        s['rank'] = num  # 등수입력
    print("\n등수처리가 완료되었습니다.")
    print()

# 학생성적수정 함수선언
def stu_modify(students):
    print("[ 학생성적 수정 ]")
    no = int(input("수정할 학생의 번호를 입력하세요.>> "))
    for s in students:
        if s['no'] == no:
            print(f"{s['name']} 학생의 성적을 수정합니다.")
            s['kor'] = int(input("국어점수를 입력하세요.>> "))
            s['eng'] = int(input("영어점수를 입력하세요.>> "))
            s['math'] = int(input("수학점수를 입력하세요.>> "))
            s['total'] = s['kor'] + s['eng'] + s['math']
            s['avg'] = s['total'] / 3
            print(f"{s['name']} 학생의 성적이 수정되었습니다.")
            print()
            return
    print("해당 번호의 학생이 없습니다.")
    print()



# ---------------------------------------------------------------------------------------------


# 메인 프로그램
def main():
    students = []
    count = 1
    title = ["번호", "이름", "국어", "영어", "수학", "총점", "평균", "등수"]

    while True:
        choice = stu_print()
        if choice == 1:
            count = stu_input(count, students)
        elif choice == 2:
            stu_output(title, students)
        elif choice == 3:
            stu_modify(students)
        elif choice == 4:
            stu_rank(students)
        elif choice == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
            print()

if __name__ == "__main__":
    main()