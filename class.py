import math
def how_many(letter,string):
    count = 0
    for i in range(len(string)):
        if string[i] == letter:9
            count += 1
    return count


def howmany(letter,string):
    count = 0
    for c in string:
        if c == letter:
            count = count + 1 #can be written as count += 1
    return count

a = 'a'
howmany(a,banana)
