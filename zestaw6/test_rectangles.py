import unittest
from rectangles import Rectangle  

class TestRectangle(unittest.TestCase):

    def test_str(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        rect3 = Rectangle(2, 3, 4, 5)
        self.assertTrue(rect1 == rect2)
        self.assertFalse(rect1 == rect3)

    def test_center(self):
        rect = Rectangle(1, 2, 3, 4)
        center = rect.center()
        self.assertEqual(str(center), "(2.0, 3.0)")   

    def test_area(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.area(), 4)  

    def test_move(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.move(1, 1)  
        self.assertEqual(str(rect), "[(2, 3), (4, 5)]") 

if __name__ == "__main__":
    unittest.main()
