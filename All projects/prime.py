import math
import sys

numbers = sys.argv

numbers = [] #Convert strings in list to intigers
for s in sys.argv[1:]:
    numbers += [int(s)]

def is_prime(n):
    if n <= 1:
        return(False)
    else:
        for i in range(2,n):
            if n % i == 0:
                return(False)
        else:
            return(True)

def sum_prime(numbers): #Prints the prime numbers on a line and their sum on the other line
    count = 0
    for i in numbers:
        if is_prime(i):
            print(i, end = " ")
            count += i
    print()
    print("The sum is:",count)
    return(count)


sum_prime(numbers)
