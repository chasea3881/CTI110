# Adriana Chase
# 7/4/2025
# P4Lab1-2
# Initials

import turtle
ac = turtle.Turtle()
win = turtle.Screen()

# Draw A
i = 0
while i < 1:
    ac.left(75)
    ac.forward(100)
    i = i + 1

i = 0
while i < 1:
    ac.right(150)
    ac.forward(100)
    i = i + 1

i = 0
while i < 1:
    ac.backward(50)
    ac.left(75)
    ac.backward(25)
    #Move to C
    ac.forward (100)
    i = i + 1 


# Draw C
i = 0
while i < 1:
    ac.right(90)
    ac.forward(50)
    ac.left(90)
    ac.forward(50)
    ac.backward(50)
    ac.left(90)
    ac.forward(90)
    ac.right(90)
    ac.forward(50)
    i = i + 1
i = 0

win.mainloop()
