class Father:
    def house(self):
        print("Father has a house")

class Mother:
    def car(self):
        print("Mother has a car")

class Child(Father, Mother):  # Inherits both
    def bike(self):
        print("Child has a bike")

c = Child()
c.house()
c.bike()  #}this object can call every methods in their parent classes
c.car()






## __init__

