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
    file_path = 'C:/Lyfter/DUAD/Semana10/students.csv'
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
    file_path = 'C:/Lyfter/DUAD/Semana10/students.csv'

    if not os.path.isfile(file_path):
        print(f"File doesn't exist in this Path: {file_path}")
    else:
        return convert_csv_file_to_list(file_path)


def convert_csv_file_to_list(file_path):
    list_of_students = []
    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                for key, value in row.items():
                    if key != "name" and key != "section":
                        row[key] = float(value)
            list_of_students.append(row)        
            return list_of_students
    except FileNotFoundError as ex:
        print(ex)




