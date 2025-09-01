"""#--->DECORATORS
#A decorator in Python is a function that modifies the behavior of another function or class.
#It allows you to wrap another function in order to extend or change its behavior without modifying the original function's code.

def my_decorator(func): #--> defines the decorator function
    def wrapper():  #-->define a wrapper inside
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper #--> return wrapper returns the new wrapper version of the original function

@my_decorator  #-->uses the Decorator  say_hello= my_decorator(say_hello)
def say_hello():
    print("Hello, world!")

say_hello() #--> calls the function"""

# example for decorator
"""def my_dec(fun):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return wrapper
@my_dec
def substraction(a,b):
    print(a-b)

substraction(7,6)
substraction(35,67)"""



