import sys
import turtle
import math

n = int(sys.argv[1])
d = int(sys.argv[2])

def circle(r):
    arc_length = 2* math.pi * r
    n = int(arc_length/3)+1
    step_length = arc_length / n
    step_angle = float(360)/ n
    for i in range(n):
        turtle.forward(step_length)
        turtle.left(step_angle)

turtle.tracer(0)
for i in range(n):
    circle(d)
    turtle.left(360/n)
turtle.ht()
turtle.update()
turtle.done()
