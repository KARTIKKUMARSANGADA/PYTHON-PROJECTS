import random

while True:

    random_num =random.randint(0,15)

    user = int(input("enter number betwn range (0,15):"))
    print("your number is:",user)
    print("random_num generated number is:",random_num)

    if user >15 or user<0:
        print("Invalid number")


    if user == random_num:
        print("you are winner")
    else:
        print("try next time, Thank you!")

    again = input("do you want to play again?(y/n)").lower()
    if again != 'y':
        print("good bye")
        break


