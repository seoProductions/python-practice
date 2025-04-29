# simple exercise using TKinter's Geometric object library
# demonstrates OOP in python. very read-able!!!!
import math

class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self): return self.side1
    def getSide2(self): return self.side2
    def getSide3(self): return self.side3
    
    def getArea(self):
        return math.sqrt() # i dont know the formula, it wasent given in the description
    
    def getPerimiter(self):
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        return f"side1 ={self.side1} side2 ={self.side2} side3 ={self.side3}"
