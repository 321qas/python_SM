#반복문

# for n in range(1,11):
#     print(n)

import random
num = []
a = random.randint(1,100)

for n in range(1,8):
    b = int(input("1부터 100 사이의 숫자를 입력하세요: "))
    num.append(b)
    if a == b:
        print("정답입니다.")
        break
    else:
        print("틀렸습니다.")
        if a > b:
            print("더 큰 수를 입력하세요.")
        else:
            print("더 작은 수를 입력하세요.")
print("정답은",a,"입니다.")
print("시도 횟수는",len(num),"번,","입력 숫자는",num,"입니다")
