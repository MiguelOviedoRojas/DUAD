from bus_class import Bus, Person


def option_menu():
    go_on = True
    go_passengers = None
    go_bus_name = True
    while go_on:
        while go_passengers is None:
            capacity_of_bus = input("What is the capacity of the Bus: ")
            go_passengers = convert_string_to_integer(capacity_of_bus)
        
        while go_bus_name:
            bus_name = input("What is the name of the Bus: ")
            go_bus_name = valid_name_of_bus(bus_name)
            
        bus = Bus(go_passengers, bus_name)
        while True:
            user_select = user_selection()
            if user_select == 1:
                passenger = Person()
                bus.add_passenger(passenger)
            elif user_select == 2:
                go_passenger_id = None
                while go_passenger_id is None:
                    passenger_id = input("What is the ID of the Passenger: ")
                    go_passenger_id = convert_string_to_integer(passenger_id)
                bus.remove_passenger(go_passenger_id)
            else:
                break


def valid_name_of_bus(bus_name):
    character_list = ['+', '-', '*', '/', '%', '=', '(', ')']
    try:
        name_bus = str(bus_name)
        for character in character_list:
            if character in name_bus:
                print("Error Name, Please Insert a Valid Name")
                return True
        return False
    except ValueError as ex:
        print(f"Insert only letters: {ex}")
        return True


def convert_string_to_integer(capacity_of_bus):
    try:
        num_passengers = int(capacity_of_bus)
        if num_passengers <= 0:
            print("Number Must Be mayor than cero")
            return None
        else:
            return num_passengers
    except ValueError as ex:
        print(f"Please Insert a Valid Number: {ex}")
        return None


def user_selection():
    go_on = True
    while go_on:
        try:
            user_select = int(input("Select an Option\n1-Add Passenger                 2-Delete Passenger\n"))
            if user_select < 1 or user_select > 2:
                print("Select a Valid Option")
            else:
                go_on = False
                return user_select
        except ValueError as ex:
            print(f"You must select a number from the list: {ex}")