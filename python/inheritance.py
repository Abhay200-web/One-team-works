class University:
    def __init__(self,ne,pl):
        self.uname=ne
        self.place=pl                   #------------------>{SINGLE INHERITANCE}

class Student(University):
    def __init__(self, m, r, h):  # self is the reference of the object
        self.name=m
        self.age=r
        self.height=h
        super().__init__("ktu","calicut")
student1=Student("abhay",23,179,)
print("name:",student1.name)
print("place:",student1.place)
print("age:",student1.age)

