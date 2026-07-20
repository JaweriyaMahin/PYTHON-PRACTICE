## python string formating

# Python String Formatting Examples



name = "Alice"
print(f"Hello, {name}")

# Output:Hello, Alice



age = 22
print(f"Age: {age}")

# Output:Age: 22



price = 99.99
print(f"Price: ₹{price}")

# Output:Price: ₹99.99



a = 10
b = 20
print(f"Sum = {a + b}")

# Output:Sum = 30



city = "Mumbai"
print("City: {}".format(city))

# Output: City: Mumbai


name = "John"
age = 25
print("Name: {}, Age: {}".format(name, age))

# Output: Name: John, Age: 25




pi = 3.14159
print("{:.2f}".format(pi))

# Output:3.14




num = 7
print("{:03}".format(num))

# Output: 007



text = "Python"
print("{:<10}".format(text))

# Output:Python


text = "Python"
print("{:>10}".format(text))

# Output:Python



text = "Python"
print("{:^10}".format(text))

# Output: Python


value = 0.85
print("{:.0%}".format(value))

# Output:85%



name = "David"
print("Hello %s" % name)

# Output: Hello David




marks = 95
print("Marks = %d" % marks)

# Output: Marks = 95



salary = 45678.90
print(f"Salary: ₹{salary:,.2f}")

# Output: Salary: ₹45,678.90


