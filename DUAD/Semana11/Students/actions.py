from data import take_headers_of_list

class Student():
    def __init__(self, name, section, spanish_grade, english_grade, social_grade, science_grade, student_average):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade
        self.student_average = student_average

    
    def print_info(self):
        print(f"Name: {self.name}\n"
                    f" Section: {self.section}\n"
                    f" Spanish Grade: {self.spanish_grade}\n"
                    f" English: {self.english_grade}\n"
                    f" Social: {self.social_grade}\n"
                    f" Science: {self.science_grade}\n"
                    f" Average: {self.student_average}\n"
        )

    
    def convert_object_list_in_dictionary_list(self):
        dictionary = {}
        dictionary["Name"] = self.name
        dictionary["Section"] = self.section
        dictionary["Spanish Grade"] = self.spanish_grade
        dictionary["English Grade"] = self.english_grade
        dictionary["Social Grade"] = self.social_grade
        dictionary["Science Grade"] = self.science_grade
        dictionary["Average"] = self.student_average
        return dictionary


    def print_top_three(self):
        print(f"Name: {self.name}\n"
                    f" Section: {self.section}\n"
                    f" Average: {self.student_average}\n"
        )


    def search_student(self,student_name,student_section):
        if self.name.upper() == student_name.upper() and self.section.upper() == student_section.upper():
            print(f"Student {self.name}, Exist in {self.section}")
            return 0


def convert_object_to_list(list_of_students):
    dictionary_list_of_students = []
    if not list_of_students:
        print("Empty List")
        return list_of_students
    for student in list_of_students:
            dictionary_student = student.convert_object_list_in_dictionary_list()
            dictionary_list_of_students.append(dictionary_student)
    take_headers_of_list(dictionary_list_of_students)
    

def search_students_failed(list_of_students):
    if not list_of_students:
        print("List Empty")
        return list_of_students
    else:
        list_of_students_failed = []
        for student in list_of_students:
            dictionary = {}
            if student.spanish_grade < 70:
                dictionary["spanish"] = student.spanish_grade
            if student.english_grade < 70:
                dictionary["english"] = student.english_grade
            if student.social_grade < 70:
                dictionary["social"] = student.social_grade
            if student.science_grade < 70:
                dictionary["science"] = student.science_grade
            if dictionary:
                dictionary["name"] = student.name
                list_of_students_failed.append(dictionary)
        return print_failed_student(list_of_students_failed)


def create_new_student(list_of_students):
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
        student_object = Student(student_name,student_section,spanish_grade,english_grade,social_grade,science_grade,student_average)
        list_of_students.append(student_object)
        go_on = user_add_another_student(0)
        if go_on == 2:
            break
    return list_of_students


def print_failed_student(list_of_students_failed):
    print("*****Students Failed Grades*****")
    for student in list_of_students_failed:
        for key,value in student.items():
            print(f"{key.title()}: {student[key]}")
        print("\n")


def general_average(list_of_student_objects):
    actual_average = 0
    counter = 0
    try:
        for student in list_of_student_objects:
            actual_average += student.student_average
            counter += 1
        general_average = actual_average / counter
        return general_average
    except ZeroDivisionError as ex:
        print(f"Cannot Divide by Zero: {ex}")
        return 0


def top_three_best_students(list_of_student_object):
    first = None
    second = None
    third = None
    if not list_of_student_object:
        print("Empty List")
    else:
        for student in list_of_student_object:
            if first == None:
                first = student
            elif student.student_average > first.student_average:
                third = second
                second = first
                first = student
            elif second == None:
                second == student
            elif student.student_average > second.student_average:
                third = second
                second = student
            elif third == None:
                third = student
            elif student.student_average > third.student_average:
                third = student
        best_students = [first, second, third]
        print_top_three_students_objects(best_students)


def print_top_three_students_objects(students_list):
        if not students_list:
            print("Empty List")
            return students_list
        for student in students_list:
                student.print_top_three()


def student_exist(list_of_students,student_name,student_section):
    flag = False
    if not list_of_students:
        print("Empty List, continue Please")
        return 1
    else:
        for student in list_of_students:
            if student.search_student(student_name,student_section) == 0:
                return 0
        if not flag:
            print(f"Student Doesn't Exist, continue Please")
            return 1


def print_all_students_objects(students_list):
        if not students_list:
            print("Empty List")
            return students_list
        for student in students_list:
                student.print_info()


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


def user_add_another_student(user_selection):
    while user_selection < 1 or user_selection > 2:
        try:
            user_selection = int(input("Do you want Insert a Student, Select 1 for YES or 2 for NO: "))
        except ValueError as ex:
            user_selection == 0
            print(f"Select a Valid Option {ex}")
    return user_selection


def search_student(list_of_students):
    if not list_of_students:
        print("Empty List")
        return list_of_students
    else:
        student_name = is_valid_name()
        student_section = is_valid_section()
        for student in list_of_students:
            if student_name.upper() == student.name.upper() and student_section.upper() == student.section.upper():
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






'''def add_student_of_dictionary(student_name,student_section,spanish_grade,english_grade,social_grade,science_grade,student_average):
    dictionary_student = {}
    dictionary_student["name"] = student_name
    dictionary_student["section"] = student_section
    dictionary_student["spanish"] = spanish_grade
    dictionary_student["english"] = english_grade
    dictionary_student["social"] = social_grade
    dictionary_student["science"] = science_grade
    dictionary_student["average"] = student_average
    return dictionary_student'''


