def area(a, b):
    '''
    Вычисляет площадь прямоугольника.

        Параметры:
            a (float): длина одной стороны прямоугольника
            b (float): длина другой стороны прямоугольника

        Возвращаемое значение:
            float: площадь прямоугольника

        Пример:
            area(4, 5)
            20
    '''
    if a < 0 or b < 0:
        raise ValueError("Side length must be non-negative")
    return a * b


def perimeter(a, b):
    '''
    Вычисляет периметр прямоугольника.

        Параметры:
            a (float): длина одной стороны прямоугольника
            b (float): длина другой стороны прямоугольника

        Возвращаемое значение:
            float: периметр прямоугольника

        Пример:
            perimeter(4, 5)
            18
    '''
    if a < 0 or b < 0:
        raise ValueError("Side length must be non-negative")
    return 2 * (a + b)


print("Manual testing for rectangle")
print("Calculated that for a = 4, b = 5 => Area = 20")
print(area(4, 5))
print("Calculated that for a = 4, b = 5 => Perimeter = 18")
print(perimeter(4, 5))