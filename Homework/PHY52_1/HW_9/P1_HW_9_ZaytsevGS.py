# Написать класс точка на плоскости с двумя координатами.
# Написать класс отрезок, который будет содержать две точки.
# Реализовать для классов конструкторы и свойства.
# Реализовать для отрезка метод, который вернёт длину отрезка.

class Point:
    """Базовый класс точки"""
    def __init__(self, x: int | float, y: int | float):
        self.__x = x
        self.__y = y

    # Определяем вывод строки для точки
    def __str__(self):
        return f'({self.__x}, {self.__y})'

    @property
    def x(self):
        """Возвращает координату Х"""
        return self.__x

    @property
    def y(self):
        """Возвращает координату Y"""
        return self.__y

class Line2D:
    """Базовый класс двумерного отрезка. Строится на основе двух точек Point"""
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end

    # Определяем вывод строки для отрезка
    def __str__(self):
        return (f'({self.__start.x}, {self.__start.y}), '
                f'({self.__end.x}, {self.__end.y})')

    # Определяем длину отрезка
    def __len__(self):
        """Возвращает длину отрезка с округлением до целого числа"""
        return round(self.length())

    @property
    def start(self):
        """Возвращает координаты начала отрезка"""
        return self.__start.x, self.__start.y

    @property
    def end(self):
        """Возвращает координаты конца отрезка"""
        return self.__end.x, self.__end.y

    def length(self):
        """Возвращает длину отрезка"""
        return ((self.__end.x - self.__start.x) ** 2 +
                (self.__end.y - self.__start.y) ** 2) ** 0.5


# Задаем точки
p1 = Point(0, 3)
print(p1)
p2 = Point(3, -6)
print(p2)
line = Line2D(p1, p2)
print(line)
print(line.length())
print(len(line))
