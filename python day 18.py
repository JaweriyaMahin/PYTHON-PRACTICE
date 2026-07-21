# PYTHON (OOP) OBJECT ORIENTED PROGRAMMING

class Student:
    def study(self):
        print("Student is studying")

s = Student()
s.study()

# Output:
# Student is studying


class Car:
    def start(self):
        print("Car Started")

c = Car()
c.start()

# Output:
# Car Started


class Animal:
    def sound(self):
        print("Dog Barks")

a = Animal()
a.sound()

# Output:
# Dog Barks


class Mobile:
    def call(self):
        print("Calling...")

m = Mobile()
m.call()

# Output:
# Calling...


class Laptop:
    def power_on(self):
        print("Laptop is ON")

l = Laptop()
l.power_on()

# Output:
# Laptop is ON

# PYTHON CLASSES AND OBJECT


class Student:
    name = "lily"

s = Student()
print(s.name)

# Output:
# lily


class Car:
    brand = "Toyota"

c = Car()
print(c.brand)

# Output:
# Toyota


class Book:
    title = "Python"

b = Book()
print(b.title)

# Output:
# Python



class Employee:
    company = "TCS"

e = Employee()
print(e.company)

# Output:
# TCS


class Animal:
    type = "Dog"

a = Animal()
print(a.type)

# Output:
# Dog


#_INTIT_()METHOD

class Student:
    def __init__(self):
        print("Classes is start")

s = Student()

# Output:
# Classes is start


class Student:
    def __init__(self, name):
        self.name = name

s = Student("Mili")
print(s.name)

# Output:
# mili



class Car:
    def __init__(self, brand):
        self.brand = brand

c = Car("BMW")
print(c.brand)

# Output:
# BMW


class Book:
    def __init__(self, title):
        self.title = title

b = Book("Python")
print(b.title)

# Output:
# Python



# self Parameter

class Student:
    def show(self):
        print("Hello Student")

s = Student()
s.show()

# Output:
# Hello Student


class Car:
    def brand(self, name):
        print(name)

c = Car()
c.brand("Toyota")

# Output:
# Toyota


class Employee:
    def info(self, name):
        print("Employee:", name)

e = Employee()
e.info("Rahul")

# Output:
# Employee: Rahul


class Mobile:
    def company(self, brand):
        print(brand)

m = Mobile()
m.company("Samsung")

# Output:
# Samsung


# Class Properties

class Student:
    name = "Mahin"

print(Student.name)

# Output:
# Mahin


class Car:
    brand = "Toyota"

c = Car()
print(c.brand)

# Output:
# Toyota


class Book:
    title = "Python Basics"

b = Book()
print(b.title)

# Output:
# Python Basics


# Class Methods


class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()

# Output:
# ABC School

class Book:
    category = "Programming"

    @classmethod
    def details(cls):
        print(cls.category)

Book.details()

# Output:
# Programming

# PYTHON INHERITANCE

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()

# Output:
# Animal makes sound

class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def drive(self):
        print("Car is Running")

c = Car()
c.start()
c.drive()

# Output:
# Vehicle Started
# Car is Running



class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()

# Output:
# Class A

class Father:
    def home(self):
        print("Father's House")

class Son(Father):
    pass

s = Son()
s.home()

# Output:
# Father's House


class Father:
    def home(self):
        print("House")

class Mother:
    def car(self):
        print("Car")

class Child(Father, Mother):
    pass

c = Child()
c.home()
c.car()

# Output:
# House
# Car















