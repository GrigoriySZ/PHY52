# Создайте класс прямоугольник с полями ширина и высота
# Реализуйте конструктор
# Реализуйте метод подсчёта площади
# Реализуйте метод вычисления периметра

# Создаем класс прямоугольник
class Rectangular:
    # Реализуем конструктор класса
    def __init__(self, width: int | float, height: int | float):
        self.__width = self.__validate_size(width)
        self.__height = self.__validate_size(height)

    def __validate_size(self, size):
        if not isinstance(size, (int, float)):
            raise TypeError
        return size

    # Геттер поля width
    @property
    def width(self):
        return self.__width
    
    # Сеттер поля width с проверкой типа данных
    @width.setter
    def width(self, new_width):
        if not isinstance(new_width, (int, float)):
            raise TypeError
        self.__width = new_width
    
    # Геттер поля height
    @property
    def height(self):
        return self.__height
    
    # Сеттер поля height с проверкой типа данных
    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, (int, float)):
            return TypeError
        self.__height = new_height

    # Реализуем метод подсчета площади прямоугольника
    def area(self):
        return self.width * self.height

    # Реализуем метод подсчета периметра прямоугольника
    def perimeter(self):
        return self.width * 2 + self.height * 2


# Объявляем экземпляр класса
rec1 = Rectangular(2, 3.3)
print(rec1.area())
print(rec1.perimeter())

# Объявляем экземпляр класса с ошибкой
rec2 = Rectangular(0.2, 'f')
print(rec2.area())
print(rec2.perimeter())

