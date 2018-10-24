from turtle import *
color("red")
pensize(2)

for i in range(4):
    for i in range(2):
        left(60)
        forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)
    left(-30)

mainloop()