class Rectangle():
    def __init__(self):
        pass
    
    def get_area(self, width, height):
        self.width = width
        self.height = height
        rectangle_area = self.width * self.height
        try:
            if rectangle_area < 0:
                return f"{rectangle_area}, Exist a Negative Value, Please Insert Positives Values"
            return rectangle_area
        except ValueError as ex:
            return ex
    

    def get_perimeter(self, width, height):
        self.width = width
        self.height = height
        rectangle_perimeter = 2 * (self.width + self.height)
        try:
            if self.width < 0 or self.height < 0:
                return f"{rectangle_perimeter}, Exist a Negative Value, Please Insert Positives Values"
            return rectangle_perimeter
        except ValueError as ex:
            return ex



