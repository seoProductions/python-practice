
#eliseo duque 
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
    
    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return self.width * 2 + self.height * 2
    

rect1 = Rectangle(4,40)
rect2 = Rectangle(3.5, 35.7)

print(f"Rectangle 1's Width: ", rect1.width)
print(f"Rectangle 1's Height: ", rect1.height)
print(f"Rectangle 1's area: ", rect1.getArea())
print(f"Rectangle 1's Perimeter: ", rect1.getPerimeter())


print(f"Rectangle 2's Width: ", rect2.width)
print(f"Rectangle 2's Height: ", rect2.height)
print(f"Rectangle 2's area: ", rect2.getArea())
print(f"Rectangle 2's Perimeter: ", rect2.getPerimeter())

