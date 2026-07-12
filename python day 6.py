# IF ELSE ELIF


num = 7

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Output: Odd Number


age = 20

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

# Output: Eligible to Vote


a = 45
b = 20

if a > b:
    print(a, "is Greater")
else:
    print(b, "is Greater")

# Output:45 is Greater


marks = 55

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# Output:Pass


year = 2024

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

# Output:Leap Year



temp = 18

if temp > 35:
    print("Hot")
elif temp >= 20:
    print("Pleasant")
else:
    print("Cold")

# Output:Cold



a = 25
b = 80
c = 60

if a > b and a > c:
    print(a, "is Largest")
elif b > c:
    print(b, "is Largest")
else:
    print(c, "is Largest")

# Output:80 is Largest




num = 35

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

# Output:Divisible by 5




ch = "@"

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

# Output:Special Character



day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

# Output:Weekend



temperature = 40

if temperature > 35:
    print("It's a hot day")

# Output:It's a hot day




cart_items = 6
if cart_items >= 5:
    print("Free Delivery Unlocked")

# Output: Free Delivery Unlocked




otp = 1234
entered_otp = 1234

if otp == entered_otp:
    print("OTP Verified")
else:
    print("Invalid OTP")

# Output:OTP Verified


stock = 0

if stock > 0:
    print("Product Available")
else:
    print("Out of Stock")

# Output: Out of Stock



speed = 110

if speed > 120:
    print("Overspeeding")
elif speed >= 60:
    print("Normal Speed")
else:
    print("Slow Vehicle")

# Output:Normal Speed



cloud = "AWS"

if cloud == "Azure":
    print("Microsoft Cloud")
elif cloud == "AWS":
    print("Amazon Cloud")
else:
    print("Other Cloud")

# Output:Amazon Cloud


disk_space = 8

if disk_space < 10:
    print("Storage Almost Full")

# Output: Storage Almost Full



camera = False

if camera:
    print("Camera Enabled")
else:
    print("Camera Disabled")

# Output: Camera Disabled




day = "Friday"

if day == "Monday":
    print("Start Working")
elif day == "Friday":
    print("Weekend is Near")
else:
    print("Regular Day")

# Output: Weekend is Near



wifi = True

if wifi:
    print("Connected")
else:
    print("Not Connected")

# Output: Connected


status = "Stopped"

if status == "Running":
    print("Server is Live")
elif status == "Stopped":
    print("Start the Instance")
elif status == "Terminated":
    print("Cannot Restart")
else:
    print("Unknown Status")

# Output: Start the Instance


attendance = 68
if attendance >= 75:
    print("Exam Allowed")
else:
    print("Exam Not Allowed")
# Output:Exam Not Allowed





