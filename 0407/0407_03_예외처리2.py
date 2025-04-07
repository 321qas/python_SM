try:
    print(1)
    print(2)
    choice = int(input("정수를 입력하세요."))
    print(4)
except:     # 에러가 났을 때
    print(5)
else:       # 에러가 안났을 때  
    print(6)
finally:    # 무조건 실행
    print(7)

# print(1)
# print(2)
# raise Exception("프로그램 미구현 - 수정부분이 프로그램 진행해야 함.")
# try:
#     print(3)
# except:
#     print(4)
# else:
#     print(5)
# finally:
#     print(6)

