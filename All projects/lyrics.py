
def read_lyrics(filename):
    f = open(filename,'r')
    contents = f.read()
    words = contents.split()
    return words

def lyrics_to_frequencies(lyrics):
    d = dict()
    for i in lyrics:
        d[i] = d.get(i,0) + 1
    return d

def most_common_words(freqs):
    highest = 0
    lst = []
    for i in freqs.values():
        if i > highest:
            highest = i
    for j in freqs.keys():
        if freqs[j] == highest:
            lst.append(j)
    return((lst,highest))

def words_often(freqs, min_times):
    lst = []
    done = False
    while not done:
        if most_common_words(freqs)[1] > min_times:
            lst += [((most_common_words(freqs)[0],most_common_words(freqs)[1]))]
            for i in most_common_words(freqs)[0]:
                del freqs[i]
        else:
            done = True
    return lst

dic = lyrics_to_frequencies(read_lyrics('song.txt'))
n = 10
s = words_often(dic,n)
print("The words repeated more than",n,"times, in decreasing order, are:")
for i in s:
    print(i)
print(most_common_words(dic))
