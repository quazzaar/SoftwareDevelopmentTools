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
        raise ValueError("Side length must be non-negative")
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
        raise ValueError("Side length must be non-negative")
    return 4 * a


print("Manual testing for square")
print("Calculated that for a = 5 => Area = 25")
print(area(5))
print("Calculated that for a = 5 => Perimeter = 20")
print(perimeter(5))
