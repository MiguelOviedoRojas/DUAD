'''
Cree un programa que use una lista para eliminar keys de un diccionario.
'''
my_dictionary = {
    "name": "Miguel",
    "email": "moviedo@gmail.com",
    "access_level": 5,
    "age": 39,
}

my_list = ["access_level", "age"]
counter = 0
print(my_dictionary)

while (counter < len(my_list)):
    record = my_list[counter]
    print(my_list[counter])
    delete_record = my_dictionary.pop(my_list[counter])
    counter += 1

print(my_dictionary)