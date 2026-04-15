def start():
    print("You wake up in a dark forest.")
    print("There are two paths: left or right.")

    choice = input("Do you go left or right? ").lower()

    if choice == "left":
        lake()
    elif choice == "right":
        cave()
    else:
        print("You stand still and get lost... Game over.")


def lake():
    print("\nYou arrive at a peaceful lake.")
    print("You see a boat and a bridge.")

    choice = input("Do you take the boat or the bridge? ").lower()

    if choice == "boat":
        print("The boat sinks... Game over.")
    elif choice == "bridge":
        print("You safely cross and find treasure! You win 🎉")
    else:
        print("You hesitate too long and night falls... Game over.")


def cave():
    print("\nYou enter a dark cave.")
    print("You see glowing eyes.")

    choice = input("Do you run or investigate? ").lower()

    if choice == "run":
        print("You escape safely! You win 🎉")
    elif choice == "investigate":
        print("It's a sleeping dragon... Game over.")
    else:
        print("You freeze in fear... Game over.")


# Start the game
start()