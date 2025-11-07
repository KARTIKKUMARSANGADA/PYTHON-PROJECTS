import random

print("WELCOME TO THE DICE ROLLING GAME🎲")
print("You will be playing against the computer.")
print("Both you and the computer will roll a dice, and the one with the higher number wins!")

while True:
    input("Press Enter to roll the dice...")
    
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    
    print(f"Your roll: {user_roll}")
    print(f"Computer's roll: {computer_roll}")
    
    if user_roll > computer_roll:
        print("🎉 You win!")
    elif user_roll < computer_roll:
        print("Computer wins! Try next time 😊")
    else:
        print("It's a draw!")
    
    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Good bye 👋")
        break
