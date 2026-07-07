colors = ["Red", "Blue", "Green", "Black"]
print(colors[1:3])
#output:'Blue', 'Green'

fruits = ["Apple", "Banana", "Mango"]
print(fruits[1])

#Output:
# Banana

colors = ["Red", "Blue", "Green"]
colors[2] = "Yellow"
print(colors)
#Output:Red, Blue, Yellow

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#Output:10, 20, 30, 40

cities = ["Delhi", "Mumbai", "Pune"]
cities.insert(1, "Hyderabad")
print(cities)

#Output:Delhi, Hyderabad, Mumbai, Pune

animals = ["Cat", "Dog", "Rabbit"]
animals.remove("Dog")
print(animals)

#Output:Cat, Rabbit

marks = [85, 45, 70, 95]
marks.sort()
print(marks)

#Output:45, 70, 85, 95

list1 = ["Pen", "Book", "Bag"]
list2 = list1.copy()
print(list2)

#Output:Pen, Book, Bag

list1 = [1, 2]
list2 = [3, 4]
list3 = list1 + list2
print(list3)

#Output:1, 2, 3, 4

names = ["Ali", "Sara", "John", "Ayan"]
print(names[1:3])

#Output:Sara, John

flowers = ["Rose", "Lily", "Lotus"]

for flower in flowers:
    print(flower)

#Output:Rose, Lily ,Lotus




