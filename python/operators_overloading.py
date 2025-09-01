"""class Myclass:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def __add__(self, other):
        return Myclass(self.a + other.a, self.b + other.b)

ob1=Myclass(45,6)
ob2=Myclass(69,879)


R=ob1+ob2
print(R)"""


"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2   # Actually calls: p1.__add__(p2)
print(result)  """

"""#substraction
class Sub:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __sub__(self, other):
        return Sub(self.x-other.x,self.y-other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

obj1=Sub(8,9)
obj2=Sub(6,9)
result=obj1-obj2
print(result)"""

