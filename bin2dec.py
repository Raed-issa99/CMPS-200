import sys
n = sys.argv[1]
dec = 0
for i in range(1,len(n)+1):
    if n[-i] == '1':
        dec += 2**(i-1)
print(dec)
