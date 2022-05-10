import random
import sys


def shuffle(list):
    n = len(list)
    for i in range(n):
        r = random.randint(i, n-1)
        x = list[i]
        list[i] = list[r]
        list[r] = x



def listToSent(x): #Transforms a list into a sentence (elements outside the list)
    for i in range(len(x)):
        print(x[i], end = ' ')




shuflist = sys.argv[1:]
shuffle(shuflist)
listToSent(shuflist)
