import math
import sys
import turtle

turtle.speed(250)

t = turtle.Turtle

def polyline(n, length, angle):
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)

def polygon(n, length):
    polyline(n, length, 360.0/n)

def arc(r, angle):
    arc_length = 2* math.pi * r * angle / 360
    n = int(arc_length/3)+1
    step_length = arc_length / n
    step_angle = float(angle)/ n
    polyline(n, step_length, step_angle )

def circle(r):
    arc(r, 360)

def petal(r,angle):
    for i in range(2):
        arc(r, angle)
        turtle.left(180 - angle)

def flower(n, r, angle):
    for i in range(n):
        petal (r, angle)
        turtle.left(360/n)

def move(length):
    turtle.up()
    turtle.forward(length)
    turtle.down()

turtle.color('red')
def turtledown():
    turtle.right(90)
    turtle.forward(275)
turtle.begin_fill()
flower (10,105,80)
turtle.color('red')
turtledown()
turtle.end_fill()
turtle.right(180)
turtle.forward(45)
turtle.color('green')
petal(70,55)
turtle.left(27.5)
turtle.forward(65)

turtle.down()




turtle.done()
