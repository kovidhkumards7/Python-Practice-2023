'''
SUPER() - func used to give access to the methods of parent class. Returns a tempravory obj of a parent class when used
'''

class Rect():
    def __init__(self, len, wid):
        self.length = len
        self.width = wid

class Square(Rect):
    def __init__(self, len, wid):
        super().__init__(len,wid)

    def area(self):
        print("Area is: "+str(self.width*self.length))
class Cube(Rect):
    def __init__(self, len, wid, hei):
        self.height = hei
        super().__init__(len, wid)

    def vol(self):
        print("Volume is: " + str(self.width * self.length*self.height))


sq = Square(3,3)
cub = Cube(3,3,3)

sq.area()
cub.vol()