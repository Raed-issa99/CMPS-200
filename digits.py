import sys
import math

def last_digit(number):
    return (number % 10)


def nth_digit(number, n):
        s = (number // (10**(n)))
        return(last_digit(s))



for i in range(13):
    print(str(nth_digit(2**i, 1)) + str(last_digit(2**i))) 
