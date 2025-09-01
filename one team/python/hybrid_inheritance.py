"""class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(A):
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()
"""


#__init__
class School:#We're creating a **base class** named `School`
    def __init__(self):
        print("Welcome to School")

class Teacher(School):
    def __init__(self):
        super().__init__()
        print("I'm a Teacher")

class Student(School):
    def __init__(self):
        super().__init__()
        print("I'm a Student")

class TeachingAssistant(Teacher, Student):
    def __init__(self):
        super().__init__()
        print("I'm a Teaching Assistant")

ta = TeachingAssistant()
