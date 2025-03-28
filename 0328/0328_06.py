# for i in range(2,10):
#     print("\n{}단".format(i))
#     for j in range(1,10):
#         print("{:d} x {:d} = {:d}".format(i,j,i*j), end="  ")
        
fruits = ['apple', 'banana', 'cherry']

for i,fruit in enumerate(fruits):
    print("{}번째 과일: {}".format(i+1,fruit))

    # enumerate : 인덱스 번호 부여해줌