class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color
    def draw(self):
        print(f'Рисуем фигуру цветом {self.color} и шириной {self.width}')

    def del_line(self):
        print('Линия удалена')
class Line(Figure):
    def draw(self):
        print(f'Рисуем линии цветом {self.color} и шириной {self.width}')

class Rect(Figure):
    def __init__(self, coords, width, color, right):
        super().__init__(coords, width, color)
        self.right = right
    def draw(self):
        print(f'Рисуем прямоугольник цветом {self.color} и шириной {self.width}. Прямоугольник {self.right}')

class Ellips(Figure):
    def draw(self):
        print(f'Рисуем линии цветом {self.color} и шириной {self.width}')


f = Figure([1, 2, 3, 4, 5, 7, 8], 2, 'black')
f.draw()
l = Line([1, 5, 4, 2], 3, 'orange')
l.draw()
e =Ellips([6, 1, 3, 5], 4,'yellow')
e.draw()
e = Rect([5, 4, 3], 103, 'green', 'Правильный')
e.draw()

e.del_line()