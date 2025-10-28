
def insert_new_student(list_of_students):
    while True:
        student_name = is_valid_name()
        student_section = is_valid_section()
        status_of_student = student_exist(list_of_students,student_name, student_section)
        if status_of_student == 0:
            break
        spanish_grade = insert_new_grade("Spanish")
        english_grade = insert_new_grade("English")
        social_grade = insert_new_grade("Social")
        science_grade = insert_new_grade("Science")
        student_average = calculate_average_of_student(spanish_grade,english_grade,social_grade,science_grade)
        dictionary_students = add_student_of_dictionary(student_name,student_section,spanish_grade,english_grade,social_grade,science_grade,student_average)
        list_of_students.append(dictionary_students)
        go_on = user_add_another_student(0)
        if go_on == 2:
            break
    return list_of_students


def is_valid_name():
    go_on = True
    while go_on:
        student_name = str(input("Insert Student Name: "))
        try:
            if not student_name:
                print("Name Empty")
            else:  
                for index in range(len(student_name)):
                    if student_name[index].isalpha() or student_name[index] == " ":
                        go_on = False
                    else:
                        print(f"Insert a Valid Name Please")
                        go_on = True
        except ValueError as ex:
            return ex
    return student_name


def is_valid_section():
    go_on = True
    while go_on:
        student_section = str(input("Insert Student Section: "))
        try:
            if not student_section:
                print("Section Empty")
            else:
                for index in range(len(student_section)):
                    if index == 0 or index == 1:
                        if student_section[index].isdigit():
                            continue
                        else:
                            print("Section Invalid")
                            go_on = True
                    elif index == 2:
                        if student_section[index].upper() == "A" or student_section[index].upper() == "B" or student_section[index].upper() == "C":
                            go_on = False
                        else:
                            print("Section Invalid")
                            go_on = True
            return student_section
        except ValueError as ex:
            return ex


def student_exist(list_of_students,student_name,student_section):
    flag = False
    if not list_of_students:
        print("Empty List, continue Please")
        return 1
    else:
        for student in list_of_students:
            if student["name"].upper() == student_name.upper() and student["section"].upper() == student_section.upper():
                print(f"Student {student_name.title()} Exist in {student_section.upper()}")
                return 0
        if not flag:
            print(f"Student Doesn't Exist, continue Please")
            return 1


def insert_new_grade(grade_name):
    grade = -1
    while grade < 0 or grade > 100:
        try:
            grade = float(input(f"Insert {grade_name} Grade: "))
            if grade < 0 or grade > 100:
                print("Insert a Valid Grade")
        except ValueError as ex:
            grade = -1
            print(f"Insert a Number: {ex}")
    return grade


def calculate_average_of_student(spanish_grade,english_grade,social_grade,science_grade):
    amount = spanish_grade+english_grade+social_grade+science_grade
    average = amount/4
    return average


def add_student_of_dictionary(student_name,student_section,spanish_grade,english_grade,social_grade,science_grade,student_average):
    dictionary_student = {}
    dictionary_student["name"] = student_name
    dictionary_student["section"] = student_section
    dictionary_student["spanish"] = spanish_grade
    dictionary_student["english"] = english_grade
    dictionary_student["social"] = social_grade
    dictionary_student["science"] = science_grade
    dictionary_student["average"] = student_average
    return dictionary_student


def user_add_another_student(user_selection):
    while user_selection < 1 or user_selection > 2:
        try:
            user_selection = int(input("Do you want Insert a Student, Select 1 for YES or 2 for NO: "))
        except ValueError as ex:
            user_selection == 0
            print(f"Select a Valid Option {ex}")
    return user_selection


def print_all_students(list_of_dictionary):
        if not list_of_dictionary:
            print("Empty List")
            return list_of_dictionary
        for user in list_of_dictionary:
                print(f"Name: {user.get('name', 'N/A')}\n"
                    f" Section: {user.get('section', 'N/A')}\n"
                    f" Spanish Grade: {user.get('spanish', 'N/A')}\n"
                    f" English: {user.get('english', 'N/A')}\n"
                    f" Social: {user.get('social', 'N/A')}\n"
                    f" Science: {user.get('science', 'N/A')}\n"
                    f" Average: {user.get('average', 'N/A')}\n"
                )
        return list_of_dictionary


def top_three_best_students(dictionary):
    first = {"name": "", "section": "", "average": 0}
    second = {"name": "", "section": "", "average": 0}
    third = {"name": "", "section": "", "average": 0}

    if not dictionary:
        print("Empty List")
    else:
        for user in dictionary:
            if user.get('average') > first["average"]:
                third = second
                second = first
                first = {"name": user["name"], "section": user["section"], "average": user["average"]}
            elif user.get('average') > second["average"]:
                third = second
                second = {"name": user["name"], "section": user["section"], "average": user["average"]}
            elif user.get('average') > third["average"]:
                third = {"name": user["name"], "section": user["section"], "average": user["average"]}

        best_students = [first, second, third]
        print("********Top Best Students********")
        print_top_three_best_students(best_students)
        return best_students


def print_top_three_best_students(list_of_dictionary):
        for user in list_of_dictionary:
                print(f"Name: {user.get('name', 'N/A')}\n"
                    f" Section: {user.get('section', 'N/A')}\n"
                    f" Average: {user.get('average', 'N/A')}\n"
                )


def general_average(dictionary):
    actual_average = 0
    counter = 0
    try:
        for user in dictionary:
            actual_average += user.get('average')
            counter += 1
        general_average = actual_average / counter
        return general_average
    except ZeroDivisionError as ex:
        print(f"Cannot Divide by Zero: {ex}")
        return 0

        
def search_student(list_of_students):
    if not list_of_students:
        print("Empty List")
        return list_of_students
    else:
        student_name = str(input("Insert name of student: ").upper())
        student_section = str(input("Insert student section: ").upper())
        for student in list_of_students:
            if student_name == student["name"].upper() and student_section == student["section"].upper():
                user_response = user_confirmation()
                if user_response == True:
                    list_of_students.remove(student)
                    return list_of_students
                else:
                    return list_of_students


def user_confirmation():
    user_selection = str(input("Do you want delete user YES or NO: ").upper())
    try:
        if user_selection == "YES":
            print("Selection is YES")
            return(True)
        elif user_selection == "NO":
            print("Selection is NO")
            return(False)
        else:
            print("Select a Valid Option")
    except ValueError as ex:
        return ex


def search_students_failed(list_of_students):
    if not list_of_students:
        print("List Empty")
        return list_of_students
    else:
        list_of_students_failed = []
        for student in list_of_students:
            dictionary = {}
            spanish_grade = 0
            english_grade = 0
            social_grade = 0
            science_grade = 0
            for key,value in student.items():
                if key != 'name' and key != 'section' and key != 'average':
                    if student[key] < 70:
                        dictionary["name"] = student["name"]
                        dictionary["section"] = student["section"]
                        if key == "spanish":
                            spanish_grade = student[key]
                            dictionary["spanish"] = spanish_grade
                        elif key == "english":
                            english_grade = student[key]
                            dictionary["english"] = english_grade
                        elif key == "social":
                            social_grade = student[key]
                            dictionary["social"] = social_grade
                        else:
                            science_grade = student[key]
                            dictionary["science"] = science_grade
            if dictionary:
                list_of_students_failed.append(dictionary)
        return print_failed_student(list_of_students_failed)


def print_failed_student(list_of_students_failed):
    print("*****Students Failed Grades*****")
    for student in list_of_students_failed:
        for key,value in student.items():
            print(f"{key.title()}: {student[key]}")
        print("\n")

