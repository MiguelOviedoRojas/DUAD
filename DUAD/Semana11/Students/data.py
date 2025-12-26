from student import Student
import csv
import os


def take_headers_of_list(list_of_students):
    try:
        if not list_of_students:
            print("Empty List, cannot export file")
        else:    
            list_of_headers = list(list_of_students[0].keys())
            write_csv_file(list_of_headers,list_of_students)
    except TypeError as ex:
        return ex


def write_csv_file(list_of_headers, list_of_students):
    file_path = 'C:/Lyfter/DUAD/Semana11/students.csv'
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as arch:
            writer = csv.DictWriter(arch, fieldnames=list_of_headers)
            writer.writeheader()
            writer.writerows(list_of_students)
            print("File Write Successful")
            return list_of_students
    except FileNotFoundError as ex:
        return ex


def search_csv_file():
    file_path = 'C:/Lyfter/DUAD/Semana11/Students/students.csv'
    if not os.path.isfile(file_path):
        print(f"File doesn't exist in this Path: {file_path}")
    else:
        return convert_csv_file_to_list(file_path)


def convert_csv_file_to_list(file_path):
    student_list = []
    list_of_student_objects = []
    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                for key, value in row.items():
                    student_list.append(value)
                student_object = convert_list_in_object(student_list)
                list_of_student_objects.append(student_object)
                student_list = []    
            return list_of_student_objects
    except FileNotFoundError as ex:
        print(ex)


def convert_list_in_object(student_list):
    while len(student_list) < 7:
        if len(student_list) < 2:
            student_list.append("")
        else:
            student_list.append(0.0)
    student_name = str(student_list[0])
    student_section = str(student_list[1])
    spanish_grade = float(student_list[2])
    english_grade = float(student_list[3])
    social_grade = float(student_list[4])
    science_grade = float(student_list[5])
    student_average = float(student_list[6])
    student_object = Student(student_name,student_section,spanish_grade,english_grade,social_grade,science_grade,student_average)
    return student_object