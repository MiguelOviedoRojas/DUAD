from data import SavingsAccount

def option_menu():
    savings_account = SavingsAccount()
    while True:
        user_select = user_selection()
        if user_select == 1:
            user_money = is_valid_float()
            savings_account.insert_money(user_money)
        elif user_select == 2:
            subtract_user_money = is_valid_float()
            savings_account.compare_balance(subtract_user_money)
        elif user_select == 3:
            savings_account.print_balance()
        else:
            break


def user_selection():
    go_on = True
    while go_on:
        try:
            user_select = int(input("Select an Option\n1-Add Money                 2-Subtract Money                 3-Print Balance                 4-Exit\n"))
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
            money = float(input("Insert Money: "))
            go_on = False
            return money
        except ValueError as ex:
            go_on = True
            print(f"Insert a Valid Number: {ex}")
