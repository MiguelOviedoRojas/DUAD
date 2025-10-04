

def insert_name():
    user_name = " "

    try:
        user_name = input("Insert your name: ")
        if(user_name.isdigit()):
            raise ValueError("El nombre no puede ser un numero")
        return(user_name)
    except ValueError as ex:
        return(ex)


def insert_age():
    user_age = 0
    try:
        user_age = int(input("Insert your Age: "))
        if(user_age < 1 or user_age > 100):
            raise ValueError("Número no es válido")
        return(user_age)
    except ValueError as ex:
        return(ex)


def main():
    try:
        print(f"Hello {insert_name()}, your age is {insert_age()}")
    except Exception as ex:
        print(f"General Error: {ex}")


main()