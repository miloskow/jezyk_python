import math

class Point:
    
    def __init__(self, x, y):  
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"  

    def __repr__(self):
        return f"Point({self.x}, {self.y})"  

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y 

    def __ne__(self, other):
        return not self == other  

    def __add__(self, other):
        if not isinstance(other, Point):
            print("Dodawanie wymaga dwóch punktów.")
            return
        return Point(self.x + other.x, self.y + other.y) 

    def __sub__(self, other):
        if not isinstance(other, Point):
            print("Odejmowanie wymaga dwóch punktów.")
            return
        return Point(self.x - other.x, self.y - other.y) 

    def __mul__(self, other):
        if not isinstance(other, Point):
            print("Iloczyn skalarny wymaga dwóch punktów.")
            return
        return self.x * other.x + self.y * other.y 

    def cross(self, other):
        if not isinstance(other, Point):
            print("Iloczyn wektorowy wymaga dwóch punktów.")
            return
        return self.x * other.y - self.y * other.x 

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y)) 
