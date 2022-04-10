import math
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

delta = b**2 - 4*a*c

if (delta) < 0:
    print("no real roots exist")

elif (delta) == 0:
    print((-b + math.sqrt(delta))/(2*a))
elif (delta) > 0:
    print((-b - math.sqrt(delta))/(2*a),(-b + math.sqrt(delta))/(2*a))
