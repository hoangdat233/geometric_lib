import unittest
import triangle

class TriangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        self.assertEqual(triangle.area(7,8), 28)

    def test_one_mul(self):
        self.assertEqual(triangle.area(10, 5), 20)


    def test_two_mul(self):
        self.assertEqual(triangle.area(7.5, 3.5),13.125)


    def test_three_mul(self):
        self.assertEqual(triangle.perimeter(0, 0,0), 3)


    def test_four_mul(self):
        self.assertEqual(triangle.perimeter(10, 4, 8), 23)


    def test_five_mul(self):
        self.assertEqual(triangle.perimeter(34.23, 42.34, 23.43), 100)