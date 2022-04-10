import sys
name = sys.argv[1]
words = sys.argv[2:]
f = open(name,'r')
wordind= dict()
for i in words:
    wordind[i] = []

linenumber = 0
for line in f:
    linenumber +=1
    for char in words:
        if char in line:
            wordind[char] += [linenumber]


for i in wordind:
    vals = ''
    value = wordind[i]
    for b in value:
        vals += str(b) + ','
    print('%-15s' %(i), vals[0:-1])
