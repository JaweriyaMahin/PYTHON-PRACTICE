# python modules

import mymodule

mymodule.greeting("Jonathan")
# output
# Hello,jonathan


import random

num = random.randint(1, 10)

print("Random Number =", num)

# Sample Output:
# Random Number = 6
# (Output will be different every time.)


import math

number = 64

result = math.sqrt(number)

print("Square Root =", result)

# Output:
# Square Root = 8.0


from datetime import datetime

today = datetime(2026, 7, 15)

print("Date =", today.strftime("%d-%m-%Y"))

# Output:
# Date = 15-07-2026


import os

print("Current Folder:")
print(os.getcwd())

# Sample Output:
# Current Folder:
# C:\Users\jhon\Desktop
# (Your path may be different.)


import statistics

marks = [70, 80, 90, 100]

average = statistics.mean(marks)

print("Average =", average)

# Output:
# Average = 85



import calendar

print("Leap Year:", calendar.isleap(2024))

# Output:
# Leap Year: True


# python math

import math

num = 6

result = math.factorial(num)

print("Factorial =", result)

# Output:
# Factorial = 720


import math

result = math.pow(4, 3)

print("Power =", result)

# Output:
# Power = 64.0


import math

num = 7.2

result = math.ceil(num)

print("Ceiling Value =", result)

# Output:
# Ceiling Value = 8



import math

num = 7.9

result = math.floor(num)

print("Floor Value =", result)

# Output:
# Floor Value = 7



x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
# output : 5,25


x = abs(-7.25)

print(x)
#output: 7.25


x = pow(4, 3)

print(x)
#output: 64



import datetime

x = datetime.datetime.now()

print(x)
#output:2026-07-15 21:28:15.214379


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#output: 2026, wenesdayimport datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
#output: june


import datetime

x = datetime.datetime.now()

print(x.strftime("%j"))
#output: 196 



