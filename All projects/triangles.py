import math
import sys

s1 = float(sys.argv[1])
s2 = float(sys.argv[2])
s3 = float(sys.argv[3])

def is_valid(s1, s2, s3):
    if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
        return True
    else:
        return False

def area(s1, s2 ,s3):
    s = (s1 + s2 + s3) /2
    area =math.sqrt((s * (s - s1) * (s - s2) * (s - s3)))
    return(area) #we can return from 2nd line but this is neater

if is_valid(s1, s2, s3):
    print("Valid triangle.", end = ' ')
    print(area(s1, s2, s3))

else:
    print("Invalid triangle")
