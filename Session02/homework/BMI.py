mass = float(input("Your mass in kg: "))
height_cm = float(input("Your height in cm: "))
height_m = height_cm/100
BMI = mass/(height_m**2)
print("==> Your BMI =", BMI)
if BMI < 16:
    print("You are SEVERELY UNDERWEIGHT.")
elif BMI < 18.5:
    print("You are UNDERWEIGHT")
elif BMI < 25:
    print("You are NORMAL")
elif BMI < 30:
    print("You are OVERWEIGHT")
else:
    print("You are OBESE")