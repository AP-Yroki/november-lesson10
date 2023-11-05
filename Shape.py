class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f'Это геометрическая фигура, цвет - {self.color}.')

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init(color)
        self.radius = radius

    def area(self):
        return round(3.1415 * self.radius**2, 1)

    def describe(self):
        print(f'Это {self.color} окружность. Радиус - {self.radius} см, цвет - {self.color}.')

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def describe(self):
        print(f'Это {self.color} прямоугольник. Длина - {self.length} см, ширина - {self.width} см, цвет - {self.color}.')

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init(color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def describe(self):
        print(f'Это {self.color} треугольник с основанием {self.base} см и высотой {self.height} см, цвет - {self.color}.')

circle = Circle("красный", 5)
rectangle = Rectangle("синий", 3, 4)
triangle = Triangle("фиолетовый", 6, 8)

circle.describe()
rectangle.describe()
triangle.describe()

print(f"Площадь треугольника {triangle.area()} см², окружности {circle.area()} см², прямоугольника {rectangle.area()} см².")
