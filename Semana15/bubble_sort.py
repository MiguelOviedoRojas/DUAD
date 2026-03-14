
def bubble_sort(list):  # 0(1)
    for outer_index in range(0, len(list)-1): # 0(n)
        changed_list = False # 0(1)
        for index in range(0, len(list)-1 - outer_index): # 0(n^2)
            current_index = list[index] # 0(1)
            next_index = list[index + 1] # 0(1)

            if current_index > next_index: # 0(1)
                print("Intercambiando valores...") # 0(1)
                list[index] = next_index # 0(1)
                list[index + 1] = current_index # 0(1)
                changed_list = True # 0(1)
        
        if not changed_list: # 0(1)
            return # 0(1)





#my_list = [20,25,11,5,10,85,2]
my_list = [1,2,3,5] # O(1)
bubble_sort(my_list) # 0(n^2)
print(my_list) # O(1)