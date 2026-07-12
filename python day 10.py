#LOOP : WHILE, FOR

i = 1
while i < 6:
  print(i)
  i += 1
#OUTPUT: 1,2,3,4,5


i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
#OUTPUT: 1,2,3


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
#OUTPUT: apple, banana, cherry


for x in range(2, 6):
  print(x) 
#output: 2,3,4,5


attempt = 1
while attempt <= 3:
    print("Enter PIN - Attempt", attempt)
    attempt += 1
# Output
# Enter PIN - Attempt 1
# Enter PIN - Attempt 2
# Enter PIN - Attempt 3


stop = 1
while stop <= 4:
    print("Bus reached Stop", stop)
    stop += 1
# Output
# Bus reached Stop 1
# Bus reached Stop 2
# Bus reached Stop 3
# Bus reached Stop 4


bottle = 5
while bottle > 0:
    print(bottle, "bottles left")
    bottle -= 1
# Output
# 5 bottles left
# 4 bottles left
# 3 bottles left
# 2 bottles left
# 1 bottles left


employees = ["Rahul", "Anjali", "Amit"]
for employee in employees:
    print(employee)
# Output
# Rahul
# Anjali
# Amit


brands = ["Dell", "HP", "Lenovo"]
for brand in brands:
    print(brand)
# Output
# Dell
# HP
# Lenovo


days = ["Monday", "Tuesday", "Wednesday"]
for day in days:
    print(day)
# Output
# Monday
# Tuesday
# Wednesday


floor = 1
while floor <= 5:
    print("Floor", floor)
    floor += 1
# Output
# Floor 1
# Floor 2
# Floor 3
# Floor 4
# Floor 5



level = 1
while level <= 3:
    print("Level", level, "Completed")
    level += 1
# Output
# Level 1 Completed
# Level 2 Completed
# Level 3 Completed


seconds = 5

while seconds > 0:
    print(seconds)
    seconds -= 1

print("Green Signal")

# Output
# 5
# 4
# 3
# 2
# 1
# Green Signal


token = 101

while token <= 103:
    print("Serving Token", token)
    token += 1

# Output
# Serving Token 101
# Serving Token 102
# Serving Token 103


animals = ["Lion", "Tiger", "Elephant"]

for animal in animals:
    print(animal)

# Output
# Lion
# Tiger
# Elephant


movies = ["Avatar", "Inception", "Titanic"]

for movie in movies:
    print(movie)

# Output
# Avatar
# Inception
# Titanic


subjects = ["Python", "AWS", "Linux"]

for subject in subjects:
    print("Learning", subject)

# Output
# Learning Python
# Learning AWS
# Learning Linux


temperatures = [28, 30, 32]

for temp in temperatures:
    print(temp, "°C")

# Output
# 28 °C
# 30 °C
# 32 °C


team = ["Ali", "Sara", "John"]

for member in team:
    print(member, "is online")

# Output
# Ali is online
# Sara is online
# John is online

