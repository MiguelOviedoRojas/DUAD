
def convert_to_int(user_list):
    try:
        for index in range(len(user_list)):
            position = user_list[index]
            if(position.isdigit()):
                num = int(user_list[index])
                print(f"'{position}' has been converted to: {num}")
            else:
                print(f"Could not be converted: '{position}'")
    except ValueError as ex:
        return(ex)

    
def main():
    try:
        user_list = ["4","Hola","5.2", "10"]
        convert_to_int(user_list)
    except Exception as ex:
        print(ex)


main()