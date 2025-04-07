class Car :
    speed = 0
    tire = 4
    door = 5
    def speedUp(self, s):
        self.speed += s
        print("현재 속도 : ", self.speed)

class Sedan(Car): # Car 클래스를 상속받음
    color ="red"

c = Car()

s = Sedan() # Sedan 클래스는 Car 클래스를 상속받음
print(s.tire) # Car 클래스의 속성 접근
s.speedUp(10) # Car 클래스의 메서드 호출
