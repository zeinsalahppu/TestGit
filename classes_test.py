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



c1.description = "Small-size 4-Wheel Vehicle"
print(c1.description)
print(c2.description)
print(Car5.description)


