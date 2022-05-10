import turtle
import math


def isosceles(r,angle):
    y = r* math.sin(angle*math.pi)/180
    turtle.right(angle)
    turtle.forward(r)
    turtle.left(90+angle)
    turtle.forward(2*y)
    turtle.left(90+angle)
    turtle.forward(r)
    turtle.left(180-angle)


def polypie(n,r):
    angle = 360.0/n
    for i in range(n):
        isosceles(r,angle/2)
        turtle.left(angle)




def draw_pie(n,r):
    polypie(n,r)
    turtle.up()
    turtle.forward(r*2 +10)
    turtle.down()

isosceles(100,60)


turtle.done()
