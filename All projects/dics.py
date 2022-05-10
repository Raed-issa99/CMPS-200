def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


print(histogram('brontosaurus'))

def histogramm(s):
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        elif c not in d:
            d[c] = 1
    return d

print(histogramm('brontosaurus'))
