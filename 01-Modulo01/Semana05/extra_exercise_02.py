'''
Cree un programa que verifique si todos los elementos de una lista son positivos
'''

my_list = [3, 6, -5, -2, 4, 59, -45, 14, -8, 74, 40]
negative_number = 0


for index in range(0,len(my_list)):
    if (my_list[index] < 0):
        negative_number += 1
    else:
        negative_number = negative_number

print(my_list)
print(f"The amount of negative numbers is: {negative_number}")
