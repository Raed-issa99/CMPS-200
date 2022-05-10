import sys
class Square:
    def __init__(self,filename):
        f = open(filename, 'r')
        self.twoD = [[ int(j) for j in i.split()] for i in f]

    def row_sum(self,row):
        return sum(self.twoD[row])

    def column_sum(self,column):
        return sum(i[column] for i in self.twoD)

    def diagonalright(self):
        return sum(i[j] for i,j in zip(self.twoD,range(len(self.twoD))))

    def diagonalleft(self):
        return sum(i[-(j+1)] for i,j in zip(self.twoD,range(len(self.twoD))))

    def is_magic_square(self):
        check = self.diagonalleft()
        for i in range(len(self.twoD)):
            if self.column_sum(i) != check:
                return False
            if self.row_sum(i) != check:
                return False
        if self.diagonalright != check:
            return False
        return True

f = sys.argv[1]
sq = Square(f)

if sq.is_magic_square:
    print("the %d by %d input is a magic square; its sum is %d" %(len(sq.twoD),len(sq.twoD),(sq.diagonalleft())))
else:
    print("The input given is not a magic square")
