'''
Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.
'''

def select_operation():
    go_on = True
    while(go_on):
        try:
            user_select = int(input(" 1-Add        2-Subtract           3-Multiply\n 4-Divide     5-CE                 6-Exit\n"))
            if(user_select < 1 or user_select > 6):
                print("Select a valid option")
                go_on = True
            else:
                go_on = False
                return(user_select)
        except ValueError as ex:
            print(f"You must select a number from the list: {ex}")

def sum_operation(actual_result):
    try:
        user_number = float(input(f"{actual_result} + "))
        final_result = actual_result + user_number
    except ValueError as ex:
        print(f"You must enter a number: {ex}")
        final_result = 0
        return (final_result)

    return(final_result)


def rest_operation(actual_result):
    try:
        user_number = float(input(f"{actual_result} - "))
        final_result = actual_result - user_number
    except ValueError as ex:
        print(f"You must enter a number: {ex}")
        final_result = 0
        return(final_result)
    
    return(final_result)


def multiplication_operation(actual_result):
    try:
        user_number = float(input(f"{actual_result} * "))
        final_result = actual_result * user_number
    except ValueError as ex:
        print(f"You must enter a number: {ex}")
        final_result = 0
        return(final_result)
    return(final_result)


def division_operation(actual_result):
    try:
        user_number = float(input(f"{actual_result} / "))
        final_result = actual_result / user_number
    except ValueError as ex:
        print(f"You must enter a number: {ex}")
        final_result = 0
        return(final_result)
    except ZeroDivisionError as ex:
        print(f"Cannot divide by Zero: {ex}")
        final_result = 0
        return(final_result)
    return(final_result)


def reset_operation():
    final_result = 0
    return(final_result)


def main(): 
    go_on = True  
    actual_result = 0
    while(go_on):
        user_select = select_operation()
        try:
            if(user_select == 1):
                actual_result = sum_operation(actual_result)
                print(actual_result)
            elif(user_select == 2):
                actual_result = rest_operation(actual_result)
                print(actual_result)
            elif(user_select == 3):
                actual_result = multiplication_operation(actual_result)
                print(actual_result)
            elif(user_select == 4):
                actual_result = division_operation(actual_result)
                print(actual_result)
            elif(user_select == 5):
                actual_result = reset_operation()
                print(actual_result)
            else:
                go_on = False
        except Exception as ex:
            print(f"General Error: {ex}")


main()