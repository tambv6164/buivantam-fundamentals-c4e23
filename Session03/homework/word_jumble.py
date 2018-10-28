import random
word_list = ["champion", "meticulous", "hexagon", "handsome", "beautiful", "chicken"]

random_word = random.choice(word_list)
word = list(random_word)
random.shuffle(word)

for letter in word:
    print(letter, end = " ")
print()

answer = input("Your answer: ")

if answer == random_word:
    print("Hura!")
else:
    print("Sorry. Your answer is incorrect.")
