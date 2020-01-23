# squareSpiral.py - draws a square spiral
import turtle
t = turtle.Pen()
turtle.bgcolor("Black")
colors = ["Red","Blue","Green","Yellow","Purple","Brown"]
sides = eval(input("Enter the number of sides you'd like: \n"))
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides)
    t.left(91)
