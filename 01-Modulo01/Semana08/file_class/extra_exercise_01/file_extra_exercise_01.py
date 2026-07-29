def open_read_file(path):
    file_path = path
    file_list = []
    try:
        with open(file_path) as arch:
            for line in arch.readlines():
                file_list.append(line)
    except ValueError as ex:
        return(ex)
    return(file_list)


def create_string(file_list):
    new_list = file_list
    final_str = ""
    try:
        for index in range(len(new_list)):
            if("\n" in new_list[index]):
                final_str = final_str + " " + new_list[index][:-1]
            else:
                final_str = final_str + " " + new_list[index]
    except ValueError as ex:
        return(ex)
    return(final_str)


def write_file(path, final_str):
    file_path = path
    try:
        with open(file_path, "w", encoding= "utf-8") as arch:
            arch.write(final_str)
    except ValueError as ex:
        return(ex)


def main(read_path, write_path):
    try:
        new_list = (open_read_file(read_path))
        final_str = (create_string(new_list))
        write_file(write_path, final_str)
    except Exception as ex:
        return(ex)


path_one = "C:\Lyfter\Semana08\extra_exercise_01\line_per_line.txt"
path_two = "C:\Lyfter\Semana08\extra_exercise_01\one_line_per_line.txt"

main(path_one, path_two)

