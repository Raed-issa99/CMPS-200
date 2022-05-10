import sys

def is_pyth(tup):
    tup = sorted(tup)
    a,b,c = tup
    if a**2 + b**2 == c**2:
        return True
    return False

def is_multiple(tup):
    tup = sorted(tup)
    a,b,c = tup
    if a%3 == 0 and b%4 == 0 and c%5 == 0:
        return True
    return False

def triplets_n(n):
    triplets = []
    #Tries all the possible combinations of a,b,c such that a+b+c < n and check for neccesary conditionsZ
    for a in range(n):
        for b in range(n):
            for c in range(n):
                tup = (a,b,c)
                if (a + b + c < n) and is_pyth(tup) and not(is_multiple(tup)) and (a<b<c):
                    triplets += [tup]
    return(triplets)

n = int(sys.argv[1])
for i in (triplets_n(n)):
    print(i)
