'''
7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista).
    Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
'''

def list_of_prime_numbers(user_list):
    list_of_numbers = user_list
    final_list= []
    for number in range(len(list_of_numbers)):
        if(list_of_numbers[number] > 1):
            number_rice = list_of_numbers[number]**0.5
            counter = 2
            is_prime = True
            while(counter <= number_rice):
                if(list_of_numbers[number] % counter == 0):
                    is_prime = False
                    break
                counter += 1
            if(is_prime == True):
                final_list.append(list_of_numbers[number])
    return(final_list)


print(f"List of Prime Numbers: {list_of_prime_numbers([1,2,3,4,5,6,7,8,9,10,11,12,13])}")
