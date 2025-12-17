from actions import create_new_student, print_all_students_objects, top_three_best_students, general_average, search_student, search_students_failed, convert_object_to_list
from data import take_headers_of_list, search_csv_file


def option_menu():
    student_list = []
    while True:
        user_select = user_selection()
        if user_select == 1:
            create_new_student(student_list)
        elif user_select == 2:
            print_all_students_objects(student_list)
        elif user_select == 3:
            top_three_best_students(student_list)
        elif user_select == 4:
            print(f"General Average of Students is: {round(general_average(student_list), 2)}")
        elif user_select == 5:
            convert_object_to_list(student_list)
        elif user_select == 6:
            student_list = search_csv_file()
        elif user_select == 7:
            search_student(student_list)
        elif user_select == 8:
            search_students_failed(student_list)
        else:
            break


def user_selection():
    go_on = True
    while go_on:
        try:
            user_select = int(input("Select an Option\n1-Add Students                 2-View Student Information      3-Top Best 3 Student\n4-View Average All Students    5-Export Data                   6-Import Data\n7-Delete User                  8-Search Fail Students          9-Exit\n"))
            if user_select < 1 or user_select > 9:
                print("Select a Valid Option")
            else:
                go_on = False
                return user_select
        except ValueError as ex:
            print(f"You must select a number from the list: {ex}")




