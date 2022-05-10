import turtle
import random
import time
# function to draw the race course: n vertical striped lines at 20-pixel intervals.
# The function stops animating the process initially, but resets
# the animation seting after it is done.
def draw_course(n):
    turtle.tracer(0, 0)      # stop animating the drawing process
    for i in range(n):
        draw_stripedline(i)
        turtle.forward(20)
    turtle.hideturtle()      # hide the arrow shape
    turtle.update()          # show the race course
    turtle.tracer(1)         # resume animating the drawing process
    turtle.speed(1)          # set drawing speed to the slowest value


# function to draw a vertical striped line 100 pixels long, consisting of
# five segments
def draw_stripedline(line):
    turtle.write(line, align='center')
    turtle.right(90)
    for num in range(5):
        turtle.up()
        turtle.forward(10)
        turtle.down()
        turtle.forward(10)
        turtle.up()
    turtle.backward(100)
    turtle.left(90)


# function that takes in a list of turtles and places them at the
# start line (x = 0)
def place_turtles(turtles):
    location = 0
    for t in turtles:
        location -= 25
        t.up()
        t.goto(0, location)
        t.down()


# function that takes in a list of turtles and simulates a race between them
def turtlerace(turtles):
    a_counter = 0
    b_counter = 0
    while a_counter < 200 and b_counter < 200:
        time.sleep(0.01)
        dicea = random.randint(1,6)
        diceb = random.randint(1,6)
        if dicea > diceb:
            alice.forward(dicea)
            a_counter += dicea
        elif diceb > dicea:
            bob.forward(diceb)
            b_counter += diceb
    if a_counter > b_counter:
        return 'Alice, the red turtle!'
    else:
        return 'Bob, the blue turtle!'
# main part of the program: draws the course, create two turtles, start the
# race, and print color of winner
draw_course(11)

alice = turtle.Turtle()
alice.color('red')
alice.shape('turtle')

bob = turtle.Turtle()
bob.color('blue')
bob.shape('turtle')

place_turtles([alice, bob])

winner = turtlerace([alice, bob])
print('The winner is:', winner)
turtle.done()
