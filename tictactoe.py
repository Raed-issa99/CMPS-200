#TIC TAC TOE game
import random
# function to print a tic-tao-toe grid stored as a list of 3 lists
def print_grid(grid):
    for row in grid:
        for e in row:
            print(e, end = ' ')
        print()

# test the function print_grid
g = [ ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'] ]



def check_win(grid, player):
    '''your code goes here'''

    win=False

    for row in grid:
        for winner in player:
            if row[0]==row[1]==row[2]==winner:
                print("{0} wins".format(winner))
                win=True

    for column in range(len(grid)):
            for winner in player:
                if grid[0][column]==grid[1][column]==grid[2][column]==winner:
                    print("{0} wins".format(winner))
                    win=True

    for winner in player:
        if grid[0][0]==grid[1][1]==grid[2][2]==winner or grid[0][2]==grid[1][1]==grid[2][0]==winner:
            print("{0} wins".format(winner))
            win=True

    return win

check_win(g,['x','o'])

def emptycells():
    empty_cells=[]
    for emptyrow in range(len(g)):
        for emptycolumn in range(len(g)):
            if g[emptyrow][emptycolumn]=="_":
                empty_cells+=[(emptyrow,emptycolumn)]
    return empty_cells

def get_user_pick(empty_cells, grid):

    row= int(input("it's the user's turn.\nPlease enter the row: "))
    column=int(input("Please enter the column: "))

    while (row>2 or row<0) or (column>2 or column<0) or not (row,column) in empty_cells:
        row= int(input("Please enter a valid number.\nPlease enter the row: "))
        column=int(input("Please enter the column: "))

    if (row,column) in empty_cells:
        grid[row][column]="x"

    emptycells()
    print_grid(g)

    print('\n-------------------')


def computer_pick(empty_cells, grid):
    '''your code goes here'''

    row=random.randint(0,2)
    column=random.randint(0,2)

    while not (row,column) in empty_cells:
        row=random.randint(0,2)
        column=random.randint(0,2)

    if (row,column) in empty_cells:
        grid[row][column]="o"

    emptycells()
    print_grid(g)

    print('\n-------------------')

def tictactoe():
    ''' Your code goes here'''
    dice=random.randint(1,10)
    
    while not check_win(g,['x','o']):

        if emptycells()==[]:
            print('its a tie')
            break

        if dice%2==1:
            dice=dice+1
            computer_pick(emptycells(), g)

        else:
            get_user_pick(emptycells(),g)
            dice=dice+1


# start the game
tictactoe()
