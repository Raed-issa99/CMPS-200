import sys
li = sys.argv[1:]

def strings2ints(slist):
    li = []
    for i in slist:
        li += [int(i)]
    return li


def lmax(listx):
    maxes = [] # the list that will contain the local maxima
    for i in range(1, len(listx)-1 ): #i can't be the first nor the last items in the list since they can't be local maximas
        if listx[i] > listx[i+1] and listx[i] > listx[i-1] :#if element of index i is > than elements of indecies i-1 and i+1, add it to the list
            maxes += [listx[i]]
    return maxes


def list2sentance(listy): #transforms a list, into a sentance (elements concatinated with a space between)
    for i in listy:
        print(i, end= ' ')

print('local maxima are:', end = ' ')
list2sentance(lmax(strings2ints(li)))
