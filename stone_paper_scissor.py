import random

while True:
   
    random_num = random.randint(1, 3)

    user = int(input("Enter your choice (Stone = 1, Paper = 2, Scissor = 3): "))
    if user == 1:
        print("You chose Stone 🪨")
    elif user == 2:
        print("You chose Paper 📄")
    elif user == 3:
        print("You chose Scissor ✂️")
    else:
        print("Invalid choice! Please choose between 1 and 3.\n")

        continue
    
    if random_num == 1:
        print("Computer chose Stone 🪨")
    elif random_num == 2:
        print("Computer chose Paper 📄")
    elif random_num == 3:
        print("Computer chose Scissor ✂️")
    if user == random_num:
        print("It's a draw!")
    elif (user == 1 and random_num == 3) or (user == 2 and random_num == 1) or (user == 3 and random_num == 2):
        print("🎉 You win!")
    else:
        print("Computer wins! Try next time 😊")

    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Good bye 👋")
    break
