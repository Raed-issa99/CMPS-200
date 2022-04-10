import sys

n = int(sys.argv[1])

def triangle(n):
    for i in range(n):
        for j in range(i):
            print ('.' , end = ' ')
        for s in range(n-i):
            print ('*' , end = ' ')
        print()

triangle(n)
