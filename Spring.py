import sys
m= int(sys.argv[1])
d= int(sys.argv[2])

spring= (m== 3 and 21<=d<=31) or (m==4 and 1<=d<=30) or (m==5 and 1<=d<=31) or (m==6 and 1<=d<=20)
print(spring)
