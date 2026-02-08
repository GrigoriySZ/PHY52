# Создайте класс прямоугольник с полями ширина и высота
# Реализуйте конструктор
# Реализуйте метод подсчёта площади
# Реализуйте метод вычисления периметра

# Создаем класс прямоугольник
class Rectangular:
    # Реализуем конструктор класса
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    # Реализуем метод подсчета площади прямоугольника
    def area(self):
        return self.__width * self.__height

    # Реализуем метод подсчета периметра прямоугольника
    def perimeter(self):
        return self.__width * 2 + self.__height * 2

rec1 = Rectangular(2, 3)
print(rec1.area())
print(rec1.perimeter())