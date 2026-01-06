#user_list = [1,25,"hh", 2, "Casa", "23", 8.0, 9,"Dog"]

def sum_values(user_list):
    sum = 0
    for index in range(len(user_list)):
        try:
            position = float(user_list[index])
            print(f"{position} Correct Add")
            sum = sum + position
        except ValueError as ex:
            print(f"Invalid Element: {ex}")
            sum = sum
    print(f"Total Amount: {sum}")

def main():
    try:
        user_list = [1,25,"hh", 2, "Casa", "23", 8.0, 9,"Dog"]
        sum_values(user_list)
    except Exception as ex:
        return(ex)


main()