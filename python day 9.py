from array import *

numbers = array('i', [10, 20, 30, 40])
print(numbers)
# Output
# array('i', [10, 20, 30, 40])


from array import *

numbers = array('i', [5, 10, 15, 20])
print(numbers[0])
print(numbers[2])

# Output
# 5
# 15


from array import *

numbers = array('i', [1, 2, 3])
numbers.append(4)
print(numbers)

# Output
# array('i', [1, 2, 3, 4])


from array import *

numbers = array('i', [10, 20, 40])
numbers.insert(2, 30)
print(numbers)
# Output
# array('i', [10, 20, 30, 40])


from array import *

numbers = array('i', [10, 20, 30, 40])
numbers.remove(20)
print(numbers)

# Output
# array('i', [10, 30, 40])


from array import *

numbers = array('i', [1, 2, 3, 4, 5])
numbers.reverse()
print(numbers)

# Output
# array('i', [5, 4, 3, 2, 1])



from array import *

numbers = array('i', [11, 22, 33, 44])
print(len(numbers))

# Output
# 4



from array import *

numbers = array('i', [100, 200, 300])
for num in numbers:
    print(num)

# Output
# 100
# 200
# 300



from array import *

numbers = array('i', [5, 10, 15])
print(sum(numbers))

# Output
# 30



from array import *

numbers = array('i', [45, 12, 78, 23])
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Output
# Maximum: 78
# Minimum: 12





