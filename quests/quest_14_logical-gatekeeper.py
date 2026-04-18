# Ask user for input
age = int(input("Enter your age: "))
gold = int(input("Enter how many gold coins you have: "))

# Check conditions
if age >= 18 and gold >= 20:
    print("Access Granted. You may enter the club.")
else:
    print("Access Denied. You do not meet the requirements.")
