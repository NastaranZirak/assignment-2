import random

first = random.randint(1, 6)

if first == 6:
    second = random.randint(1, 6)
    third = random.randint(1, 6)
    print("YOU GOT A 6! you have two more tries")
    print("your second try is", second)
    print("your third try is", third)

else:
    print("you got a", first)