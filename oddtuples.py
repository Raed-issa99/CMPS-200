def odd_tuples(tup):
    outtup= tuple()
    for c in range(len(tup)):
        if c % 2 == 0:
            outtup += (tup[c],)
    return outtup

x = "I","am","a","test","tuple"
print(odd_tuples(x))
