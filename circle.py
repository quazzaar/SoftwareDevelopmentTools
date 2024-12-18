import math


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
        raise ValueError("Radius must be non-negative")
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
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * r


print("Manual testing for circle")
print("Calculated that for r = 5 => Area = 78.53982")
print(area(5))
print("Calculated that for r = 5 => Perimeter = 31.41593")
print(perimeter(5))