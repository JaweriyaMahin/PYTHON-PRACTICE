def greet(name):
    print("Hello", name)

greet("Ali")

# Output:
# Hello Ali


def add(a, b):
    print(a + b)

add(20, 15)

# Output:
# 35


def student(name, age, city):
    print(name, age, city)

student("Sara", 20, "Mumbai")

# Output:
# Sara 20 Mumbai


def country(name="India"):
    print(name)

country()

# Output:
# India


def employee(name, salary):
    print(name, salary)

employee(salary=30000, name="Rahul")

# Output:
# Rahul 30000


x = 100

def show():
    print(x)
show()
# Output:
# 100


def number():
    x = 50
    print(x)

number()

# Output:
# 50


x = 10

def demo():
    x = 20
    print(x)

demo()
print(x)

# Output:
# 20
# 10


def decorator(func):
    def message():
        print("Before Function")
        func()
    return message

@decorator
def hello():
    print("Hello")

hello()

# Output:
# Before Function
# Hello


add = lambda a, b: a + b

print(add(12, 8))

# Output:
# 20


multiply = lambda a, b: a * b

print(multiply(7, 6))

# Output:
# 42


square = lambda x: x * x

print(square(9))

# Output:
# 81


check = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check(15))

# Output:
# Odd


def numbers(n):
    if n <= 5:
        print(n)
        numbers(n + 1)

numbers(1)

# Output:
# 1
# 2
# 3
# 4
# 5


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Output:
# 120



def total(n):
    if n == 1:
        return 1
    return n + total(n - 1)

print(total(5))

# Output:
# 15


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1


def numbers():
    yield 1
    yield 2
    yield 3

for i in numbers():
    print(i)

# Output:
# 1
# 2
# 3



def count():
    for i in range(1, 6):
        yield i

for x in count():
    print(x)

# Output:
# 1
# 2
# 3
# 4
# 5


def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)

# Output:
# 100


def student(**details):
    print(details["name"])
    print(details["age"])

student(name="Aisha", age=21)

# Output:
# Aisha
# 21


x = 50

def change():
    global x
    x = 100

change()
print(x)

# Output:
# 100


def decorator(func):
    def wrapper():
        print("Program Started")
        func()
        print("Program Ended")
    return wrapper

@decorator
def message():
    print("Learning Python")

message()

# Output:
# Program Started
# Learning Python
# Program Ended


def welcome(func):
    def wrapper():
        print("Welcome User")
        func()
    return wrapper

@welcome
def hello():
    print("Hello Python")

hello()

# Output:
# Welcome User
# Hello Python



largest = lambda a, b: a if a > b else b

print(largest(45, 70))

# Output:
# 70


upper = lambda text: text.upper()

print(upper("python"))

# Output:
# PYTHON


def marks(*args):
    print("Total Marks:", sum(args))

marks(85, 90, 88, 92)

# Output:
# Total Marks: 355


def subjects(*args):
    print("Subjects:", ", ".join(args))

subjects("Math", "Science", "English")

# Output:
# Subjects: Math, Science, English


def cities(*args):
    print("First:", args[0])
    print("Last:", args[-1])

cities("Delhi", "Mumbai", "Pune", "Hyderabad")

# Output:
# First: Delhi
# Last: Hyderabad


def salary(*args):
    print("Average Salary:", sum(args) / len(args))

salary(25000, 30000, 35000)

# Output:
# Average Salary: 30000.0



def student(**kwargs):
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])

student(name="Ali", age=20)

# Output:
# Name: Ali
# Age: 20


def employee(**kwargs):
    print("Employee:", kwargs["name"])
    print("Salary:", kwargs["salary"])

employee(name="Rahul", salary=45000)

# Output:
# Employee: Rahul
# Salary: 45000


def book(**kwargs):
    print("Title:", kwargs["title"])
    print("Author:", kwargs["author"])

book(title="Python Basics", author="John")

# Output:
# Title: Python Basics
# Author: John



def product(**kwargs):
    print(kwargs)

product(name="Mouse", price=799)

# Output:
# {'name': 'Mouse', 'price': 799}


def city(**kwargs):
    print("City:", kwargs["city"])
    print("State:", kwargs["state"])

city(city="Pune", state="Maharashtra")

# Output:
# City: Pune
# State: Maharashtra


def website(**kwargs):
    for value in kwargs.values():
        print(value)

website(name="Google", country="USA")

# Output:
# Google
# USA

