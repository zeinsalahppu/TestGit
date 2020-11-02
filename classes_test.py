import math


class Car:
    def __init__(self, givenname):
        self.name = givenname
        self.status = "idle"
        self.speed = 0
        self.fuel = 100  # %
        self.direction = "forward"

    def get_name(self):
        return self.name

    def set_speed(self, sp):
        self.speed = sp

    def get_speed(self):
        return self.speed
        
        
# my_car = Car("Smart Car")
# # print(type(my_car))
#
# # print(my_car.name)
# # my_car.speed = 20
# # print(my_car.speed)
#
# print(my_car.get_name())
# my_car.set_speed(25)
# print(my_car.get_speed())

class Car2:
    def __init__(self, givenname):
        self.name = givenname  # public
        self._status = "idle"  # protected
        self.__speed = 0       # private

    def set_status(self, st):
        self._status = st

    def get_status(self):
        return self._status

    def set_speed(self, sp):
        self.__speed = sp

    def get_speed(self):

       return self.__speed


# sc = Car2("Smart Car 2.0")
# print(sc.name)
# # sc._status = "driving"
# # print(sc._status)
# # print(sc.get_status())
#
# sc = Car2("Smart Car 2.0")
# sc.set_speed(55)
# print(sc.__speed)


class Car3:
    def __init__(self, givenname):
        self.name = givenname  # public
        # self._status = "idle"  # protected
        self.__speed = 0       # private

    # def set_status(self, st):
    #     self._status = st
    #
    # def get_status(self):
    #     return self._status

    def set_speed(self, sp):
        print("Setting speed value")
        self.__speed = sp

    def get_speed(self):
        print("Getting speed value")
        return self.__speed

    speed = property(get_speed, set_speed)

sc3 = Car3("Smart Car 3.0")
# sc3.set_speed(33)
# print(sc3.get_speed())

# sc3.speed = 40
# print(sc3.speed + 10)



c1.description = "Small-size 4-Wheel Vehicle"
print(c1.description)
print(c2.description)
print(Car5.description)


