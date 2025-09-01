"""class Student:
    def __init__(self,name,age):
        self.___name=name
        self.___age=age
    def display(self):
        print(f"name:{self.___name}, age: {self.___age}")  #--->private variable
s1=Student("abhay",22)
s1.display()"""


"""print(s1.___age) # --> ingane cheyaathalll error verum"""

# protected
"""
class Father:
    def __init__(self):
        self._money=100000 # this is protected variable
    def show_money(self):
        print("father's money", self._money)
class Son(Father):
    def spend_money(self):
        print("son spends fathers money",self._money)
s=Son()
s.show_money()
s.spend_money()"""





