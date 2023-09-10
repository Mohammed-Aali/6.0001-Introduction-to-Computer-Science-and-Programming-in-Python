class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.i)

# changing i 
MyClass.i = 666
print(MyClass.__doc__)
print(MyClass.i)

# class instantiation
x = MyClass()
print(x.f())

print('-----------------------------------------')
# creating new instanse of a class. it needs a class for it to be instantiated
def __init__(self):
    self.data = []

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.5, -4.5)
print(x.r, x.i)
print('-----------------------------------------')

# instance objects/ data attributes / data members

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

print('-----------------------------------------')
# method objects using MyClass object
x = MyClass()

# storing away method object and calling it later
xf = x.f
x.counter = 0
while x.counter < 1:
    print(xf())
    x.counter += 1

del x.counter

# equivalent statements
x.f()
MyClass.f(x)

print('-----------------------------------------')
# class and instance variables
class Dog:
    kind = 'canine'                 # class variable shared by all instances
    def __init__(self, name) -> None:
        self.name = name            # instance variable unique to each instance

fido = Dog('Fido')
buddy = Dog('Buddy')

fido.kind # = canine. shared by all dogs
buddy.kind # = canine. shared by all dogs

fido.name # = Fido. unique to fido
buddy.name # = Buddy. unique to buddy


class Dog:
    tricks = []                     # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                   # = ['roll over', 'play dead']. unexpectedly shared by all dogs

# the correct way of implementing this should be in instance variable
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks # = ['roll over']
e.tricks # = ["play dead"]

print('-----------------------------------------')
# random remarks
class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

# calling other methods inside other methods using self arguemnt:
class Bag:
    def __init__(self):
        self.data = []
    
    def add(self, x):
        self.data.append(x)
    
    def add_twice(self, x):
        self.add(x)
        self.add(x)

print('-----------------------------------------')
# inheritance
class DerivedClassName(MyClass): #BaseClassName
    # <statement-1>
    # .
    # .
    # .
    # <statement-N>
    ...

# use when the base class is used in another module
class DerivedClassName(MyClass): # modname.BaseClassName
    ...

# methods that work with inheritance
isinstance(1, int) # returns True because 1 is an int
issubclass(bool, int) # returns True because bools is a subclass of int
issubclass(float, int) # returns False because float is not a subclass of int


print('-----------------------------------------')
# multiple inheritance
class DerivedClassName(Dog, MyClass, Bag): # Base1, Base2, Base3
    # <statement-1>
    # .
    # .
    # .
    # <statement-N>
    ...

print('-----------------------------------------')
# privete variables
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

print('-----------------------------------------')
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
print(john.salary)
print(john.dept)

print('-----------------------------------------')
# iterators
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)