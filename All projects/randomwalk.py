import random
import turtle
"""
for i in range(6):
    print([(i,j) for j in range(5)])
"""


def manhattan(c,r):
    i = r//2
    j = c//2
    walked = [(i,j)]
    while i != r and  j != c and i > -1 and j > -1:
        step = random.randint(0,3)
        if step == 0:
            i += 1
        elif step == 1:
            i -= 1
        elif step == 2:
            j += 1
        else:
            j -= 1
        walked += [(i,j)]
    walked.pop(len(walked)-1)
#    print()
#    print()
#    print(walked)
    for i in range(r):
            print([walked.count((i,j)) for j in range(c)])
    return walked

x = manhattan(5,6)

def square(size):
    for i in range(4):
        turtle.forward (size)
        turtle.left(90)


def grid(c,r,size):
    turtle.setpos((c*size)/2,(r*size)/2)
    for i in range(c):
        for j in range(r):
            square(1)


grid(5,6,100)
for i in range(len(x)):
    a,r = x[i]
    print(a,r)
    turtle.setpos(a,r)
turtle.done()
