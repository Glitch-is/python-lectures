
def greeting(name, greeting):
    if type(name) == int:
        raise ValueError
    return f"{greeting}! How are you {name}"


# try:
#     print(greeting(1 ,"howdy"))
# except:
#     print("Please pass in strings")


class MyClass():
    id = 1
    '''
    This is my test class
    '''
    class MySubClass():
        def __init__(self, my_arg):
            MyClass.id += 1
            self.my_arg = my_arg



    def __init__(self, my_arg):
        MyClass.id += 1
        self.my_arg = my_arg


    def konni(self, number):
        '''
        We want a number and we'll print it for you 
        '''
        print(self.my_arg)
        print(f"You passed in {number}")

    def wrapper(self, a):
        def fun(b):
            return a + b
        return fun
    


my_class1 = MyClass("arg")
# print(my_class1.id)
my_class2 = MyClass("arg")
# print(my_class2.id)

# print(isinstance(my_class2, MyClass))

fun1 = my_class1.wrapper(5)
fun2 = my_class1.wrapper(100)

import math

class Shapes():
    def __init__(self, edges, color, name="Circle"):
        self.edges = edges
        self.color = color
        self.name = name

    def get_info(self):
        return f"I'm a {self.name}, I have {self.edges} edges and I'm {self.color}"

class Circle(Shapes):
    def __init__(self, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radius = radius

    def __diameter__(self):
        return self.radius*2 

    def get_info(self):
        return super().print_info() + f". And I have the radius {self.radius}"

circle = Circle(5, 0, "Yellow", "Circle")


# Decorators
logged_in = False
def is_logged_in(some_function):
    def wrapper():
        if logged_in:
            some_function()
        else:
            login()
    return wrapper

@is_logged_in
def hello():
    print("Hello world")
