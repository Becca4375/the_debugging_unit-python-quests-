# Define functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add, subtract, multiply, divide): ").lower()

# Perform calculation using if-elif-else
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation"

# Display result
print(f"Result: {result}")
