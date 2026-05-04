
def valid_input_as_a_string(type_of_movement, input_data):
    flag = True
    for index in range(len(input_data)):
        if not input_data[index].isalpha():
            print(f"Insert a Valid {type_of_movement} Please")
            flag = False
            break
    return flag


def valid_if_category_exist_in_category_list(category, category_list):
    flag = True    
    for index in range(len(category_list)):
        if category_list[index].name.upper() == category.upper():
            flag = False
            break
    return flag


'''def valid_input_insert_as_a_string(type_of_movement, input_str):
    go_on = True
    while go_on:
        user_input = input(f"Insert {input_str}: ").upper()
        result_of_string = valid_input_as_a_string(type_of_movement, user_input)
        if result_of_string:
            go_on = False
            return user_input'''


'''def valid_amount_as_positive_float():
    while True:
        user_amount = input("Insert Amount: ")
        try:
            amount = float(user_amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be mayor than 0")
        except ValueError as ex:
            print(f"Insert a valid numeric amount: {ex}")'''


'''def valid_category_exist(category_list):
    type_of_movement = "EXPENSIVE"
    go_on = True
    while go_on:
        user_category = input("Insert Category: ")
        result_of_string = valid_input_as_a_string(type_of_movement, user_category)
        if result_of_string:
            search_result = search_category_in_category_list(user_category, category_list)
            if search_result != "":
                go_on = False
                return search_result'''


'''def search_category_in_category_list(category, category_list): 
    for index in range(len(category_list)):
        if category_list[index].name.upper() == category.upper():
            return category_list[index].name.upper()    '''

