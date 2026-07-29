from rectangle_class import Rectangle


def insert_user_data():
    go_width = True
    while go_width:
        try:
            rectangle_width = float(input("Insert Width: "))
            go_width = False
        except ValueError as ex:
            go_width = True
            print(f"Incorrect Value, Please Insert a Valid Number: {ex}")

    go_height = True
    while go_height:
        try:
            rectangle_height = float(input("Insert Height: "))
            go_height = False
        except ValueError as ex:
            go_height = True
            print(f"Incorrect Value, Please Insert a Valid Number: {ex}")
        
    rectangle = Rectangle()
    print(f"Rectangle Area is: {rectangle.get_area(rectangle_width, rectangle_height)}")
    print(f"Rectangle Perimeter is: {rectangle.get_perimeter(rectangle_width, rectangle_height)}")
    
    