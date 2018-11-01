import random
word_list = ["champion", "meticulous", "hexagon", "handsome", "beautiful", "chicken"]

count_wrong = 0

while True:
    random_word = random.choice(word_list)
    word = list(random_word)
    random.shuffle(word)

    for letter in word:
        print(letter, end = " ")
    print()

    answer = input("Your answer: ")

    if answer == random_word:
        print("Hura!")
        count_wrong = 0
    else:
        print("Sorry. Your answer is incorrect.")
        count_wrong += 1
    if count_wrong == 5:
        print("You're wrong too much. Please come back later")
        break
