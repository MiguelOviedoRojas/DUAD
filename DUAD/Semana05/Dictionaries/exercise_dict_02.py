'''
Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
'''


my_dictionary = {}
list_one = ["first_name", "last_name", "role", "province", "company_name"]
list_two = ["Miguel", "Oviedo", "Software Engenieer", "Alajuela", "Lyfter"]
counter = 0


while (counter < len(list_two)):
    record_one = list_one[counter]
    record_two = list_two[counter]
    my_dictionary[record_one] = record_two
    counter += 1

print(my_dictionary)