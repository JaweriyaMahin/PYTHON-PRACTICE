# remove list duplicate 

instance_ids = [
    "i-101", "i-102", "i-101",
    "i-103", "i-102", "i-104"
]

unique_instances = list(dict.fromkeys(instance_ids))

print(unique_instances)

# Output:
# ['i-101', 'i-102', 'i-103', 'i-104']


images = [
    "nginx",
    "ubuntu",
    "nginx",
    "redis",
    "ubuntu"
]

print(list(dict.fromkeys(images)))

# Output:
# ['nginx', 'ubuntu', 'redis']



employee_ids = [101, 102, 103, 101, 105, 103]

result = []

for emp in employee_ids:
    if emp not in result:
        result.append(emp)

print(result)

# Output:
# [101, 102, 103, 105]



servers = [
    "web01",
    "db01",
    "web01",
    "cache01",
    "db01"
]

print(list(dict.fromkeys(servers)))

# Output:
# ['web01', 'db01', 'cache01']



regions = [
    "us-east-1",
    "ap-south-1",
    "us-east-1",
    "eu-west-1"
]

print(list(dict.fromkeys(regions)))

# Output:
# ['us-east-1', 'ap-south-1', 'eu-west-1']



logs = [
    "INFO",
    "ERROR",
    "INFO",
    "WARNING",
    "ERROR"
]

print(list(dict.fromkeys(logs)))

# Output:
# ['INFO', 'ERROR', 'WARNING']



#Reverse a String

region = "ap-south-1"

print(region[::-1])

# Output:
# 1-htuos-pa


filename = "backup.tar.gz"

print(filename[::-1])

# Output:
# zg.rat.pukcab

username = "devopsadmin"

print(username[::-1])

# Output:
# nimdaspoved



#Add Two Numbers

dev_cost = 4500
prod_cost = 12500

total = dev_cost + prod_cost

print(total)

# Output:
# 17000


images = 230
videos = 870

print(images + videos)

# Output:
# 1100


docker1 = 8
docker2 = 12

print(docker1 + docker2)

# Output:
# 20


ec2_bill = 14500
s3_bill = 3200

print(ec2_bill + s3_bill)

# Output:
# 17700

