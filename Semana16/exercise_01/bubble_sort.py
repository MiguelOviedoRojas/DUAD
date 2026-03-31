
def bubble_sort(number_list):  # 0(1)
    if not isinstance(number_list, list):
        raise TypeError("number_list must be a list")
    for outer_index in range(0, len(number_list)-1): # 0(n)
        changed_list = False # 0(1)
        for index in range(0, len(number_list)-1 - outer_index): # 0(n^2)
            current_index = number_list[index] # 0(1)
            next_index = number_list[index + 1] # 0(1)

            if current_index > next_index: # 0(1)
                number_list[index] = next_index # 0(1)
                number_list[index + 1] = current_index # 0(1)
                changed_list = True # 0(1)
        
        if not changed_list: # 0(1)
            break # 0(1)
    
    return number_list





my_list = [1,2,3,5] # O(1)
bubble_sort(my_list) # 0(n^2)
print(my_list) # O(1)
