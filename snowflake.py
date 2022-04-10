import turtle
import math


def koch(n):
    if n<3:
        turtle.fd(n)
        return
    m = n/3.0
    koch(m)
    turtle.lt(60)
    koch(m)
    turtle.rt(120)
    koch(m)
    turtle.lt(60)
    koch(m)

def snowflake(n):
    for i in range(3):
        koch(n)
        turtle.rt(120)
turtle.tracer(0)
snowflake(300)
turtle.update()
turtle.done()
