import build_die
import sys
n=int(sys.argv[1])
times=int(sys.argv[2])
def count_occurances(times,n,d1,d2):
    counter=0
    for i in range(times):
        if build_die.Dice_Pair(d1,d2).roll()==n:
            counter+=1
    print("{0} was rolled {1} times out of {2}".format(n,counter,times))
d1=build_die.Die(3,20)
d2=build_die.Die(3,20)
count_occurances(times,n,d1,d2)