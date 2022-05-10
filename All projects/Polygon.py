import math


class Polygon:
    '''This class represents a polygon
    
    attributes: sides length
    '''

    def __init__(self, sides, length):
        self.n = sides
        self.s = length

    def perimeter(self):
        return self.n * self.s

    def area(self):
        return ((self.s**2) * self.n) / (4 * math.tan(math.pi / self.n))

class Square(Polygon):
    def __init__(self,length):
        super().__init__(4,length)
        
class Triangle(Polygon):
    def __init__(self,length):
        super().__init__(3,length)

    def area(self):
        return (self.s**2)*math.sqrt(3)/4

s=Square(5)
print(s.perimeter())
print(s.area())

t= Triangle(8)
print(t.perimeter())
print(t.area())