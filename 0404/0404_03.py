

# 메모장 파일 경로
file_path = "scores.txt" 

# 파일 읽기
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 데이터 정리
data = []
for index, line in enumerate(lines):
    parts = line.strip().split()  # 공백으로 분리
    if len(parts) >= 6:  # 숫자, 이름, 국어, 영어, 수학, 합계가 있는지 확인
        record = {
            "Index": index + 1,
            "Number": parts[0],
            "Name": parts[1],
            "Korean": int(parts[2]),
            "English": int(parts[3]),
            "Math": int(parts[4]),
            "Total": int(parts[5]),
        }
        data.append(record)

