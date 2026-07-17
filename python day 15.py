import json

patient = {
    "patient_id": 101,
    "name": "Rahul",
    "blood_group": "O+"
}

print(json.dumps(patient))

# Output:
# {"patient_id": 101, "name": "Rahul", "blood_group": "O+"}



import json

ticket = {
    "flight": "AI202",
    "from": "Delhi",
    "to": "Mumbai"
}

print(json.dumps(ticket))

# Output:
# {"flight": "AI202", "from": "Delhi", "to": "Mumbai"}


import json

mobile = {
    "brand": "Samsung",
    "ram": "8GB",
    "storage": "128GB"
}

print(json.dumps(mobile, indent=2))

# Output:
# {
#   "brand": "Samsung",
#   "ram": "8GB",
#   "storage": "128GB"
# }




import json

cart = [
    {"item": "Keyboard", "qty": 1},
    {"item": "Mouse", "qty": 2}
]

print(json.dumps(cart))

# Output:
# [{"item": "Keyboard", "qty": 1}, {"item": "Mouse", "qty": 2}]



import json

weather = {
    "city": "Pune",
    "temperature": 29,
    "condition": "Cloudy"
}

print(weather["temperature"])

# Output:
# 29


import json

movies = [
    {"title": "Inception"},
    {"title": "Interstellar"}
]

print(len(movies))

# Output:
# 2



import json

library = {
    "book": "Python Basics",
    "author": "John Smith"
}

print(json.dumps(library))

# Output:
# {"book": "Python Basics", "author": "John Smith"}


import json

menu = {
    "pizza": 299,
    "burger": 149,
    "coffee": 99
}

print(menu["burger"])

# Output:
# 149



import json

score = {
    "team": "India",
    "runs": 320,
    "overs": 50
}

print(json.dumps(score))

# Output:
# {"team": "India", "runs": 320, "overs": 50}



import json

account = {
    "account_no": 12345678,
    "balance": 50000
}

print(account["balance"])

# Output:
# 50000



import json

students = [
    {"name": "Ali"},
    {"name": "Sara"}
]

print(json.dumps(students))

# Output:
# [{"name": "Ali"}, {"name": "Sara"}]



import json

data = '[1,2,3,4,5]'
numbers = json.loads(data)

print(len(numbers))

# Output:
# 5




import json

student = '{"name":"Aman"}'
data = json.loads(student)

data["age"] = 21

print(json.dumps(data))

# Output:
# {"name": "Aman", "age": 21}



import json

student = {"name": "Riya", "age": 20}

del student["age"]

print(json.dumps(student))

# Output:
# {"name": "Riya"}


