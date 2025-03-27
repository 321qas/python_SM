import datetime
now = datetime.datetime.now()

# minute = "{:02d}".format(now.minute)
# if 1 < now.hour and now.hour < 12:
#     print("오전", now.hour,minute, "분")
# else:
#     print("오후", now.hour-12,"시",minute,"분")
 
print("{}년 {:02d}월 {:02d}일".format(now.year, now.month, now.day))