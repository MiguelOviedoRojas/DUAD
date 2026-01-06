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
        return(new_str)
    except ValueError as ex:
        return(ex)


def count_words_to_string(str_of_list):
    new_str = str_of_list
    counter = 1
    try:
        for character in range(len(new_str)):
            if(new_str[character] == " " or new_str[character] == "\n"):
                counter += 1
        return(counter)
    except ValueError as ex:
        return(ex)


def main(path):
    file_list = convert_file_to_list(path)
    str_list = convert_list_to_string(file_list)
    return(count_words_to_string(str_list))


user_path = "C:\Lyfter\Semana08\extra_exercise_02\open_file.txt"
print(f"El archivo contiene: {main(user_path)} palabras")
