# 랜덤숫자 1-100까지 생성해서 10번 시도후 정답을 맞추면 정답입니다. 출력하고 시도횟수와 입력숫자를 출력하는 프로그램을 작성하시오.
# import random

# d = []
# a = random.randint(1,100)




# for c in range(1,11):
#     b = int(input("1부터 100 사이의 숫자를 입력하세요: "))
#     d.append(b)
#     if a == b:
#         print("정답입니다")
#         break
#     else:
#         print("틀렸습니다.")
#         if a > b:
#             print("더 큰 수를 입력하세요.")
#         else:
#             print("더 작은 수를 입력하세요.")
# print("시도횟수는 ",len(d),"번", "입력한 숫자는",d,"입니다")



import random
num = []
input_num_list = []
n = 1

for A in range(0, 6):
    num.append(random.randint(1, 100))
print(num)

for B in range(0,6):
    print(n, end="")
    input_num_list.append(int(input("번째 1부터 100 사이의 숫자를 입력하세요: ")))
    n += 1

if input_num_list[0] == num[0] and input_num_list[1] == num[1] and input_num_list[2] == num[2] and input_num_list[3] == num[3] and input_num_list[4] == num[4] and input_num_list[5] == num[5]:
    print("100억 당첨")
else:
    print("틀렸습니다.")