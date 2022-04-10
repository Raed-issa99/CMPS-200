class Pseudorandom:
    """Creates a pseudorandom"""

    def __init__(self,a,c,m,x):
        """initialize the values of a c m x"""
        self.a=a
        self.c=c
        self.m=m
        self.x=x

    def next(self):
        """gives us the next term of this sequence"""
        number =((self.a*self.x)+self.c)%(self.m)
        self.x = number
        return number

pseudo= Pseudorandom(17,7,31,12)
for i in range(10):
    r = pseudo.next()
    print(r, end = '  ')
