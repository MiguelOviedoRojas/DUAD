# First Exercise: Bubble Sort
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


my_list = [1,2,3,5] # O(1)
bubble_sort(my_list) # 0(n^2)
print(my_list) # O(1)

# Response: This algorithm is 0(n^2)

#****************************************************************************************#

#Second Exercise: Print Numbers Times 2

def print_numbers_times_2(numbers_list): #0(1)
	for number in numbers_list: # 0(n)
		print(number * 2) # 0(1)

# Response: This algorithm is 0(n)

#****************************************************************************************#

#Third Exercise: check_if_lists_have_an_equal

def check_if_lists_have_an_equal(list_a, list_b): # 0(1)
	for element_a in list_a: # 0(n)
		for element_b in list_b: # 0(n^2)
			if element_a == element_b: # 0(1)
				return True # 0(1)
				
	return False # 0(1)

# Response: This algorithm is 0(n^2)

#****************************************************************************************#

#Forth Exercise: print_10_or_less_elements

def print_10_or_less_elements(list_to_print): # 0(1)
	list_len = len(list_to_print) # 0(1)
	for index in range(min(list_len, 10)): # 0(1)
		print(list_to_print[index]) # 0(1)


# Response: This algorithm is 0(1)

#****************************************************************************************#

#Fifth Exercise: generate_list_trios

def generate_list_trios(list_a, list_b, list_c): # 0(1)
	result_list = [] # 0(1)
	for element_a in list_a: # 0(n)
		for element_b in list_b: # 0(n^2)
			for element_c in list_c: # 0(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}') # 0(1)
				
	return result_list # 0(1)

# Response: This algorithm is 0(n^3)