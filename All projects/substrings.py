def substring(s1, s2, k):
    if s1 in s2[k: k+len(s1)]:
        return True
    else:
        return False

def how_many(string1, string2): #Traverses string2 letter by letter in slices = to len(string1) to check when str2 in str1
    counter = 0
    for i in range(len(string2)):
        if substring(string1, string2, i):
            counter += 1
    return counter

print(how_many('bob','azcbobobegghak1'))
