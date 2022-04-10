import sys
import string


k = int(sys.argv[1])
str1 = sys.argv[2]
l_alphabets = string.ascii_lowercase
u_alphabets = string.ascii_uppercase

def cipher(k):
    d = dict()
    for i in range(len(l_alphabets)):
        d[l_alphabets[i]] = l_alphabets[(i+k) % (len(l_alphabets))]
        d[u_alphabets[i]] = u_alphabets[(i+k) % (len(u_alphabets))]
    return d
def caesar(str1, dictionary):
    encrypted = ''
    for c in str1:
        if c in dictionary:
            c = dictionary[c]
        else:
            c = c
        encrypted += c
    return encrypted

diction = cipher(k)


print(caesar(str1, diction))
