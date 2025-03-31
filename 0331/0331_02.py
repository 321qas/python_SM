# import random
# sample_list = [i+1 for i in range(25)]
# random.shuffle(sample_list)

# a_list = [[0]*5 for i in range(5)]

# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = sample_list[5*i + j]

# print(a_list)



# 5 * 5 2차원 리스트 - > 랜덤으로 1-25까지 숫자를 넣기

import random
def generate_random_matrix(size=5):
    numbers = list(range(1, size * size + 1))  # 1부터 n*n까지 숫자 리스트 생성
    random.shuffle(numbers)  # 리스트 섞기
    
    matrix = [numbers[i * size:(i + 1) * size] for i in range(size)]  # nxn 형태로 변환
    return matrix

def print_matrix(matrix):
    size = len(matrix)
    print("   ", "  ".join(f"{i:2}" for i in range(1, size + 1)))  # x 좌표 표시
    print("   " + "---" * size * 2)  # 구분선
    for idx, row in enumerate(matrix, start=1):
        print(f"{idx:2}|", "  ".join(f"{num:2}" if num != "X" else " X" for num in row))  # y 좌표 및 행 출력

def check_bingo(matrix, marked):
    size = len(matrix)
    bingo_count = 0

    for i in range(size):
        if all(marked[i][j] for j in range(size)):
            bingo_count += 1
        if all(marked[j][i] for j in range(size)):
            bingo_count += 1

    if all(marked[i][i] for i in range(size)):
        bingo_count += 1
    if all(marked[i][size - i - 1] for i in range(size)):
        bingo_count += 1

    return bingo_count >= 2  # 2빙고 이상인지 확인

# 실행
size = 5
table = generate_random_matrix(size)
marked = [[False] * size for _ in range(size)]

print("빙고 게임을 시작합니다!")
while True:
    print_matrix(table)
    print("-" * 30)
    num1 = int(input("X좌표 : "))
    num2 = int(input("Y좌표 : "))
    
    # 좌표에 해당하는 값 마킹 및 숫자를 'X'로 변경
    if 1 <= num1 <= size and 1 <= num2 <= size:
        if not marked[num2 - 1][num1 - 1]:
            marked[num2 - 1][num1 - 1] = True
            table[num2 - 1][num1 - 1] = "X"  # 선택된 숫자를 'X'로 변경
            print(f"좌표 ({num1}, {num2})를 선택했습니다.")
        else:
            print("이미 선택된 좌표입니다. 다시 입력해주세요.")
    else:
        print("잘못된 좌표입니다. 다시 입력해주세요.")
    
    # 빙고 체크
    if check_bingo(table, marked):
        print_matrix(table)
        print("2빙고! 게임에서 승리했습니다!")
        break