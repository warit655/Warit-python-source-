"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    
    def __init__(self, length ,width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return self.__length*self.__width

    def getPermter(self):
        return 2 * (self.__length + self.width)

    def isSquare(self):
        if self.__length == self.width:
            return True
        else:
            return False
    
x =Rectangle(10,5)
print("area of x =+ {x.getArea()}")
print("Perimeter of x = + {x.getPerimter()}")
if x.isSquare():
    print("x is square")
else:
    print("x is not square")