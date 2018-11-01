print("Answer the following algebra question:")
quizz = {
    "If x = 1, then what is the value of x + 1:": [2, 3, 4, 5],
    "Calculate 2 multiply by itself 5 times:": [22, 24, 26, 28, 30, 32, 34],
    "What is the letter at position 2 of English Alphabet:": ["D", "B", "E"],
    "'One plus one minus one plus one plus one minus one' goes to:": [-2, -1, 0, 1, 2]
}
keys = {
    "If x = 1, then what is the value of x + 1:": 2,
    "Calculate 2 multiply by itself 5 times:": 32,
    "What is the letter at position 2 of English Alphabet:": "B",
    "'One plus one minus one plus one plus one minus one' goes to:": 2
}

while True:
    count_right = 0
    for (k, v) in quizz.items():
        print(k)
        for i in range(len(v)):
            print(i+1, v[i], sep = ". ")
        choice = int(input("Your choice: "))
        while choice == 0 or choice not in range(len(v) + 1):
            choice = int(input("Your choice is out of range. Type again: "))
        if v[choice - 1] == keys[k]:
            print("Ủ ôi, siêu quá, đúng dồi bạn ơi <3")
            count_right += 1
        else: 
            print("Sai rồi má :(. Thôi bỏ đi :(")
        print()
    print("You correctly answer", count_right, "of", len(quizz), "questions")
    play_again = input("Ready to play again? - Y for Yes and N for No: ").upper()
    while play_again not in ["Y", "N"]:
            play_again = input("Sorry. Please type Y of N: ").upper()
    if play_again == "N": 
        print("Thank you ^^. See you next time!")
        break
    print()
