import math
import sys
a = float(sys.argv[1])

def mysqrt(a):
    x = a
    while abs(a- (x**2)) >= 10**(-7):
        x = (x + (a/ x))/2
    return x

print("the squareroot of", a,"is:",mysqrt(a))
