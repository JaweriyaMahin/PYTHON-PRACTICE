# python match 

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
#output: thursday


day = 6
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
#output: today is saturday


day = 1
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
# output: today is a weekday


month = 4
day = 3
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
# output: a weekday in april


operation = "+"
match operation:
    case "+":
        print("Addition")
    case "-":
        print("Subtraction")
    case "*":
        print("Multiplication")
    case "/":
        print("Division")
    case _:
        print("Invalid Operation")
# Output: Addition


service = "EC2"
match service:
    case "EC2":
        print("Virtual Server")
    case "S3":
        print("Object Storage")
    case "IAM":
        print("Access Management")
    case _:
        print("Service Not Found")
# Output: Virtual Server


month = 8

match month:
    case 1:
        print("January")
    case 8:
        print("August")
    case 12:
        print("December")
    case _:
        print("Invalid Month")
# Output:August



status = "On"

match status:
    case "On":
        print("Device Running")
    case "Off":
        print("Device Stopped")
    case _:
        print("Unknown Status")
# Output: Device Running


grade = "A"
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case _:
        print("Needs Improvement")
# Output: Excellent




