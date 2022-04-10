class Segment:
    def __init__(self,left,right = None):
        """Constructs a segment, left coordinate defaulted at 0"""
        if right == None and left > 0:
            right,left = left,right
            left = 0
        if left > right:
            raise ValueError
        self.left = left
        self.right = right

    def __str__(self):
        """allows the print of the coordinates"""
        return ('[%.1f -- %.1f]' %(self.left,self.right))

    def __repr__(self):
        return ('[%.1f -- %.1f]' %(self.left,self.right))

    def get_left(self):
        """Returns the left coordinate"""
        return self.left

    def get_right(self):
        """Returns the right coordinate"""
        return self.right

    def mid_point(self):
        """Returns the midpoint of a segment"""
        return (self.right + self.left)/2
    def contains(self,x):
        """retuns if a coordinate x is in the segment or not"""
        return self.left < x <= self.right

    def overlaps(self,other):
        """Returns if a segment overlaps the other"""
        for i in (other.left,other.right):
            if self.contains(i):
                return True
        return False

    def __lt__(self,other):
        return self.mid_point() < other.mid_point()

s = Segment(6)
print(s)
def Test():
    s1 = Segment(10)
    s2 = Segment(20,30)
    s3 = Segment(5)
    print(s2.overlaps(s1)) #False
    print(s3.overlaps(s1)) #True
    print(s1.contains(3))  #True
    print(s1.mid_point())  #5.0
    print(s1.get_left(),s1.get_right()) #0,10
    print(s1 < s2) #True
    print(s1)
