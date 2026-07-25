# python error handling (try/except)

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output:
# Cannot divide by zero

try:
    num = int("abc")
    print(num)
except ValueError:
    print("Invalid number")

# Output:
# Invalid number


try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")

# Output:
# File not found


try:
    fruits = ["Apple", "Banana"]
    print(fruits[5])
except IndexError:
    print("Index out of range")

# Output:
# Index out of range


try:
    student = {"name": "John"}
    print(student["age"])
except KeyError:
    print("Key does not exist")

# Output:
# Key does not exist


try:
    result = "10" + 20
    print(result)
except TypeError:
    print("Cannot add string and integer")

# Output:
# Cannot add string and integer


try:
    num = int("abc")
    result = 10 / num
except (ValueError, ZeroDivisionError):
    print("Error occurred")

# Output:
# Error occurred


try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Result:", result)

# Output:
# Result: 5.0


try:
    print("File opened")
except:
    print("Error")
finally:
    print("File closed")

# Output:
# File opened
# File closed


try:
    print(20 / 0)
except ZeroDivisionError:
    print("Division by zero is not allowed")

# Output:
# Division by zero is not allowed


try:
    nums = [10, 20, 30]
    print(nums[5])
except IndexError:
    print("Index out of range")

# Output:
# Index out of range


try:
    student = {"name": "Ali"}
    print(student["age"])
except KeyError:
    print("Key not found")

# Output:
# Key not found

