# class Car:
#     color = "white"
#     speed = 0
#     tire = 4
#     door = 2

#     def speedUp(self,s):
#         self.speed += s

#     def speedDown(self,s):
#         self.speed -= s

#     def stop(self):
#         self.speed = 0

# a = Car()

# a.speed = 50

# print(a.speed)

# # 함수 사용방법
# a.speedUp(20)
# print(a.speed)




# 클래스 생성자
class Car:
    def __init__(self, color, speed, tire, door):
        self.color = color  # self.color : Car변수, color : 요청받은변수
        self.speed = 0
        self.tire = tire
        self.door = door

c = Car("red", 0, 4, 2)
c2 = Car("blue", 0, 4, 2)


print("car color : ",c.color, "car speed : ",c.speed, "car tire : ", c.tire, "car door : ", c.door)
