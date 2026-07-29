'''
Funciones


def print_hello_world():
    print("Hello World")
    print("Mi primera función")

print_hello_world()

def calculate_salary():
    worked_hours = int(input("Ingrese sus horas trabajadas: "))
    hour_rate = int(input("Ingrese su tarifa por hora: "))
        
    salary = worked_hours * hour_rate
        
    print(f'Su salario sera de {salary}')

calculate_salary()


def function_1():
	print('Ejecutando 1')


def function_2():
	print('Ejecutando 2')


def function_3():
	print('Ejecutando 3')


def main():
	function_1()
	function_2()
	function_3()

main()


def print_parameters(parameter_1, parameter_2, parameter_3):
	print(f'This is parameter 1: {parameter_1}')
	print(f'This is parameter 2: {parameter_2}')
	print(f'This is parameter 3: {parameter_3}')

var_parameter_1 = 50
var_parameter_2 = "Hello"
var_parameter_3 = True

print_parameters(var_parameter_1, var_parameter_2, var_parameter_3)


def sum_three_numbers(number1, number2, number3):
	return number1 + number2 + number3


result = sum_three_numbers(600, 700, 850)
print(result)


def get_max_of_two_numbers(number1, number2):
    if number1 > number2:
        return number1

    return number2


print(get_max_of_two_numbers(3, 7))

result = get_max_of_two_numbers(4,15)
print(result)
'''
