secret_code = 42
attempts = 3
while attempts > 0:
    guess = int(input("Enter the secret code: "))
    if guess == secret_code:
        print("Access Granted 🎉")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong code! You have {attempts} attempt(s) left.")
        else:
            print("Access Denied! No attempts left.")