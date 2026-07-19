#  python RegEx

import re

text = "Python 123 Java 456"
result = re.findall(r"\d+", text)

print(result)

# Output:['123', '456']


import re

text = "Welcome to Python"
result = re.search("Python", text)

print(result.group())

# Output: Python


import re

text = "Python Programming"
result = re.match("Python", text)

print(result.group())

# Output: Python

import re

text = "apple,banana;orange"
result = re.split(r"[,;]", text)

print(result)

# Output:['apple', 'banana', 'orange']


import re

text = "I like Java"
result = re.sub("Java", "Python", text)

print(result)

# Output:I like Python


import re

text = "Python Java C++"
result = re.findall(r"\w+", text)

print(result)

# Output:['Python', 'Java', 'C']


import re

text = "Email: test@gmail.com"
result = re.search(r"\S+@\S+", text)

print(result.group())

# Output:test@gmail.com


import re

text = "Python123"
result = re.sub(r"\d", "", text)

print(result)

# Output:Python


import re

text = "PyTHon"
result = re.findall(r"[A-Z]", text)

print(result)

# Output:['P', 'T', 'H']


import re

text = "Python is easy"
result = re.split(r"\s+", text)

print(result)

# Output:['Python', 'is', 'easy']


