import unittest
from rectangle import area, perimeter


print("Ручное тестирование для прямоугольника")
print("Посчитал, что при a = 4, b = 5 => S = 20")
print(area(4, 5))
print("Посчитал, что при a = 4, b = 5 => P = 18")
print(perimeter(4, 5))


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4, 5), 20)  # Стандартный случай
        self.assertEqual(area(0, 5), 0)  # Сторона равна 0
        self.assertEqual(area(4, 0), 0)  # Другая сторона равна 0
        self.assertEqual(area(0, 0), 0)  # Обе стороны равны 0

    def test_perimeter(self):
        self.assertEqual(perimeter(4, 5), 18)  # Стандартный случай
        self.assertEqual(perimeter(0, 5), 10)  # Сторона равна 0
        self.assertEqual(perimeter(4, 0), 8)   # Другая сторона равна 0
        self.assertEqual(perimeter(0, 0), 0)   # Обе стороны равны 0

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            area(-4, 5)
        with self.assertRaises(ValueError):
            area(4, -5)
        with self.assertRaises(ValueError):
            perimeter(-4, 5)
        with self.assertRaises(ValueError):
            perimeter(4, -5)