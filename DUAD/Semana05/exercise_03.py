'''
Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
'''

my_list = [1, 6, 1, 7,5,8,1,15,18,200,954,50,147,6,36,4,5,6,90,4,9,2,6,64,55,877,122,470]

print(f"Original List: {my_list}")
first_item = my_list.pop(0)
last_item = my_list.pop(len(my_list)-1)
my_list.append(first_item)
my_list.insert(0, last_item)
print(f"Modified List: {my_list}")
