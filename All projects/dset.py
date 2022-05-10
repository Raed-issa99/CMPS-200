class Dset:
    def __init__(self, str1 = ''):
        """Creates a digit set element from a given string"""
        for i in str1:
            if not i.isdigit():
                raise ValueError("Expected digits or spaces only")
        strf = ''
        for char in str1:
            if char not in strf:
                strf += char
        self.set = [int(i) for i in strf]


    def __len__(self):
        """Returns the cardinality of the set"""
        return len(self.set)

    def in_set(self,d):
        """Returns whether a digit d is in the set or not"""
        return(int(d) in self.set)

    def add_element(self,d):
        """Adds an intiger d to the set"""
        if d < 0 or d > 9:
            raise ValueError("Digit must be between 0 and 9")
        if d not in self.set:
            self.set.append(d)

    def __eq__(self,s):
        """Returns whether the two sets have the same elements"""
        if len(self) != len(s):
            return False
        for i in self.set:
            if i not in s.set:
                return False
        return True

    def union(self,s):
        """Returns the set which is the uninion of the 2 sets"""
        u = ''
        for i in self.set:
            u += str(i)
        for char in s.set:
            if str(char) not in u:
                u += str(char)
        return(Dset(u))

    def intersection(self,s1):
        """Returns the set which is the intersection of the 2 sets"""
        u = ''
        for i in s1.set:
            if i in self.set:
                u += str(i)
        return(Dset(u))

    def __str__(self):
        finalstr = '{'
        b = self.set
        for i in range(len(b)):
            finalstr += str(b[i])
            if i == len(b)-1:
                finalstr += '}'
            else:
                finalstr += ' '
        return finalstr
    def __repr__(self):
        finalstr = '{'
        b = self.set
        for i in range(len(b)):
            finalstr += str(b[i])
            if i == len(b)-1:
                finalstr += '}'
            else:
                finalstr += ' '
        return finalstr
def test():
    """Tests all the methods of the class"""
    a = Dset('123456')
    b = Dset('456789')
    c = Dset('143265')
    print(a)
    print("length of set 'a' is:" + str(len(a)))
    print(a.in_set(1))
    print(a == c)
    print(a.union(b))
    print(a.intersection(b))
    a.add_element(7)
    print(a)

if __name__ == '__main__':
    test()
