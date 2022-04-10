class Element:
    def __init__(self,name,atomicnb,symbol,atomicweight):
        self.__name = name
        self.__atomicnb = atomicnb
        self.__symbol = symbol
        self.__atomicweight = atomicweight
    def __str__(self):
        return(str(self.__name) + ' ' + self.__atomicnb + ' ' + self.__symbol + ' ' + self.__atomicweight)
    def get_name(self):
        return self.__name
    def get_atomicnb(self):
        return self.__atomicnb
    def get_symbol(self):
        return self.__symbol
    def get_atomicweight(self):
        return self.__atomicweight
    def __repr__(self):
        return('< name:' + str(self.__name) + ' atomic number:' + self.__atomicnb + ' symbol' + self.__symbol + ' atomic weight:' + self.__atomicweight)

class PeriodicTable():
    def __init__(self,filename):
        Periodt = dict()
        f = open(filename,'r')
        skip = False
        for line in f:
            if skip == False:
                skip = True
                continue
            info = line.split(',')
            name,atomicnb,symbol,atomicweight = info[0], info[1], info[2], info[3]
            Periodt[symbol] = Element(name,atomicnb,symbol,atomicweight)
        self.table = Periodt

    def weight(self,molecule):
        """Returns the weight of a molecule"""
        total = 0
        molecules = molecule.split(' ')
        for elem in molecules:
            element = ''
            number = ''
            for char in elem:
                if char.isalpha():
                    element += char
                if char.isdigit():
                    number += char
            if number == '':
                number = 1
            atomicelement = self.table[element]
            weight = atomicelement.get_atomicweight()
            r = float(weight)
            total += r * int(number)
        return total


s = PeriodicTable('elements.txt')
print(s.table)
print(s.weight('H2 O'))
print(s.weight('H2 S O4'))
