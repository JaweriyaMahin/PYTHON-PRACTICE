# python range

for i in range(5):
    print("Hello")
# Output
# Hello
# Hello
# Hello
# Hello
# Hello


for i in range(1, 6):
    print(i, "=", i * i)

# Output
# 1 = 1
# 2 = 4
# 3 = 9
# 4 = 16
# 5 = 25


for i in range(1, 6):
    print(i, "=", i ** 3)

# Output
# 1 = 1
# 2 = 8
# 3 = 27
# 4 = 64
# 5 = 125


for i in range(1, 6):
    print(f"7 x {i} = {7 * i}")

# Output
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35


names = ["Ali", "Sara", "John"]

for i in range(len(names)):
    print(names[i])

# Output
# Ali
# Sara
# John


for i in range(1, 11):
    if i % 3 == 0:
        print(i)

# Output
# 3
# 6
# 9


total = 0

for i in range(2, 11, 2):
    total += i

print("Sum =", total)

# Output
# Sum = 30


x = range(10)

print(x)
print(list(x))
#output
#range(0, 10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


x = range(3, 10)


print(x)
print(list(x))
#output: range(3, 10)
#[3, 4, 5, 6, 7, 8, 9]


print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))
#[0, 1, 2, 3, 4]
#[1, 2, 3, 4, 5]
#[5, 8, 11, 14, 17]


