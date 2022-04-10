import sys

def strings2floats(ls1):
    ls = []
    for s in ls1:
        ls += [float(s)]
    return(ls)

def positive_min(lf):
    s = 0 #assigns the first positive number to s to be compared with the other numbers
    for i in lf:
        if i > 0:
            s =  i
            break
    if s == 0: #if there are no positive numbers (>0) return none
        return None
    for i in lf: #compares numbers in list to s, and assigns the number to s if it's < s
        if i < s and i > 0:
            s = i
    return s

ls = sys.argv[1:]
print(positive_min(strings2floats(ls)))
