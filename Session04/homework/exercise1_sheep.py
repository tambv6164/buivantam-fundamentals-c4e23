mysheeps = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep.")

month = 0
total_flock = 0

price = 2
default_size = 8

def typeagain(x):
    while x not in ["Y", "N"]:
        x = input("Sorry. Please type Y of N: ").upper()

def print_mysheep():
    print("My flock now:")
    print(mysheeps)
    print()

while True:
    print_mysheep()
    if all(i <= 8 for i in mysheeps):
        print("Your flock is too low. Please grow it for shearing in the future.")

    grow_ask = input("Grow one more month?: Y for Yes or N for No: ").upper()
    typeagain(grow_ask)
    if grow_ask == "Y":
        print("One month has passed.")
        for i in range(len(mysheeps)):
            mysheeps[i] += 50
        month += 1
        print("MONTH", month)
    print_mysheep()

    if not (all(i <= 8 for i in mysheeps)):
        print("Now, my biggest sheep has size", max(mysheeps), ".")
        shear_ask = input("Let shear it. Y for Yes or N for No: ").upper()
        typeagain(shear_ask)
        if shear_ask == "Y":
            mysheeps[mysheeps.index(max(mysheeps))] = default_size
            print("After shearing:")
        print_mysheep()
    else:  
        print("You can't shear. Because you don't grow the flock.")
        shear_ask = "N"

    total_flock_ask = input("Wanna know your total money will get now? Y for Yes or N for No: ").upper()
    typeagain(total_flock_ask)
    if total_flock_ask == "Y":
        for i in mysheeps:
            total_flock += i
        print("My flock has size in total:", total_flock)
        print("I would get", total_flock, "*", price, "$ =", total_flock*price, "$")
        break
    
    if grow_ask == "N" and shear_ask == "N" and total_flock_ask == "N":
        print("Thank for comming ^^. See you next time!")
        break
