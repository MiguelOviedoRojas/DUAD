'''Uso de get
Uso get cuando no se si existe la key. Si la key no existe el sistema no se cae, solo devuelve NONE'''
print("--------------Uso de Método GET--------------")
course_information = {
    "title": "Introduction to DB's",
    "description": "Here we review the class",
    "length_in_minutes": 600,
}

print(course_information["description"])
print(course_information.get("key_01"))

'''Iteracion'''
print("--------------Iteracion de Diccionarios Sencilla--------------")
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country in europe_capitals_by_country:
    print({country})

print("--------------Iteracion de Diccionarios con ITEMS--------------")
print("--------------me puede devolver KEY o VALUE o ambas: Similar a enumerate--------------")

for country, capital in europe_capitals_by_country.items():
    print(f'{country} : {capital}')

print("--------------Iteracion de Diccionarios con KEYS--------------")
print("--------------Devuelve solo los KEYS--------------")
for country in europe_capitals_by_country.keys():
    print(country)

print("--------------Iteracion de Diccionarios con VALUES--------------")
print("--------------Devuelve solo los VALUES--------------")
for capital in europe_capitals_by_country.values():
    print(capital)

print("--------------Agregar datos a Diccionarios--------------")
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

europe_capitals_by_country["costa rica"] = "san jose"
print(europe_capitals_by_country)

key_to_add = "colombia"
europe_capitals_by_country[key_to_add] = "bogota"
print(europe_capitals_by_country)

for number in range(0,4):
    europe_capitals_by_country[str(number)] = "sidney"
print(europe_capitals_by_country)

print("--------------Eliminar datos a Diccionarios--------------")
print("--------------Se usa pop con su respectivo KEY--------------")

student_information = {
    "first_name": "Harry",
    "last_name": "Potter",
    "age": 17,
}

deleted_item = student_information.pop("last_name")
print(student_information)
print(f"Deleted Item: {deleted_item}")
