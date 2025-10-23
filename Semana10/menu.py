from actions import insert_new_student, print_all_students, top_three_best_students, general_average, search_student
from data import take_headers_of_list, search_csv_file

def user_selection(list_of_students):
    go_on = True
    while go_on:
        try:
            user_select = int(input("Select an Option\n1-Add Students                 2-View Student Information      3-Top Best 3 Student\n4-View Average All Studens     5-Export Data                   6-Import Data\n7-Delete User\n"))
            if user_select < 1 or user_select > 7:
                print("Select a Valid Option")
            else:
                go_on = False
                option_menu(user_select,list_of_students)
        except ValueError as ex:
            print(f"You must select a number from the list: {ex}")


def option_menu(user_select,list_of_students):
    if user_select == 1:
        user_select = insert_new_student(list_of_students, user_select)
        if user_select == 2:
            return user_selection(list_of_students)
    elif user_select == 2:
        print_all_students(list_of_students)
        user_selection(list_of_students)
    elif user_select == 3:
        top_three_best_students(list_of_students)
        user_selection(list_of_students)
    elif user_select == 4:
        print(round(general_average(list_of_students), 2))
        user_selection(list_of_students)
    elif user_select == 5:
        take_headers_of_list(list_of_students)
        user_selection(list_of_students)
    elif user_select == 6:
        list_of_students = search_csv_file()
        user_selection(list_of_students)
    elif user_select == 7:
        search_student(list_of_students)
        user_selection(list_of_students)

