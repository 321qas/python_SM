# 두 수를 입력받아 두 수 사이의 합계를 구하시오

# a = int(input("첫 번째 수: "))
# b = int(input("두 번째 수: "))
# if a > b:
#     a, b = b, a

# sum = 0

# for i in range(a,b+1):
#     sum = sum + i
    # print(sum)


# for i in range(2, 10):
#     print("{}단".format(i))
#     for j in range(1,10):
#         print("{} x {} = {}".format(i, j, i*j), end=" ")
#     print()

a = int(input("첫 번째 수: "))
b = int(input("두 번째 수: "))
if a > b:
    a, b = b, a
for i in range(a, b+1):
    print("{}단".format(i))
    for j in range(1,10):
        print("{} x {} = {}".format(i, j, i*j), end=" ")