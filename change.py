import sys

values = [100,50,20,10,5,1]
n = int(sys.argv[1])
filename = sys.argv[2]


def make_change(n):
    change = tuple()
    remainder = n
    for i in values:
        bill,remainder = divmod(remainder,i)
        change += (bill,)
    return(change)


def output(n):
    s = ''
    for i,j in zip(make_change(n),values):
        if i != 0:
            s+= ('%d  LBP %3s,000' %(i,j))
            s+= '\n'
    print(s)
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        f = open(filename, 'w')
        f.write(s)
        f.close()

output(n)
