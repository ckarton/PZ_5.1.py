# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Rectangle(Shape):
    pass


class Square(Shape):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_perimeter(self):
        return 4 * self.width


# Создаем объекты классов Прямоугольник и Квадрат
rectangle = Rectangle(4, 6)
square = Square(5)

# Выводим информацию о прямоугольнике
print("Прямоугольник:")
print("Площадь:", rectangle.calculate_area())
print("Периметр:", rectangle.calculate_perimeter())

# Выводим информацию о квадрате
print("\nКвадрат:")
print("Площадь:", square.calculate_area())
print("Периметр:", square.calculate_perimeter())
