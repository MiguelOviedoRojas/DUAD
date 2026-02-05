def print_parameters(func):
    def wrapper(name, lastname):
        print(f"Name: {name} {lastname}")
        func(name, lastname)
    return wrapper


@print_parameters
def function(name, lastname):
    #print(f"This are the parameters of the function: {parameters}")
    print(f"This the return of the function")
    print(f"{name} {lastname}")
    print("End")


user_name = input("Insert your name: ")
user_last_name = input("Insert your lastname: ")
function(user_name, user_last_name)