import random

# Generate a secret number between 1 and 100
secret_number = random.randint(1, 100)

print("🧙‍♂️ Welcome to the Number Wizard!")
print("I have chosen a secret number between 1 and 100.")
print("Can you guess it?\n")

# Main game loop
while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Correct! The secret number was {secret_number}!")
            break

        elif guess < secret_number:
            print(" Too low! Try a higher number.")

        else:  # guess > secret_number
            print(" Too high! Try a lower number.")

    except ValueError:
        print(" Please enter a valid number.")
