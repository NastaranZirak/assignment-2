import random

pc_number = random.randint(0, 20)
N = 0
while True:
    user_number = int(input("Enter a number between 0,20 = "))
    N += 1

    if pc_number == user_number:
        print("YOU WON!")
        print("your number of tries: ", N)
        break

    if pc_number < user_number:
        print("GO LOWER")

    else:
        print("GO HIGHER")