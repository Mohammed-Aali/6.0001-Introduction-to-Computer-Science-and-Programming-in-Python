class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, new_age):
        self.age = new_age
    def set_name(self, new_name=''):
        self.name = new_name
    def __str__(self) -> str:
        return 'animal:'+str(self.name)+":"+str(self.age)

# animal = Animal(8)
# animal.set_name('marble')
# print(animal)

class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return 'cat:'+str(self.name)+':'+str(self.age)

# cat = Cat(9)
# cat.set_name('kitty')
# cat.set_age('9001')
# print(cat)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), 'years difference')
    def __str__(self):
        return 'person:'+str(self.name)+":"+str(self.name)

# him = Person('Him', 8)
# her = Person('Her', 9)
# print('Him has '+str(him.get_friends())+" as friends")
# him.add_friends('Her')
# print('Him has '+str(him.get_friends())+" as friends")
# him.age_diff(her)

# print("\n-----------person test------------")
# p1 = Person('Jack', 30)
# p2 = Person('Jill', 25)
# print(p1.get_name())
# print(p1.get_age())
# print(p2.get_name())
# print(p2.get_age())
# print(p1)
# p1.speak()
# p1.age_diff(p2)
import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r <= 0.75:
            print('I should eat')
        else:
            print('I am watching tv')
    def __str__(self):
        return f"student:{str(self.name)}:{str(self.age)}:{str(self.major)}"

# print('-----Student test ------')
# s1 = Student('Alice', 20, 'CS')
# s2 = Student('Beth', 18)
# print(s1)
# print(s2)
# print(f'{s1.get_name()} says:', end=' ')
# s1.speak()
# print(f'{s2.get_name()} says:', end=' ')
# s2.speak()

# class vairable

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self ,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_oppisite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_oppisite or parents_same
    
    def __str__(self):
        return f'rabbit: {self.get_rid()}'
    
print('-----rabbit tests ------')
print('-----testing creating rabbits ------')
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print('r1:', r1)
print('r2:', r2)
print('r3:', r3)
print('r1 perent1:', r1.get_parent1())
print('r1 parent2:', r1.get_parent2())

print('\n-----testing rabbits addition------')
r4 = r1 + r2
print('r1:', r1)
print('r2:', r2)
print('r4:', r4)
print('r4 parent1:', r4.get_parent1())
print('r4 parent2:', r4.get_parent2())




