class Rectangle():
    def __init__(self, rect_width, rect_height):
        self.width = rect_width
        self.height = rect_height
    
    
    def get_area(self):
        rectangle_area = self.width * self.height
        try:
            if self.width < 0 or self.height < 0:
                raise ValueError("Exist a Negative Value, Please Insert Positives Values")
            else:
                return rectangle_area    
        except ValueError as ex:
            return ex
    

    def get_perimeter(self):
        rectangle_perimeter = 2 * (self.width + self.height)
        try:
            if self.width < 0 or self.height < 0:
                raise ValueError("Exist a Negative Value, Please Insert Positives Values")
            else:
                return rectangle_perimeter
        except ValueError as ex:
            return ex



