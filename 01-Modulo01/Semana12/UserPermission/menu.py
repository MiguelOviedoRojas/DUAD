from admin_user import AdminUser
from regular_user import RegularUser


def option_menu():
    while True:
        user_select = user_selection()
        if user_select == 1:
            print("Insert Name")
            admin_name = is_valid_str()
            admin_user = AdminUser(admin_name)
            print("Insert Permission")
            user_permission = is_valid_str()
            result = admin_user.has_permission(user_permission)
            print(result)
        elif user_select == 2:
            print("Insert Name")
            regular_name = is_valid_str()
            regular_user = RegularUser(regular_name)
            print("Insert Permission")
            user_permission = is_valid_str()
            result = regular_user.has_permission(user_permission)
            print(result)
        else:
            print("Exit Program")
            break


def user_selection():
    go_on = True
    while go_on:
        try:
            user_select = int(input("Select an Option\n1-Admin User                 2-Regular User                 3-Exit\n"))
            if user_select < 1 or user_select > 3:
                print("Select a Valid Option")
            else:
                go_on = False
                return user_select
        except ValueError as ex:
            print(f"You must select a number from the list: {ex}")


def is_valid_str():
    while True:
        user_str = input("-> ")
        strip_user = user_str.strip()
        if len(strip_user) < 3:
            print("Error Insert String with 4 or more characters")
        elif not strip_user.isalpha():
            print("Error String has Numbers, Insert Valid String")
        else:
            return strip_user
