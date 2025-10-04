
def receive_str_to_user():
    try:
        user_str = str(input("Insert your Comment: ") + " ")
        return(user_str)
    except ValueError as ex:
        return(ex)


def write_in_file(path, str_user):
    file_path = path
    user_str = str_user
    with open(file_path, "a", encoding="utf-8") as arch:
        arch.write(user_str)


def main(path):
    try:
        user_str = receive_str_to_user()
        write_in_file(path, user_str)
    except Exception as ex:
        return(ex)


file_path = "C:\Lyfter\Semana08\extra_exercise_04\write_new_file.txt"
main(file_path)