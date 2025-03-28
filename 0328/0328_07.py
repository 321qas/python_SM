# arr = [1,2,3,4,5,6,7,8,9]

# #리스트 내포
# arr2 = [str(i)+"m" for i in arr]

# a_list = [1,2,3]
# aa_list = ["1m", "2m","3m"]
# aaa_list = [str(i)+"m" for i in a_list]
# print(aaa_list)

arr = [i+100 for i in range(100)]
print(arr)

arr2 = [str(i)+"m" for i in arr]
print(arr2)

list = []
for i in range(100):
    list.append(i+100)
print(list)