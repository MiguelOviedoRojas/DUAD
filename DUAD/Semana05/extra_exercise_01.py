'''
Cree un programa que cuente cuántas veces aparece un número específico en una lista.
Pida al usuario una lista de números y otro número a buscar
'''

user_list = []
counter = 0
search_number = 0

while (counter < 10):
    user_number = int(input("Insert a number: "))
    user_list.append(user_number)
    counter += 1

number_of_user = int(input("Insert a search number: "))

for index_list in range(0,len(user_list)):
    if(user_list[index_list] == number_of_user):
        search_number += 1
    else:
        search_number = search_number

print(f"User List is: {user_list}")
print(f"Number {number_of_user} appears {search_number} time(s) in User List")








