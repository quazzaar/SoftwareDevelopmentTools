import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25)  # Стандартный случай
        self.assertEqual(area(0), 0)  # Сторона равна 0

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)  # Стандартный случай
        self.assertEqual(perimeter(0), 0)  # Сторона равна 0

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            perimeter(-5)