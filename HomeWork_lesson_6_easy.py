# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    def __init__(self, a, h, b, c):
        self.a = a
        self.h = h
        self.b = b
        self.c = c
    def square(self):
        return (1 / 2) * (self.a * self.h)

    def height(self):
        return (self.a + self.b + self.c) / 2

    def perimeter(self):
        return (self.a + self.b + self.c)

    def info(self):
        print(f'Наш треугольник: \n '
              f'сторона А {self.a} \n '
              f'сторона B {self.b} \n '
              f'сторона C {self.c} \n '
              f'высота H {self.h} \n')

triangle1 = triangle(10, 12, 10, 10)
triangle1.info()
print('площадь треугольника через основание и высоту \n S = ', triangle1.square())
print('высота треугольника \n P = ', triangle1.height())
print('периметр треугольника \n P = ', triangle1.perimeter())
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Equal_barrel:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def info(self):
        print(f'Наша трапеция: \n '
              f'сторона А {self.a} \n '
              f'сторона B {self.b} \n '
              f'сторона C {self.c} \n '
              f'высота D {self.d} \n')


barrel1 = Equal_barrel(15, 10, 8, 8)
barrel1.info()


