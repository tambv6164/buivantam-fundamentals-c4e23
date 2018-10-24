from turtle import *
pensize(2)

for i in range(3, 7):
    if i%2 == 1:
        color("blue")
    else:
        color("red")
    n = i
    for i in range(n):
        forward(100)
        left(360/n)

mainloop()