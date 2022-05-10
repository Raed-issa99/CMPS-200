import random
import sys

n = int(sys.argv[1])


#with n = 10, value is around 3.4, with 100 it's more accurate, and with 10000 it's most accurate, the higher n the more accuracy
def monte(n):
    inQuarter = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inQuarter += 1
    return (4 * (inQuarter/n))

print(monte(n))
