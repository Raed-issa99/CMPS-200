import build_die
import sys
face=int(sys.argv[1])
weight=int(sys.argv[2])
times=int(sys.argv[3])
faces={1:0,2:0,3:0,4:0,5:0,6:0}
die=build_die.Die(face,weight)
for i in range(times):
    faces[die.roll()]+=1
x=1/(6*(times)**2)
sum=0
for i in faces:
    sum+=((6*faces[i]-times)**2)
x=x*sum
if x<0.02:
    print("Fair Die,Chi-square = {0}".format(x))
else:
    print("Unfair Die,chi-square = {0}".format(x))