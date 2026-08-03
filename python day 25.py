# 1. Class
class Student:
    pass

print(Student)

# Output:
# <class '__main__.Student'>


# 2. Object
class Student:
    pass

s1 = Student()
print(s1)

# Output:
# <__main__.Student object at 0x...>


# 3. Constructor (__init__)
class Student:

    def __init__(self):
        print("Constructor Called")

s1 = Student()

# Output:
# Constructor Called


# 4. Constructor with Parameters
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 22)

print(s1.name)
print(s1.age)

# Output:
# Ali
# 22


# 5. Method
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("sarah")
s1.display()

# Output:
# Student Name: sarah


# 6. Basic Inheritance
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()

# Output:
# Animal makes sound


# 7. Inheritance with Child Method
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()

# Output:
# Animal makes sound
# Dog barks


# 8. DevOps Example
class EC2:

    def __init__(self, instance_id):
        self.instance_id = instance_id

    def start(self):
        print(self.instance_id, "Started")

    def stop(self):
        print(self.instance_id, "Stopped")

server = EC2("i-123456789")

server.start()
server.stop()

# Output:
# i-123456789 Started
# i-123456789 Stopped