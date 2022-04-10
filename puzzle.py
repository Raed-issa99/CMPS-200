import sys
class Puzzle:
    def __init__(self,filename):
        f = open(filename,'r').read().split('\n')
        twoD = list()
        for line in f:
            lst = list()
            for char in line:
                lst += [char]
            twoD += [lst]
        self.matrix = twoD
        self.row = len(self.matrix[0])
        self.column = len(self.matrix)
    def __str__(self):
        string = ''
        for i in self.matrix:
            for char in i:
                string += char + ' '
            string += '\n'
        return string


    def found_right(self,word,location):
        row,column = location
        found = ''
        for i in range(column,column + min((self.row - 1),len(word))):
            found += self.matrix[row][i]
        return found == word

    def found_down(self,word,location):
        row,column = location
        found = ''
        for i in range(row,row + min(self.column - 1,len(word))):
            found += self.matrix[i][column]
        print(found)
        return found == word


filename = sys.argv[1]
word = sys.argv[2]
wordfound = False
puz2 = Puzzle(filename)
for i in range(puz2.column):
    for j in range(puz2.row):
        if puz2.found_down(word,(i,j)):
            print(word + "found: row" + str(i + 1) + ", column" + str(j + 1) + "going down")
            wordfound = True
            break
        if puz2.found_right(word,(i,j)):
            print(word + "found: row" + str(i + 1) + ", column" + str(j + 1) + "going right")
            wordfound= True
            break
if wordfound == False:
    print(word + "not found")
