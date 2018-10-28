items = ["T-Shirt", "Sweater"]
act_list = ["C", "R", "U", "D", "Stop"]

act = input("Welcome to our shop, what do you want: C, R, U, D or Stop? ")

while (act not in act_list):
    act = input("Please type exactly the action (notice the upper case): C, R, U, D or Stop? ")

while (act in act_list):
    if act == "Stop":
        print("Thanks for coming. See you next time!")
        break
    else: 
        if act == "C":
            new = input("Enter new item: ")
            items.append(new)
        elif act == "U":
            pos = int(input("Update position? "))
            while pos < 1 or pos > len(items):
                print("Position must start from 1 and we only have", len(items), "items now")
                pos = int(input("Update position? "))
            new = input("Enter new item: ")
            items[pos - 1] = new
        elif act == "D":
            pos = int(input("Delete position? "))
            while pos < 1 or pos > len(items):
                print("Position must start from 1 and we only have", len(items), "items now")
                pos = int(input("Delete position? "))
            items.pop(pos - 1)
        print("Our items: ", end = "")
        print(*items, sep = ", ")
        act = input("Welcome to our shop, what do you want: C, R, U, D or Stop? ")
        while (act not in act_list):
            act = input("Please type exactly the action (notice upper case): C, R, U, D or Stop? ")