import sys
from dset import Dset

n = sys.argv[1:]

def str2set(lst):
    sets = list()
    for i in lst:
        sets += [Dset(i)]
    return sets

def lst2union(lst):
    unionset = Dset()
    for s in lst:
        unionset = unionset.union(s)
    return unionset

print(lst2union(str2set(n)))
