# list_c = [5, 6, 7, 8, 9, 10, 11]
# del list_c[3:6]
# print(list_c)


# list_a = [1,2,3,4,5,6,7,8,9,10]
# sum = list_a[1]+list_a[3]+list_a[5]+list_a[7]
# print(sum)

import random

print(random.random())
print(random.randint(1, 10))

a = int(input("랜덤 숫자를 입력하세요"))
if a == random.randint(1, 10):
    print("정답")
else:
    print("오답","정답은 {}입니다".format(random.randint(1, 10)))