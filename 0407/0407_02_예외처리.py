# 예외처리
# 프로그램을 하다보면, 에러가 뜸

# 1. 구문에러
# 2. 런타임에러
# # 
# priint("데이터 출력") # 구문에러 - 오타


# for i in range(6): # 런타임에러 - 구문에 에러는 없지만 실행시 에러
#     print(a_list[i]) 

# stu = [1]
# while True:
#     print("1. 학생출력")
#     choice =int(input("원하는 번호를 입력하세요.>> "))
#     if choice == 1:
#         print(stu) # 논리

# 예외처리
# 프로그램을 하다보면, 에러가 뜸
# while True:
#     print("1. 학생출력")
#     choice =int(input("원하는 번호를 입력하세요.>> "))
#     try:
#         choice = int(choice)
#     except:
#         print("정수를 입력하세요.")
#         continue


# a_list = ["1", "2", "3", "자바", "파이썬"]

# list_number = []
# # 숫자로 변환되는 것만 저장하시오



# exception 처리
# for i in range(5):
#     try:
#         list_number.append(int(a_list[i]))
#     except ValueError:
#         print(f"\'{a_list[i]}\' 은(는) 숫자로 변환될 수 없습니다.")

# print("변환된 숫자:", list_number)
# ------------------------------------------------------------------------------------------
# if문 처리
# for a in a_list:
#     if a.isdigit():
#         list_number.append(int(a))
#     else:
#         print(f"\'{a}\' 은(는) 숫자로 변환될 수 없습니다.")
# print("변환된 숫자:", list_number)