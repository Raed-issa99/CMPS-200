import string


def buildDic(k):
    s = string.ascii_lowercase
    a = string.ascii_uppercase
    d = {}
    for i,j in zip(range(len(s)),range(len(a))):
        d[s[i]] = s[(i-k)%26]
        d[a[j]] = a[(j-k)%26]
    return d

def decrypt(dictionary, message):
    decrypted = ''
    for char in message:
        if char in dictionary.keys():
            decrypted += dictionary[char]
        else:
            decrypted += char
    return decrypted

def endlesslist():
    hell = []
    for i in range(26):
        hell += [buildDic(i)]
    return hell


def folder2words(filename):
    f = open(filename,'r').read()
    f = f.split()
    return f

def decryptAny(message,dicts,EngWords):
    MaxAngalizi = (0,0)
    for marwa in range(len(dicts)):
        check = decrypt(dicts[marwa],message).split()
        for word in check:
            Angalizi = 0
            if word in EngWords:
                Angalizi += 1
        if Angalizi > MaxAngalizi[0]:
            MaxAngalizi = (Angalizi,marwa)
    return(MaxAngalizi[1])
"""message = open('cipher-poem.txt')
dicts = endlesslist()
EngWords = folder2words('words.txt')
k = decryptAny(message,dicts,EngWords)
print(decrypt(dicts[k],message))
"""
