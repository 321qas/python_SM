students = []

def add_student():
    no = len(students) + 1
    name = input("이름을 입력하세요: ")
    kor = int(input("국어 점수를 입력하세요: "))
    eng = int(input("영어 점수를 입력하세요: "))
    math = int(input("수학 점수를 입력하세요: "))
    total = kor + eng + math
    avg = total / 3
    rank = 0  # 초기값, 나중에 계산 가능
    student = [no, name, kor, eng, math, total, avg, rank]
    students.append(student)
    print(f"{name} 학생의 정보가 추가되었습니다.\n")

def display_students():
    if not students:
        print("등록된 학생이 없습니다.\n")
        return

    print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
    for student in students:
        print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\t{student[6]:.2f}\t{student[7]}")
    print()

def modify_student():
    name = input("수정할 학생의 이름을 입력하세요: ")
    for student in students:
        if student[1] == name:
            print(f"{name} 학생의 현재 점수: 국어 {student[2]}, 영어 {student[3]}, 수학 {student[4]}")
            student[2] = int(input("새로운 국어 점수를 입력하세요: "))
            student[3] = int(input("새로운 영어 점수를 입력하세요: "))
            student[4] = int(input("새로운 수학 점수를 입력하세요: "))
            student[5] = student[2] + student[3] + student[4]
            student[6] = student[5] / 3
            print(f"{name} 학생의 정보가 수정되었습니다.\n")
            return
    print("해당 이름의 학생을 찾을 수 없습니다.\n")

def delete_student():
    name = input("삭제할 학생의 이름을 입력하세요: ")
    for student in students:
        if student[1] == name:
            students.remove(student)
            print(f"{name} 학생의 정보가 삭제되었습니다.\n")
            return
    print("해당 이름의 학생을 찾을 수 없습니다.\n")

def sort_students():
    print("1. 이름순 정렬")
    print("2. 총점순 정렬")
    choice = input("정렬 기준을 선택하세요: ")
    if choice == "1":
        students.sort(key=lambda x: x[1])
        print("이름순으로 정렬되었습니다.\n")
    elif choice == "2":
        students.sort(key=lambda x: x[5], reverse=True)
        print("총점순으로 정렬되었습니다.\n")
    else:
        print("잘못된 입력입니다.\n")

def search_student():
    name = input("검색할 학생의 이름을 입력하세요: ")
    for student in students:
        if student[1] == name:
            print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\t{student[6]:.2f}\t{student[7]}")
            print()
            return
    print("해당 이름의 학생을 찾을 수 없습니다.\n")

def main():
    while True:
        print("1. 학생 추가")
        print("2. 학생 목록 출력")
        print("3. 학생 성적 수정")
        print("4. 학생 삭제")
        print("5. 학생 정렬")
        print("6. 학생 검색")
        print("7. 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            modify_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            sort_students()
        elif choice == "6":
            search_student()
        elif choice == "7":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.\n")

if __name__ == "__main__":
    main()
