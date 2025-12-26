'''
Cree un programa que muestre el valor más pequeño de una lista sin usar `min()`.**
- Use una variable para comparar uno a uno
'''

my_list = [94, 44, 47, 131, 51, 53, 45, 54, 45, 104, 74, 21, 38]
low_number = my_list[0]

for index in range(0, len(my_list)):
    if(low_number <= my_list[index]):
        low_number = low_number
    else:
        low_number = my_list[index]

print(f"El numero menor es: {low_number}")
