import unittest
import square

class SquareTestCase(unittest.TestCase):

    def test_zero_mul(self):
        self.assertEqual(square.area(0), 0)

    def test_one_mul(self):
        self.assertEqual(square.area(20), 400)

    def test_two_mul(self):
        self.assertEqual(square.area(7.5), 56.25)

    def test_three_mul(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_four_mul(self):
        self.assertEqual(square.perimeter(15), 60)

    def test_five_mul(self):
        self.assertEqual(square.perimeter(17.25), 69)