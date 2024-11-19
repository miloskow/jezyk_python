import unittest
from points import Point

class TestPoint(unittest.TestCase):
    def test_str(self):
        p = Point(3, 4)
        self.assertEqual(str(p), "(3, 4)")

    def test_repr(self):
        p = Point(3, 4)
        self.assertEqual(repr(p), "Point(3, 4)")

    def test_eq(self):
        p1 = Point(3, 4)
        p2 = Point(3, 4)
        p3 = Point(5, 6)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_ne(self):
        p1 = Point(3, 4)
        p2 = Point(5, 6)
        self.assertTrue(p1 != p2)

    def test_add(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1 + p2, Point(4, 6))

    def test_sub(self):
        p1 = Point(5, 7)
        p2 = Point(3, 4)
        self.assertEqual(p1 - p2, Point(2, 3))

    def test_mul(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1 * p2, 11)  # 1*3 + 2*4

    def test_cross(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1.cross(p2), -2)  # 1*4 - 2*3

    def test_length(self):
        p = Point(3, 4)
        self.assertEqual(p.length(), 5)  # sqrt(3^2 + 4^2)

    def test_hash(self):
        p1 = Point(3, 4)
        p2 = Point(3, 4)
        self.assertEqual(hash(p1), hash(p2))
        self.assertNotEqual(hash(p1), hash(Point(5, 6)))

if __name__ == "__main__":
    unittest.main()
