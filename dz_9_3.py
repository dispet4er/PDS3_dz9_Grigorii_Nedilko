class Paralelogram:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area

Paralelogram1 = Paralelogram(11, 5)

print(Paralelogram1.get_area())

class Square(Paralelogram):
    def __init__(self, length, width = None):
        Paralelogram.__init__(self, length, width)
        self.length = length
        self.width = self.length

    def get_area(self):
        self.length = self.width
        area = self.length ** 2
        return area

Square1 = Square(22)

print(Square.get_area(Square1))