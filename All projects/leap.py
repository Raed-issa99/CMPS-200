import sys
import math

y = int(sys.argv[1])
if y> 0:
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print(True)
    else:
        print(False)
