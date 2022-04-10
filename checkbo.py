import sys
import turtle

def square(size):
    for i in range(4):
        turtle.forward (size)
        turtle.left(90)

def filled_square(size, color, x, y):
    turtle.color(color)
    turtle.up()
    turtle.setpos(x, y)
    turtle.begin_fill()
    turtle.down()
    square(size)
    turtle.end_fill()

n= int(sys.argv[1])
board = 300
x = -200
y = -200

for r in range (1, n+1):
    for i in range(1,n+1):
        if (i%2 != 0 and r%2 !=0) or (i%2 == 0 and r%2 == 0): #i is column, r is row, without the index 0, when the row and column are both odd or even, color is red(pattern)
            color = 'red'
        else:
            color = 'black'
        filled_square(board/n, color , x, y)
        x += board/n #moves x coordinate to draw the 2nd square by size of 1 square
    y += board/n #moves y up by size of 1 square
    x = -200 #Resets x coordinate
turtle.ht() #Hides the turtle
turtle.done()
