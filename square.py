import unittest

def area(a):
    '''
    Вычисляет площадь квадрата.

        Параметры:
            a (float): длина стороны квадрата

        Возвращаемое значение:
            float: площадь квадрата

        Пример:
            area(5)
            25
    '''
    if a < 0:
        raise ValueError("Длина стороны должна быть неотрицательной")
    return a * a


def perimeter(a):
    '''
    Вычисляет периметр квадрата.

        Параметры:
            a (float): длина стороны квадрата

        Возвращаемое значение:
            float: периметр квадрата

        Пример:
            perimeter(5)
            20
    '''
    if a < 0:
        raise ValueError("Длина стороны должна быть неотрицательной")
    return 4 * a


print("Ручное тестирование для квадрата")
print("Посчитал, что при a = 5 => S = 25")
print(area(5))
print("Посчитал, что при a = 5 => P = 20")
print(perimeter(5))


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