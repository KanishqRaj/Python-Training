class Vehicle:
    def max_speed(self):
        raise NotImplementedError("The subclasses must be implemented")

class Car(Vehicle):
    def max_speed(self):
        print("The maxspeed of car is 180 kmph")

class Bike(Vehicle):
    def max_speed(self):
        print("The maxspeed of bike is 130 kmph")

c = Car()
c.max_speed()
b = Bike()
b.max_speed()