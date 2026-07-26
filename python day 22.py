# PYTHON DSA (DATA STRUCTURE AND ALGORITHMS)

numbers = [10, 20, 30, 40]

print(numbers)

# Output:
# [10, 20, 30, 40]


fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']



text = "Python"

print(text.upper())

# Output:
# PYTHON


text = "DevOps"

print(text[::-1])

# Output:
# spOveD


text = "Cloud Computing"

print(text.replace("Cloud", "AWS"))

# Output:
# AWS Computing


numbers = (10, 20, 30)

print(numbers[1])

# Output:
# 20


numbers = (10, 20, 30, 20)

print(numbers.count(20))

# Output:
# 2


student = {
    "name": "Mike",
    "age": 22
}

print(student)

# Output:
# {'name': 'Mike', 'age': 22}


numbers = {10, 20}

numbers.add(30)

print(numbers)

# Output:
# {10, 20, 30}


numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)

# Output:
# {10, 30}


stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Output:
# [10, 20, 30]



stack = [10, 20, 30]

stack.pop()

print(stack)

# Output:
# [10, 20]


stack = [10, 20, 30]

print(stack[-1])

# Output:
# 30



from collections import deque

queue = deque([10, 20, 30])

print(queue[0])

# Output:
# 10


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)

print(head.data)

# Output:
# 10



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

current = head

while current:
    print(current.data)
    current = current.next

# Output:
# 10
# 20
# 30



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)

print(root.left.data)
print(root.right.data)

# Output:
# 5
# 15



import heapq

numbers = [30, 10, 20]

heapq.heapify(numbers)

print(numbers)

# Output:
# [10, 30, 20]


import heapq

numbers = [10, 20]

heapq.heapify(numbers)

heapq.heappush(numbers, 5)

print(numbers)

# Output:
# [5, 20, 10]



graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

print(graph)

# Output:
# {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}


graph = {
    "A": ["B", "C"],
    "B": ["D"]
}

print(graph["A"])

# Output:
# ['B', 'C']



numbers = [10, 20, 30, 40]

target = 30

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)

# Output:
# Found at index 2


numbers = [5, 10, 15]

target = 20

if target in numbers:
    print("Found")
else:
    print("Not Found")

# Output:
# Not Found



arr = [5, 3, 1]

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

# Output:
# [1, 3, 5]



arr = [30, 10, 20]

for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

# Output:
# [10, 20, 30]


arr = [30, 20, 10]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key

print(arr)

# Output:
# [10, 20, 30]



arr = [8, 4, 2, 6]

arr.sort()

print(arr)

# Output:
# [2, 4, 6, 8]



arr = [9, 1, 5, 3]

arr.sort()

print(arr)

# Output:
# [1, 3, 5, 9]


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Output:
# 120


coins = [10, 5, 2, 1]

amount = 18

result = []

for coin in coins:
    while amount >= coin:
        amount -= coin
        result.append(coin)

print(result)

# Output:
# [10, 5, 2, 1]


activities = ["A", "B", "C"]

print(activities[0])

# Output:
# A

