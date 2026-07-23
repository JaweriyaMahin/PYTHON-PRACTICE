#  python polymorphism

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

d = Dog()
d.sound()

# Output:
# Dog Barks


class Bird:
    def sound(self):
        print("Bird Chirps")

class Parrot(Bird):
    def sound(self):
        print("Parrot Talks")

p = Parrot()
p.sound()

# Output:
# Parrot Talks



class Shape:
    def draw(self):
        print("Drawing Shape")

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

c = Circle()
c.draw()

# Output:
# Drawing Circle



class Employee:
    def work(self):
        print("Employee Working")

class Manager(Employee):
    def work(self):
        print("Manager Managing")

m = Manager()
m.work()

# Output:
# Manager Managing



class Vehicle:
    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

b = Bike()
b.start()

# Output:
# Bike Started



# python encapsulation


class Student:
    def __init__(self):
        self.name = "Mahin"

s = Student()
print(s.name)

# Output:
# Mahin


class Student:
    def __init__(self):
        self._name = "Ali"

s = Student()
print(s._name)

# Output:
# Ali


class Bank:
    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.show_balance()

# Output:
# 5000


class Person:
    def __init__(self):
        self.__age = 21

    def show(self):
        print(self.__age)

p = Person()
p.show()

# Output:
# 21


# python Inner Class


class Student:
    class Laptop:
        def show(self):
            print("HP Laptop")

lap = Student.Laptop()
lap.show()

# Output:
# HP Laptop


class Car:
    class Engine:
        def start(self):
            print("Engine Started")

e = Car.Engine()
e.start()

# Output:
# Engine Started


class College:
    class Department:
        def name(self):
            print("Computer Science")

d = College.Department()
d.name()

# Output:
# Computer Science


class Company:
    class Employee:
        def info(self):
            print("Employee Details")

e = Company.Employee()
e.info()

# Output:
# Employee Details


class School:
    class Teacher:
        def teach(self):
            print("Teaching Python")

t = School.Teacher()
t.teach()

# Output:
# Teaching Python


