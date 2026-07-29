from shape_class import Shape


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radio = 0.0
        self.__pi = 3.14
    
    def calculate_perimeter(self, radio):
        self.radio = radio
        perimeter = 2 * self.__pi * self.radio
        return perimeter
    
    def calculate_area(self, radio):
        self.radio = radio
        area = self.__pi*(self.radio**2)
        return area


class Square(Shape):
    def __init__(self):
        super().__init__()
        self.side = 0.0
    
    def calculate_perimeter(self, side):
        self.side = side
        perimeter = 4 * self.side
        return perimeter
    
    def calculate_area(self, side):
        self.side = side
        area = self.side**2
        return area


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.length = 0.0
        self.width = 0.0
    
    def calculate_perimeter(self, length, width):
        self.length = length
        self.width = width
        perimeter = 2 * (self.length + self.width)
        return perimeter
    
    def calculate_area(self, length, width):
        self.length = length
        self.width = width
        area = self.length * self.width
        return area