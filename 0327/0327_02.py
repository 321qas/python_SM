
# 달러를 입력하면 원화로 환산하기

# while True:
#     print("환산 프로그램")
#     print("-" * 50)
#     print("원화 입력하기 => 1")
#     print("달러 입력하기 => 2")
#     print("종료하기 => 0")
#     print("-" * 50)
#     select = input("입력하세요 : ")
#     if select == "0":
#         print("프로그램을 종료합니다.")
#         break
#     elif select == "1":
#         input_won = input("원화를 입력하세요 : ")
#         dollar = int(input_won) / 1467
#         print("입력 한 {}원은 {:.1f}달러 입니다".format(input_won, dollar))
#     elif select == "2":
#         input_dollar = input("달러를 입력하세요 : ")
#         won = int(input_dollar) * 1467
#         print("입력한 {:.1f}달러는 {}원 입니다.".format(float(input_dollar), won))
#     else:
#         print("잘못된 입력입니다. 다시 시도하세요.")
#     print("-" * 50)

# ------------------------------------------------------------------------------------------------------------------------

# 동전변환

# input_money = int(input("금액을 입력하세요 : "))
# a = input_money // 500
# b = input_money % 500 // 100
# c = input_money % 500 % 100 // 50
# d = input_money % 500 % 100 % 50 // 10
# print("500원 : {}개".format(a))
# print("100원 : {}개".format(b))
# print("50원 : {}개".format(c))
# print("10원 : {}개".format(d))

# ------------------------------------------------------------------------------------------------------------------------


# 반지름 입력받아 원의 넓이와 둘레 구하기

# input = float(input("반지름을 입력하세요 : "))
# area = input * input * 3.14
# circumference = 2 * input * 3.14
# print("반지름이 {}인 원의 넓이는 {:.1f}입니다".format(input, area))
# print("반지름이 {}인 원의 둘레는 {:.1f}입니다".format(input, circumference))

