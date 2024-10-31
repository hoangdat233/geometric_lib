import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        self.assertEqual(rectangle.area(0,13), 0)

    def test_one_mul(self):
        self.assertEqual(rectangle.area(5,13), 120)

    def test_two_mul(self):
        self.assertEqual(rectangle.area(67.5, 3.5), 236.25)


    def test_three_mul(self):
        self.assertEqual(rectangle.perimeter(0,0), 0)


    def test_four_mul(self):
        self.assertEqual(rectangle.perimeter(10, 44), 128)

    def test_five_mul(self):
        self.assertEqual(rectangle.perimeter(67.636, 42.364), 220)