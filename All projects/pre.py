import math
import sys


li = sys.argv[1:]

def mean(li):
    total = 0.0
    for v in li:
        total += int(v) #it is not allowed to put int(v) in the 9th line (gives error)
    return total/len(li)#Returning allows u to use the value in another function

print(mean(li))
