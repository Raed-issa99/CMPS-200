import sys
n = int(sys.argv[1])
r = int(sys.argv[2])
c = int(sys.argv[3])

def line_o(n): #Draws a row of O's (will be used when row = r)
    for i in range(n):
        print("o", end = ' ')
    print()


for e in range(n):
    if e == r: #if the e has same index as the row r that is O's, it prints a row of O's
        line_o(n)
    else:
        for i in range (n): #loop to draw  the x and o's of every row
            if i == (c):  #if the i is same as the index of the column that's O's( the c ) if so, print o, else print x
                print("o", end = ' ')
            else:
                print("x", end = ' ')
        print() #new line after every row is done
