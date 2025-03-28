# dictionary = {
#     "name": "건조 망고"
#     "type": "절임"
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"]
#     "origin": "필리핀"
# }


# list = [1,2,3,4,5]
# print(list[3::2])
total = 0  # 변수 이름 sum을 사용하지 않음 (sum은 내장 함수)
for i in range(1, 101):  # 1부터 100까지 반복
    if i % 3 == 0 and i % 5 == 0:  # 3과 5의 공배수인지 확인
        total += i  # total에 i를 더함

print(total)
