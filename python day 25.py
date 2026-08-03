# 1. Class
class Student:
    pass

print(Student)

# Output:
# <class '__main__.Student'>


# 2. Object
class Student:
    pass

s1 = Student()
print(s1)

# Output:
# <__main__.Student object at 0x...>


# 3. Constructor (__init__)
class Student:

    def __init__(self):
        print("Constructor Called")

s1 = Student()

# Output:
# Constructor Called


# 4. Constructor with Parameters
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 22)

print(s1.name)
print(s1.age)

# Output:
# Ali
# 22


# 5. Method
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("sarah")
s1.display()

# Output:
# Student Name: sarah


# 6. Basic Inheritance
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()

# Output:
# Animal makes sound


# 7. Inheritance with Child Method
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()

# Output:
# Animal makes sound
# Dog barks

# Example 1: Variables & Data Types

name = "Johna"
age = 22
height = 5.4
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# Output:
# Johna
# 22
# 5.4
# True


# Example 2: Input & Output

name = input("Enter your name: ")

print("Welcome", name)

# Input:
# Ali

# Output:
# Enter your name: Ali
# Welcome Ali


# Example 3: Operators

a = 20
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# Output:
# 25
# 15
# 100
# 4.0
# 0


# Example 4: If-Else

age = 18

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

# Output:
# Eligible to Vote


# Example 5: For Loop

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# Example 6: Function

def greet(name):
    print("Hello", name)

greet("Ali")

# Output:
# Hello Ali


# Example 7: List

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(fruits[0])

fruits.append("Orange")
print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']
# Apple
# ['Apple', 'Banana', 'Mango', 'Orange']


# Example 8: Tuple

colors = ("Red", "Green", "Blue")

print(colors)
print(colors[1])

# Output:
# ('Red', 'Green', 'Blue')
# Green


# Example 9: Dictionary

student = {
    "name": "Ali",
    "age": 22,
    "city": "Delhi"
}

print(student)
print(student["name"])

# Output:
# {'name': 'Ali', 'age': 22, 'city': 'Delhi'}
# Ali


# Example 10: Set

numbers = {10, 20, 30, 40}

print(numbers)

numbers.add(50)

print(numbers)

# Output:
# {10, 20, 30, 40}
# {10, 20, 30, 40, 50}


# Example 11: File Handling

with open("test.txt", "w") as file:
    file.write("Hello Python")

with open("test.txt", "r") as file:
    print(file.read())

# Output:
# Hello Python


# Example 12: Exception Handling

try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output:
# Cannot divide by zero


# Example 13: Module

import math

print(math.sqrt(25))
print(math.factorial(5))

# Output:
# 5.0
# 120


# Example 14: Class, Object & Constructor

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("Ali")
s1.display()

# Output:
# Student Name: Ali


# Example 15: Inheritance

class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()

# Output:
# Animal makes sound
# Dog barks

