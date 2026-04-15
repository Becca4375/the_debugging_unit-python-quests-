secret_number = 90
guess = None
while guess !=secret_number:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("correct! you guessed it")
    else:
        print("wrong guess, try again")
        print("Game over!")