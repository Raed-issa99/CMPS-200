import random
import turtle

colors_list = ['salmon','blue','red','purple']
def cpolygon(n, size, colors):
        for i in range(n):
            turtle.color(random.choice(colors))
            turtle.forward(size)
            turtle.left(360.0/n)
        turtle.done()

cpolygon(8, 100, colors_list)
