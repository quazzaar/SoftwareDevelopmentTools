import unittest
from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(5), 78.53981633974483) # стандартный случай
        self.assertEqual(area(0), 0) # радиус равен 0

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(0), 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            perimeter(-5)