from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Współrzędne muszą spełniać warunek: x1 < x2 oraz y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): 
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):       
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other): 
        if isinstance(other, Rectangle):
            return self.pt1 == other.pt1 and self.pt2 == other.pt2
        return False

    def __ne__(self, other):        
        return not self == other

    def center(self): 
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return Point(cx, cy)

    def area(self): 
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)


    def move(self, x, y): 
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)
    
    def intersection(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Oczekiwano obiektu typu Rectangle.")
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        else:
            raise ValueError("Prostokąty nie mają części wspólnej")
        
    def cover(self, other):
        if not isinstance(other,Rectangle):
            raise ValueError("Oczekiwano obiektu typu Rectangle.")
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)
    
    def make4(self):
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return (
            Rectangle(self.pt1.x, self.pt1.y, cx, cy),
            Rectangle(cx, self.pt1.y, self.pt2.x, cy),
            Rectangle(self.pt1.x, cy, cx, self.pt2.y),
            Rectangle(cx, cy, self.pt2.x, self.pt2.y)
        ) 