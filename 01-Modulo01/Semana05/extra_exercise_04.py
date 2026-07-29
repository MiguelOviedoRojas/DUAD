'''
Cree un programa que reciba una lista de números y calcule el promedio de los valores,
luego cree una nueva lista con solo los valores mayores al promedio
'''

my_list = [110, 24, 3, 54, 80]
total = 0
average = 0
counter = 0
new_list = []

for index in range(0, len(my_list)):
    total = total + my_list[index]
    counter += 1

average = total / counter

for index_new in range(0, len(my_list)):
    if(my_list[index_new] > average):
        new_list.append(my_list[index_new])

print(f"The average is: {average}")
print(f"The new list is: {new_list}")

