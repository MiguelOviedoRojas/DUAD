'''
Variable Inside
'''
'''
def declare_variable():
    variable_inside_function_scope = 8
    print(f'Inside function: {variable_inside_function_scope}')


declare_variable()
#print(f'Out of function: {variable_inside_function_scope}')
'''

'''Varible Global - Outside'''

variable_outside_function_scope = 7


def print_variable():
    print(f'Inside function: {variable_outside_function_scope}')

print(print_variable)
#print(f"Outside Function: {variable_outside_function_scope}")