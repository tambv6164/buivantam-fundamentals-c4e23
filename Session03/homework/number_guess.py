from random import randint

while True:
    correct = randint(1, 100)
    num = int(input("Guess my number (1 - 100)? "))
    while num != correct:
        if num < correct:
            print("Too small :(")
        else: 
            print("A litte too large :(")
        num = int(input("Guess my number (1 - 100)? "))
    print("Bingo")

