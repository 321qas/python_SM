f = open("student_scores.txt", "w", encoding="utf-8")

print("학생 성적 입력 프로그램 (종료하려면 'x' 입력)")

while True:
    print("[학생 성적 입력]")
    print("-" * 20)
    name = input("학생 이름: ")
    if name.lower() == "x":
        break
    korean = input("국어 성적: ")
    if korean.lower() == "x":
        break
    english = input("영어 성적: ")
    if english.lower() == "x":
        break
    math = input("수학 성적: ")
    if math.lower() == "x":
        break
    f.write(f"이름: {name}, 국어: {korean}, 영어: {english}, 수학: {math}\n")

f.close()
print("입력이 완료되었습니다. 'student_scores.txt' 파일에 저장되었습니다.")


