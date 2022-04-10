import math
import random
import turtle
import sys

def square(size):
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)

turtle.speed(1000)


def set(x,y):
    turtle.up()
    turtle.setpos(x,y)
    turtle.down()

def c_circle(r,color):
    turtle.color('black', color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def c_square(size,r,color,x,y):
    set(x,y)
    square(size)
    set(x+size/2, y+size/2 - r)
    c_circle(r, color)


def grid(n, length):
    size = length/n
    x = - length/2
    y = - length/2
    for j in range(n):
        for i in range(n):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                color = 'red'
            else:
                color = 'black'
            c_square(size, size/5, color, x, y)
            x += size
        x = -length/2
        y += size

def grid_color(n,length,colors):
    size = length/n
    x = - length/2
    y = - length/2
    for j in range(n):
        for i in range(n):
            color = random.choice(colors)
            c_square(size, size/5, color, x, y)
            x += size
        x = -length/2
        y += size

n = int(sys.argv[1])
colors = ['blue','green','red','yellow','purple','salmon','brown']
grid_color(n, 200, colors)
turtle.ht()
turtle.done()
