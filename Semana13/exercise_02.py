'''def received_numbers(numbers):
    try:
        func_numbers = float(numbers)
        print(func_numbers)
    except ValueError as ex:
        print(ex)
        return ex


user_numbers = input("Insert Numbers: ")
received_numbers(user_numbers)
'''

def numbers_only(func):
    def wrapper(*args):
        for value in args:
            try:
                float(value)
            except ValueError as ex:
                raise ValueError(f"Invalid Data, please only insert numbers: {ex}")
        return func(*args)
    return wrapper


@numbers_only
def insert_numbers(numbers):
    print(f"All is good: {numbers}")


@numbers_only
def receive_parameters(parameter_one,parameter_two):
    print(f"01- {parameter_one}, 02- {parameter_two}")

first_parameter = input("Insert First Parameter: ")
second_parameter = input("Insert Second Parameter: ")
receive_parameters(first_parameter,second_parameter)

#user_numbers = input("Insert Number: ")
#insert_numbers(user_numbers)