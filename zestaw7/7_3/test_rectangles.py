import unittest
from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 1, 1)
        rect = Rectangle(1, 1, 3, 3)
        self.assertEqual(str(rect), "[(1, 1), (3, 3)]")

    def test_str_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        rect3 = Rectangle(2, 3, 4, 5)
        self.assertTrue(rect1 == rect2)
        self.assertFalse(rect1 == rect3)

    def test_center(self):
        rect = Rectangle(1, 1, 3, 3)
        center = rect.center()
        self.assertEqual(center, Point(2, 2))

    def test_area(self):
        rect = Rectangle(1, 1, 3, 3)
        self.assertEqual(rect.area(), 4)

    def test_move(self):
        rect = Rectangle(1, 1, 3, 3)
        rect.move(1, 1)
        self.assertEqual(rect, Rectangle(2, 2, 4, 4))

    def test_intersection(self):
        rect1 = Rectangle(1, 1, 4, 4)
        rect2 = Rectangle(2, 2, 5, 5)
        intersection = rect1.intersection(rect2)
        self.assertEqual(intersection, Rectangle(2, 2, 4, 4))

        with self.assertRaises(ValueError):
            rect1.intersection(Rectangle(5, 5, 6, 6))  

    def test_cover(self):
        rect1 = Rectangle(1, 1, 4, 4)
        rect2 = Rectangle(2, 2, 5, 5)
        cover = rect1.cover(rect2)
        self.assertEqual(cover, Rectangle(1, 1, 5, 5))

    def test_make4(self):
        rect = Rectangle(0, 0, 4, 4)
        parts = rect.make4()
        self.assertEqual(parts[0], Rectangle(0, 0, 2, 2))  # Lewy dolny
        self.assertEqual(parts[1], Rectangle(2, 0, 4, 2))  # Prawy dolny
        self.assertEqual(parts[2], Rectangle(0, 2, 2, 4))  # Lewy górny
        self.assertEqual(parts[3], Rectangle(2, 2, 4, 4))  # Prawy górny

if __name__ == "__main__":
    unittest.main()
