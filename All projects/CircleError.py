import math
import turtle


turtle.color('red')

def polygon(n,length):
    for i in range(n):
        turtle.forward(length)
        turtle.left(360.0/n)

def circle(r):
    circumference = 2* math.pi *r
    n = circumference//3 + 1
    print(type(n))
    length = circumference / n
    polygon (n, length)

circle(100)
turtle.done()
