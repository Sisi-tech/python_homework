# Task 5: Extending a Class
"""
Within the assignment3 folder, create a file called extend-point-to-vector.py.
Create a class called Point. It represents a point in 2d space, with x and y values passed to the __init__() method. It should include methods for equality, string representation, and Euclidian distance to another point.
Create a class called Vector which is a subclass of Point and uses the same __init__() method. Add a method in the vector class which overrides the string representation so Vectors print differently than Points. Override the + operator so that it implements vector addition, summing the x and y values and returning a new Vector.
Print results which demonstrate all of the classes and methods which have been implemented.
"""
import math 

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y 
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add another vector")
        return Vector(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    x1 = Point(2, 3)
    x2 = Point(1, 1)
    v1 = Vector(1, 2)
    v2 = Vector(3, 5)

    print("x1 = ", x1)
    print("x2 = ", x2)
    print("v1 = ", v1)
    print("v2 = ", v2)
    print("Distance from x1 to x2: ", x1.distance(x2))
    
