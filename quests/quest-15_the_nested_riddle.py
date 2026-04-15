direction = input("Do you go left or right? ").lower()

if direction == "left":
    action = input("You see a river. Do you swim or wait? ").lower()
    
    if action == "swim":
        print("You swam across and found the treasure! 🎉")
    else:
        print("You waited too long. The opportunity is gone.")
        
else:
    print("You went right and fell into a trap. Game over!")