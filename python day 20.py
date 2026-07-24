# lambda funtion 

add = lambda a, b: a + b
print(add(5, 3))

#Output: 8




multiply = lambda a, b: a * b
print(multiply(4, 6))

# Output:24




square = lambda x: x * x
print(square(7))

# Output:49




check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(10))

# Output:Even




maximum = lambda a, b: a if a > b else b
print(maximum(15, 20))

# Output:20




upper = lambda text: text.upper()
print(upper("python"))

# Output:PYTHON


length = lambda text: len(text)
print(length("Cloud"))

# Output:5



reverse = lambda text: text[::-1]
print(reverse("AWS"))

# Output:SWA



status = lambda x: "Positive" if x > 0 else "Negative"
print(status(-8))

# Output:Negative



result = lambda marks: "Pass" if marks >= 35 else "Fail"
print(result(42))

# Output:Pass


map() 
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

# Output:[2, 4, 6, 8]


numbers = [5, 10, 15]
result = list(map(lambda x: x + 5, numbers))
print(result)

# Output:[10, 15, 20]



numbers = [2, 3, 4]
result = list(map(lambda x: x ** 2, numbers))
print(result)

# Output:[4, 9, 16]



words = ["aws", "docker", "linux"]
result = list(map(lambda x: x.upper(), words))
print(result)

# Output:['AWS', 'DOCKER', 'LINUX']



words = ["Git", "Python", "Cloud"]
result = list(map(lambda x: len(x), words))
print(result)

# Output:[3, 6, 5]


filter() 
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# Output:[2, 4, 6]



numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)

# Output:[1, 3, 5]



numbers = [10, 25, 40, 55]
result = list(filter(lambda x: x > 30, numbers))
print(result)

# Output:[40, 55]



numbers = [-5, 8, -2, 10]
result = list(filter(lambda x: x > 0, numbers))
print(result)

# Output:[8, 10]



words = ["AWS", "Python", "Git", "Docker"]
result = list(filter(lambda x: len(x) > 4, words))
print(result)

# Output:['Python', 'Docker']


reduce()
from functools import reduce

numbers = [10, 20, 30]
result = reduce(lambda x, y: x + y, numbers)
print(result)

# Output:60


from functools import reduce

numbers = [2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
print(result)

# Output:24


from functools import reduce

numbers = [5, 9, 2, 8]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)

# Output:9


from functools import reduce

numbers = [5, 9, 2, 8]
result = reduce(lambda x, y: x if x < y else y, numbers)
print(result)

# Output:2



from functools import reduce

words = ["Dev", "Ops", "Engineer"]
result = reduce(lambda x, y: x + " " + y, words)
print(result)

# Output:Dev Ops Engineer



