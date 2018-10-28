print("Hi there, this is a super user gateway")
usn = input("Username: ")
while usn != "c4e":
    print("You are not superuser")
    usn = input("Username: ")
pwd = input("Password: ")
while pwd != "codethechange":
    print("Password is incorrect")
    pwd = input("Password: ")
print("Welcome, c4e")
