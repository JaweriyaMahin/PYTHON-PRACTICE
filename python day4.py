## PYTHON OPERATOR ##

## comparison operator
print(10 == 10)
# output: true

print(10 != 10)
# output: false

print(7 >= 3)
#output: true

print(7 > 3)
#output: true

print(3 < 7)
#output: true

print(7 <= 7)
#output: true


## arithmetic operators
x = 5
y = 3
print(x + y)
#output: 8

x = 10
y = 3
print(x - y)
# output: 7

x = 6
y = 3
print(x * y)
#output: 18

x = 12
y = 3
print(x / y)
#output:4

x = 5
y = 2
print(x % y)
#output: 1

x = 12
y = 5
print(x ** y)
#output: 248832

x = 15
y = 2
print(x // y)
#output: 7


## Assignment Operators
x = 5
print(x)
#output: 5

x = 25
x += 15
print(x)  
# Output: 40

x = 50
x -= 18
print(x) 
# Output: 32

x = 9
x *= 7
print(x)  
# Output: 63

x = 81
x /= 9
print(x)
# Output: 9.0

x = 29
x %= 6
print(x) 
# Output: 5

x = 45
x //= 8
print(x)  
# Output: 5

x = 5
x **= 3
print(x)  
# Output: 125

x = 14
x &= 11
print(x)  
# Output: 10

x = 12
x |= 5
print(x)  
# Output: 13

x = 15
x ^= 9
print(x)  
# Output: 6

x = 64
x >>= 3
print(x)  
# Output: 8 

x = 7
x <<= 2
print(x)  
# Output: 28

print(num := 99)  
# Output: 99


## Ternary Operator

num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)
#output: weekend!


num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)
#output: sat

age = 17

status = "Eligible to Vote" if age >= 18 else "Not Eligible"
print(status) 
# Output: Not Eligible


marks = 92

grade = "Pass" if marks >= 35 else "Fail"
print(grade)  
# Output: Pass



## Logical Operators

x = 5
print(x > 3 and x < 10)
#output: true


x = 10
print(x > 6 or x < 4)
#output: true

x = 7
print(not(x > 2 and x < 10))
#output: false

marks = 56
print(marks > 90 or marks < 20)  
# Output: False



## Identity Operators

x = ["apple", "mango"]
y = ["apple", "mango"]
z = x

print(x is z)
print(x is y)
print(x == y)
#output: true
#output: false
#output: true


x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)
#output: true


list1 = [10, 20, 30]
list2 = list1

print(list1 is list2)  
# Output: True


list1 = [10, 25, 70]
list2 = [10, 25, 70]

print(list1 is not list2)  
# Output: True



## Membership Operators

x = ["pineapple", "banana"]
print("banana" in x)
#output: true

x = ["pineapple", "banana"]
print("banana" in x)
#output: true


text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
#output: true
#output: false
#output: true



