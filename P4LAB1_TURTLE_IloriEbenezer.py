# CTI 11O
# P4LAB1 -Turtles
# Ilori Ebenezer
# 11//12/24

# draw shapes and snow falskes using for loops

# Set up the turtle
import turtle
t = turtle.Turtle()
# background
win = turtle.Screen()
win. bgcolor("black")
# add some display options

t.pensize(4)
t.pencolor("blue")
t.shape("turtle")


# triangle
for side in range(3):
    t.forward(100)
    t.right(120)
    
"""
t.pencolor("blue")
t.fillcolor ("cadetblue")
t.begin_fill()
for side in range (3):
    t.forward(100)
    t.left(120)
t.end_fill()
# octagon
t.pencolor("red")
for side in range(8):
    t.forward(50)
    t.left(50)    
t.pencolor("deeppink4")
for side in range(6):
    t.forward(60)
    t.right(60)
"""

# finally, a snowflake
t.pencolor("white")
for flake in range (60):
    color = "lemonchiffon1"
    t.pencolor(color)
    t.forward(100)
    t.back(20)
    # pointy bit on the end
    t.left(90)
    t.forward(10)
    t.back(20)
    t.right(180)
    t.forward(20)
    t.back(20)
    t.left(90)
    # end pointy bit
    t.back(120)
    t.left(28)
           



