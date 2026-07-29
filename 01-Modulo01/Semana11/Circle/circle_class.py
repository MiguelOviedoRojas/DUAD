
class Circle:
    radius = 0.0

    def get_area(self):
        area = 3.14 * (self.radius**2)
        return area


my_circle = Circle()
my_circle.radius = float(input("Insert the Radius of Circle: "))
print(f"Area of Circle is: {my_circle.get_area()}")