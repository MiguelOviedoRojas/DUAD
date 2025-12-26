'''
2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2. Intente accesar a una variable global desde una función y cambiar su valor.
'''


'''
print("Exercise 01")
def inside_function():
    var_inside_function = 5
    print(f"This is the parameter inside of the function: {var_inside_function}")

inside_function()
#print(f"This is the parameter out of the function: {var_inside_function}")
'''

print("Exercise 02")

var_outside_function = 10

def outside_function():
    global var_outside_function
    index = 0
    index += 1
    var_outside_function = var_outside_function + index
    return(var_outside_function)


def main():
    print(f"This is the global variable modified: {outside_function()}")

main()
