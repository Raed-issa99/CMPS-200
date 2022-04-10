import sys
n = int(sys.argv[1])
ls = sys.argv[2:]


vowels = 'aeoui'

def vowel_count(s):
    number = 0
    for i in s:
        if i.lower() in vowels:
            number += 1
    return(number)

def more_than_n_vowels(ls,n):
    words = []
    for i in ls:
        if vowel_count(i) > n:
            words += [i]
    return(words)


print(more_than_n_vowels(ls,n))
