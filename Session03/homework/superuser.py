print("Hi there, this is a super user gateway")
usn = input("Username: ")
if usn != "c4e":
    print("You are not superuser")
else:
    pwd = input("Password: ")
    if pwd != "codethechange":
        print("Password is incorrect")
    else:
        print("Welcome, c4e")