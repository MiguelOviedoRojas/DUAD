my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

''' Iteracion Directa
1-
for record in my_favorite_records:
    print(f'Record: {record}')

2-
for record in my_favorite_records:
    if record == 'Signify':
        print("Hey es Signify")
    else:
        print(f'Record: {record}')
	'''

'''Iteracion Indirecta usando index

#for index in range(0, len(my_favorite_records)):
 #   record = my_favorite_records[index]
  #  print(f"Record {index}: {record}")

#for index in range(0, len(my_favorite_records)):
 #   print(my_favorite_records[index])

#for index in range(0, len(my_favorite_records)):
 #   my_favorite_records[index] = "Hello"
#print(my_favorite_records)

Usando While
index = 0
while index < len(my_favorite_records):
    record = my_favorite_records[index]
    print(f"Record {index}: {record}")
    index += 1
'''

'''Iteracion Usando Enumerate
for index, record in enumerate(my_favorite_records):
    print(f"Record {index}: {record}")
'''

'''Strings Iterables
my_string = "hola mundo"
#for character in my_string:
    #print(character)

print(my_string[1])
'''

'''Rompiendo Ciclos (break)
colors = [
    "black",
    "yellow",
    "red",
    "blue",
]

for color in colors:
    print(color)
    if color == "yellow":
        break

counter = 0
while (True):
    print(counter)
    if counter > 15:
        break

    counter += 1
'''

'''Adenlantar Ciclos
colors = [
    "black",
    "yellow",
    "red",
    "blue",
]

for color in colors:
    if color == "yellow":
        continue

    print(color)
'''

