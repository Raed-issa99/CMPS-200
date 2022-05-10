import math
import turtle
import sys
turtle.speed(1000)

n = int(sys.argv[1])
def draw(length,n):
    if n == 0:
        return
    angle = 50
    turtle.forward(length*n)
    turtle.left(angle)
    draw(length, n-1)
    turtle.right(2*angle)
    draw(length, n-1)
    turtle.left(angle)
    turtle.forward(-length*n)

draw(8, n)
turtle.done()
