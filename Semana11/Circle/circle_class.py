
class Circle:
    def __init__(self, radius):
        self.radius = radius


    def get_area(self):
        area = 3.14 * (self.radius**2)
        return area


radius = float(input("Insert the Radius of Circle: "))
my_circle = Circle(radius)
print(f"Area of Circle is: {my_circle.get_area()}")