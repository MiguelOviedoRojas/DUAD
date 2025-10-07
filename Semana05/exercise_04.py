'''
Cree un programa que elimine todos los números impares de una lista.
'''

my_list = [0,1,2,3,4,5,6,25,45,69,41,54,88,52,36,11,458,74,10,2174,361,488,1024]
even_list = []


for index in range(0,len(my_list)):
    if (my_list[index] % 2 == 0):
        even_list.append(my_list[index])
        print(my_list[index])

print(f"Even List: {even_list}")
