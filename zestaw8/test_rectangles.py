import pytest
from rectangles import Rectangle
from points import Point

def test_initialization():
    rect = Rectangle(0, 0, 4, 3)
    assert rect.left == 0
    assert rect.right == 4
    assert rect.bottom == 0
    assert rect.top == 3
    with pytest.raises(ValueError):
        Rectangle(4, 4, 2, 2)

def test_from_points():
    rect = Rectangle.from_points([Point(0, 0), Point(4, 3)])
    assert rect.left == 0
    assert rect.right == 4
    assert rect.bottom == 0
    assert rect.top == 3

def test_properties():
    rect = Rectangle(1, 2, 5, 6)
    assert rect.width == 4
    assert rect.height == 4
    assert rect.topleft == Point(1, 6)
    assert rect.bottomright == Point(5, 2)

def test_center():
    rect = Rectangle(0, 0, 4, 4)
    assert rect.center == Point(2, 2)

def test_area():
    rect = Rectangle(0, 0, 3, 3)
    assert rect.area() == 9

def test_move():
    rect = Rectangle(0, 0, 4, 4)
    rect.move(1, 2)
    assert rect.left == 1
    assert rect.bottom == 2
    assert rect.right == 5
    assert rect.top == 6
