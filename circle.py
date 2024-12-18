import math
import unittest

def area(r):
    '''
    Вычисляет площадь круга.

        Параметры:
            r (float): радиус круга

        Возвращаемое значение:
            float: площадь круга

        Пример:
            area(3)
            28.274333882308138
    '''
    if r < 0:
        raise ValueError("Радиус должен быть неотрицательным")
    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет длину окружности.

        Параметры:
            r (float): радиус круга

        Возвращаемое значение:
            float: длина окружности

        Пример:
            perimeter(3)
            18.84955592153876
    '''
    if r < 0:
        raise ValueError("Радиус должен быть неотрицательным")
    return 2 * math.pi * r


print("Ручное тестирование для круга")
print("Посчитал, что при r = 5 => S ~78.53982")
print(area(5))
print("Посчитал, что при r = 5 => S ~31.41593 ")
print(perimeter(5))


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