import math
import sys

def estimate_pi(tol):
    estpi = 0
    k = 0
    lastterm=10     #The first last term is 4, so just any number > 4 should work
    while abs(lastterm) >= tol:
        lastterm = ((-1)**k) * (4/(2*k+1)) #Calculates the current last term in order to compare it to the tol
        estpi += lastterm       #The current estimate of pie
        k += 1
    return(estpi)

e = float(sys.argv[1])
myPi = estimate_pi(e)
print("%1.5f" %(myPi,))
