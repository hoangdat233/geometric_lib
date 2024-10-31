import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(circle.area(0), 0)

    def test_one_mul(self):
        self.assertEqual(circle.area(10), 314.1592653589793)

    def test_two_mul(self):
        self.assertEqual(circle.area(67.636), 14371.619275936122)

    def test_three_mul(self):
        self.assertEqual(circle.perimeter(0) , 0)

    def test_four_mul(self):
        self.assertEqual(circle.perimeter(10), 62.83185307179586)

    def test_five_mul(self):
        self.assertEqual(circle.perimeter(67.636), 424.96952143639845)