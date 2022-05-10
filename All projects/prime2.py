import sys
n = int(sys.argv[1])

def is_prime(n): # the older version was simpler to read and follow its execution.
    i = 2
    prime = True
    while i < n and prime:
        if n % i == 0:
            prime = False
        i += 1
    if n <= 1:
        prime = False
    return prime




print (is_prime(n))
