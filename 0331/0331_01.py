# # 리스트 값 변경할때 후자의 위치값이 포함
# a_list = [1,2,3,4,5,6]
# a_list[1:2] = [100,200]
# print(a_list)

# #1차원 리스트
# aa = [1,2,3,4,5]


# #2차원리스트
# aa = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,21,4145]
# ]

# print(aa[0][1])



# -------------------------------------------------------




bb = [[i * 5 + j + 1 for j in range(5)] for i in range(5)] 

# bb = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ]



for i in range(5):
    print()
    for j in range(5):
        print(bb[i][j],end=" ")






        
      
