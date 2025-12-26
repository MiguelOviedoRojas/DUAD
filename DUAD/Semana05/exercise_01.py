'''
Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
'''

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

index_list = 0

while (index_list < len(second_list)):
    index_first = index_list
    index_second = index_list
    print(f"{first_list[index_first]} {second_list[index_second]}")
    index_list += 1
