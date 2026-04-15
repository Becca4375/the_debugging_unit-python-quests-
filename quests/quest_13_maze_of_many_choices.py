# Get the score from the user
score = int(input("Enter your score (0-100): "))

# Grade the score using if-elif-else
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")
