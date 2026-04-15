# Function to ask the user for their age and return it
def ask_for_age():
    age = int(input("Enter your age: "))
    return age


# Function to check if the person can vote
def can_they_vote(age):
    if age >= 18:
        print("You are old enough to vote.")
    else:
        print("You are not old enough to vote.")


# Call first function and store returned value
user_age = ask_for_age()

# Pass the returned age into the second function
can_they_vote(user_age)