'''
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41
'''

def sum_list(the_list):
    total_amount = 0
    for index in range(len(the_list)):
        total_amount = total_amount + the_list[index]
    
    return total_amount


print(f"Total Amount is: {sum_list([4,6,2,29])}")