# while 반복문
# 무한반복
# 조건 반복

# i = 0
# while i < 10:
#     print("{}번 째 반복입니다".format(i))
#     i += 1


# ran_list = []
# while len(ran_list) < 5:
#     A = (int(input("숫자를 입력하세요: ")))
#     if A in ran_list:
#         print("중복된 숫자입니다.")
#     else:
#         ran_list.append(A)
# print(ran_list)

import random

ran_list = []
ran_list_2 = []

# 1. 랜덤 숫자 6개 생성 (중복 없이)
while len(ran_list) < 6:
    a = random.randint(1, 45)
    if a not in ran_list:
        ran_list.append(a)

# 2. 사용자 숫자 입력 (중복 방지)
while len(ran_list_2) < 6:
    b = int(input("숫자를 입력하세요: "))
    if b in ran_list_2:
        print("중복된 숫자입니다. 다시 입력하세요.")
    else:
        ran_list_2.append(b)

# 3. 두 리스트에서 숫자가 일치하는 개수 찾기
match_count = 0

# for num in ran_list:
#     for user_num in ran_list_2:
#         if num == user_num:
#             match_count += 1
#             break  # 같은 숫자를 찾으면 다음 숫자로 이동
for num in ran_list:
    if num in ran_list_2:
        match_count += 1

# 4. 결과 출력
if match_count == 6:
    print(" 당첨! ")
else:
    print("꽝! 맞춘 개수: {}개".format(match_count))

print("당첨번호:", ran_list)
print("내 번호:", ran_list_2)

