import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

inorder = (a>b>c) or (a<b<c)
print(inorder)
