import random

animals = {'a':['horse'], 'b': ['baboon'], 'c' : ['giraffe']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(d):
    vsum = 0
    for i in d.values():
        vsum += len(i)
    return vsum

def biggest(d):
    biggest = list(d.keys())[0]
    for i in d.keys():
        if len(d[i]) > len(d[biggest]):
            biggest = i
    return(biggest)

def dstats(d):
    return(how_many(d),len(d[biggest(d)]))

print(dstats(animals))
