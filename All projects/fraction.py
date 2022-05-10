class Fraction:
    """Creates a fraction"""
    def __init__(self, num , denom  = 1 ):
        if denom  == 0:
            print("denominator can't be 0, the denominator will be initialized at 1")
            denom  = 1
        self.numerator = num
        self.denominator = denom

    def __mul__(self,other):
        """Returns a fraction which is the multiplication of 2 fractions"""
        return (Fraction(self.numerator*other.numerator,self.denominator*other.denominator))

    def common_denom(self,other):
        """Creates 2 fractions that are the old fractions but with common denominators"""
        return(Fraction(self.numerator * other.denominator,self.denominator * other.denominator),Fraction(other.numerator * self.denominator,self.denominator * other.denominator))

    def __add__(self,other):
        """returns the addition of 2 fractions"""
        f1,f2 = self.common_denom(other)
        return(Fraction(f1.numerator + f2.numerator, f1.denominator))

    def __eq__(self,other):
        """Returns a boolean expressing if 2 fractions are equal"""
        f1,f2 = self.common_denom(other)
        return (f1.numerator == f2.numerator)

    def __lt__(self,other):
        """Returns a boolean expressing if a fraction is less than another fraction"""
        f1,f2 = self.common_denom(other)
        return f1.numerator < f2.numerator

    def __str__(self):
        return (str(self.numerator) + '/' + str(self.denominator))

    def simplification(self):
        x,y = self.numerator,self.denominator
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        return(Fraction(self.numerator/x,self.denominator/y))

f1 = Fraction(1,2)
f2 = Fraction(2,1)
print(f1*f2) #Should return 2/2
print(f1+f2) #Should return 5/2
print(f1==f2)#should return False
print(f1 == Fraction(2,4))#Should return True
print(f1<f2) #Should return True
print(f2<f1)#Should return False
print(Fraction(4,7).simplification())#Should return 4/7
print(Fraction(4,8).simplification())#Should return 1/2
