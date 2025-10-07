def convert_file_to_list(file_path):
    path = file_path
    new_list = []
    try:
        with open(path, "r", encoding="utf-8") as arch:
            new_list.extend(arch.readlines())
        return(new_list)
    except ValueError as ex:
        return(ex)


def convert_list_to_string(file_list):
    new_list = file_list
    new_str = ""
    try:
        for index in range(len(new_list)):
            new_str = new_str + new_list[index]
        return(new_str.upper())
    except ValueError as ex:
        return(ex)


def write_upper_file(new_file_path, str_upper):
    second_path = new_file_path
    upper_str = str_upper
    try:
        with open(second_path, "w", encoding="utf-8") as new_arch:
            new_arch.write(upper_str)
    except ValueError as ex:
        return(ex)
    

def main(first_path, second_path):
    try:
        file_list = convert_file_to_list(first_path)
        upper_str = convert_list_to_string(file_list)
        write_upper_file(second_path, upper_str)
        print("Archivo Escrito de Forma Correcta")
    except Exception as ex:
        return(ex)


first_path = "C:\Lyfter\Semana08\extra_exercise_03\diferent_lines.txt"
second_path = "C:\Lyfter\Semana08\extra_exercise_03\diferent_lines_second.txt"
main(first_path, second_path)