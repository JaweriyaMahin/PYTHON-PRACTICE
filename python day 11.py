fruits = ["Apple", "Banana", "Mango"]

it = iter(fruits)

print(next(it))
print(next(it))
print(next(it))

# Output
# Apple
# Banana
# Mango


numbers = (10, 20, 30)

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# Output
# 10
# 20
# 30


text = "DOG"

it = iter(text)

print(next(it))
print(next(it))
print(next(it))

# Output
# D
# O
# G


nums = iter(range(5, 8))

print(next(nums))
print(next(nums))
print(next(nums))

# Output
# 5
# 6
# 7



import math

print(math.sqrt(81))

# Output
# 9.0

import math

print(math.pow(4, 3))

# Output
# 64.0


import math

print(math.factorial(6))

# Output
# 720


import random

print(random.randint(1, 10))

# Output
# Random number between 1 and 10
# Example: 7


import random

colors = ["Red", "Blue", "Green"]

print(random.choice(colors))

# Output
# Random item from the list
# Example: Blue


colors = ["Red", "Green", "Blue"]

it = iter(colors)

for color in it:
    print(color)

# Output
# Red
# Green
# Blue


student = {"name": "Sara", "age": 21}

it = iter(student)

print(next(it))
print(next(it))

# Output
# name
# age


student = {"name": "Sara", "age": 21}

it = iter(student.values())

print(next(it))
print(next(it))

# Output
# Sara
# 21


student = {"id": 101, "course": "Python"}

it = iter(student.items())

print(next(it))
print(next(it))

# Output
# ('id', 101)
# ('course', 'Python')


data = [50, "Hello", 8.5]

it = iter(data)

print(next(it))
print(next(it))
print(next(it))

# Output
# 50
# Hello
# 8.5


even = [2, 4, 6, 8]

it = iter(even)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Output
# 2
# 4
# 6
# 8


import datetime

today = datetime.datetime.now()

print(today.year)

# Output
# Example: 2026


import datetime

today = datetime.date.today()

print(today)

# Output
# Example: 2026-07-13



import calendar

print(calendar.isleap(2024))

# Output
# True


import calendar

print(calendar.day_name[0])

# Output
# Monday



import os

print(os.getcwd())

# Output
# Example:
# C:\Users\Student\Python


import keyword

print("while" in keyword.kwlist)

# Output
# True


