#Enteros - Integers

my_int = 5
my_other_int = 8
result = my_int + my_other_int
print(result)

#NFloats - Numeros Decimales
my_float =3.14
my_other_float = 8.23
result_float = my_float + my_other_float
print(result_float)

#Strings - Cadenas de Texto
my_string = "Este es un String"
my_multiline_string = """
    Este
    es
    un
    string
    de
    multiples
    lineas
"""
print(my_string)
print('Este también es un String con comillas simples')
print(my_multiline_string)

#incorrect_string = este; no; es; un; my_string;
#print(incorrect_string)

#print(esto tampoco es un string)

#print("esto tampoco porque se uso comillas distintas')


#Concatenacion
other_string_concat = 'Bond'
concatenated_string = 'My name is ' + other_string_concat
print(concatenated_string)

other_string_concat_f = 'Bond'
f_string = f'My name is {other_string_concat_f}'
print(f_string)

other_string_concat_format = 'Bond'
template_string = 'My name is {name}'
formatted_string = template_string.format(name=other_string_concat_format)
print(formatted_string)

#Boolean
my_false_boolean = False
my_true_boolean = True

#Lists
my_first_list = [2,5,7,8]
print(my_first_list[2])

empty_list = []
list_of_integers = [4,7,3,5+4,3]
list_of_strings = ["Hello","I'm","A","String","List"]
list_of_booleans = [True,False,True]

print(list_of_integers[4])
print(list_of_strings[2])
print(list_of_booleans[1])

list_different_types = [1,2,3,"Hello","Name", True, False]
print(list_different_types[3])

#Tuples
my_first_tuple = (2,5,7,8)
print(my_first_tuple[0])

#Dictionaries
my_first_dictionary = {
    "key": 5,
    "other_key": "Hello again",
    "final_key": 98}

print(my_first_dictionary["final_key"])

condo_houses = [
	{
		"number": 93,
		"area_m2": 125,
		"rooms": [
			"living_room",
			"kitchen",
			"main_sleeping_room",
			"second_sleeping_room",
			"bathroom",
		],
	},
	{
		"number": 95,
		"area_m2": 125,
		"rooms": [
			"living_room",
			"kitchen",
			"main_sleeping_room",
			"second_sleeping_room",
			"third_sleeping_room",
			"bathroom",
		],
	},
]

print(condo_houses[1]['rooms'][5])














