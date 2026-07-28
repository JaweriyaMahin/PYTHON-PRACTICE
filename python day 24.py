# Exception HANDLING


try:
    username = "admin"
    password = input("Enter password: ")

    if password != "12345":
        raise Exception("Invalid Password")

    print("Login Successful")

except Exception as e:
    print(e)
#Output: Input:Enter password: 1111
#Invalid Password


try:
    port = int(input("Enter port number: "))

    if port == 8080:
        raise Exception("Port already in use")

    print("Application Started")

except Exception as e:
    print(e)
#output: Enter port number: 8080
#Port already in use


try:
    instance_status = "stopped"

    if instance_status != "running":
        raise Exception("EC2 instance is not running")

    print("Server is healthy")

except Exception as e:
    print(e)

# Output:EC2 instance is not running


try:
    disk_usage = int(input("Enter disk usage (%): "))

    if disk_usage > 80:
        print("Warning: Disk usage is high")
    else:
        print("Disk usage is normal")

except ValueError:
    print("Invalid input. Please enter numbers only.")

# Input:abc

# Output:Invalid input. Please enter numbers only.


server_status = False

try:
    if not server_status:
        raise ConnectionError("Unable to connect to EC2 server")

    print("Connected Successfully")

except ConnectionError as e:
    print(e)

# Output: Unable to connect to EC2 server


try:
    file = open("application.log", "r")
    print(file.read())

except FileNotFoundError:
    print("Log file not found.")

# Output: Log file not found.




try:
    source = "backup.zip"

    if source != "project.zip":
        raise FileNotFoundError("Backup file not found")

    print("Backup Started")

except FileNotFoundError as e:
    print(e)

# Output: Backup file not found


deployment_ready = False

try:
    if not deployment_ready:
        raise Exception("Deployment failed")

    print("Application Running")

except Exception as e:
    print(e)

# Output: Deployment failed


try:
    balance = 5000
    withdraw = int(input("Enter amount: "))

    if withdraw > balance:
        raise Exception("Insufficient Balance")

    print("Transaction Successful")

except Exception as e:
    print(e)

#Output:
#Input:7000
#Output:Insufficient Balance



