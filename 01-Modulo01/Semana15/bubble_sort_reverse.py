
def bubble_sort_reverse(my_list):
    for outer_index in range(0, len(my_list)-1):
        changed_list = False
        for index in range(len(my_list)-1, outer_index-1, -1):
            if index > 0:
                current_index = my_list[index]
                next_index = my_list[index-1]
                if current_index < next_index:
                    print("Intercambiando Datos...")
                    my_list[index-1] = current_index
                    my_list[index] = next_index
                    changed_list = True
                    
        if not changed_list:
            return



#my_list = [20,25,11,5,10,85,2]
my_list = [1,3,5,2,0]

bubble_sort_reverse(my_list)
print(my_list)