a = input(("몇 월입니까? : "))
a = int(a)
if 2 < a < 6:
    print("봄입니다.")
elif 5 < a < 9:
    print("여름입니다.")
elif 8 < a < 12:
    print("가을입니다.")
else: 
    print("겨울입니다.")