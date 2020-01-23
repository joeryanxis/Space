# circleSpiralInput.py
import turtle

colors = ["red","blue","green","orange","purple","grey","white","brown"]
t = turtle.Pen()
turtle.bgcolor("Black")
sides = eval(input("How many sides (1-8) would you like?: \n"))
for x in range(360):
    t.pencolor(colors[x%sides])
    t.circle(x)
    t.left(x%sides)
    
