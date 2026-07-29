from data_classes import Circle, Square, Rectangle

def option_menu():
    while True:
        user_select = user_selection()
        if user_select == 1:
            circle = Circle()
            print("Insert Radio")
            user_radio = is_valid_float()
            print(f"The Circle Perimeter is: {circle.calculate_perimeter(user_radio)}")
            print(f"The Circle Area is: {circle.calculate_area(user_radio)}")
        elif user_select == 2:
            square = Square()
            print("Insert Side")
            user_side = is_valid_float()
            print(f"The Square Perimeter is: {square.calculate_perimeter(user_side)}")
            print(f"The Square Area is: {square.calculate_area(user_side)}")
        elif user_select == 3:
            rectangle = Rectangle()
            print("Insert Length")
            user_length = is_valid_float()
            print("Insert Width")
            user_width = is_valid_float()
            print(f"The Rectangle Perimeter is: {rectangle.calculate_perimeter(user_length, user_width)}")
            print(f"The Rectangle Area is: {rectangle.calculate_area(user_length, user_width)}")
        else:
            break


def user_selection():
    go_on = True
    while go_on:
        try:
            user_select = int(input("Select an Option\n1-Circle                 2-Square                 3-Rectangle                 4-Exit\n"))
            if user_select < 1 or user_select > 4:
                print("Select a Valid Option")
            else:
                go_on = False
                return user_select
        except ValueError as ex:
            print(f"You must select a number from the list: {ex}")


def is_valid_float():
    go_on = True
    while go_on:
        try:
            user_data = float(input("-> "))
            go_on = False
            return user_data
        except ValueError as ex:
            go_on = True
            print(f"Insert a Valid Number: {ex}")
