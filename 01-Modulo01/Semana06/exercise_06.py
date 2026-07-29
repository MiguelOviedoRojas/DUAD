'''
6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
'''


'''
#ESTA FUNCION COMPARA 2 PALABRAS Y LAS ORDENA ALFABETICAMENTE- PERO SE HIZO LA FUNCION BUBBLE SORT QUE YA ORDENA LA LISTA DE UNA VEZ

def compared_two_words(word_one,word_two):
    word_one.upper()
    word_two.upper()
    counter_one = 0
    counter_two = 0
    found_difference = False
    small_l = ""

    counter_one = len(word_one)
    counter_two = len(word_two)

    if(counter_one <= counter_two):
        small_l = word_one
        mayor_l = word_two
    else:
        small_l = word_two
        mayor_l = word_one

    counter_less = 0
    counter_mayor = 0
    while(counter_less < len(small_l)-1):
        print(f"word One: {small_l[counter_less]}")
        print(f"Word Two: {mayor_l[counter_mayor]}")
        if(small_l[counter_less] < mayor_l[counter_mayor]):
            print(f"{small_l} va de primero, esto debido a la letra: {small_l[counter_less]}, va primero que la letra: {mayor_l[counter_mayor]} de {mayor_l}.")
            found_difference = True
            break
        counter_less += 1
        counter_mayor += 1
    if(found_difference == False):
        print(f"Small Letter va de primero, esto debido a que la palabra: {small_l}, tiene menos letras que Mayor Letter: {mayor_l}.")

    print(f"Small Letter: {small_l}, Mayor Letter: {mayor_l}")
    print(f"Mayor Letter: {mayor_l}, Small Letter: {small_l}")
    return [small_l, mayor_l]


compared_two_words("Mundo-","Hola-")
'''


def convert_string_to_list(string_of_user):
    user_string = string_of_user
    user_list = []
    new_word = ""

    for character in range(len(user_string)):
        if(user_string[character] == "-"):
            new_word = new_word + user_string[character]
            user_list.append(new_word)
            new_word = ""
        else:
            new_word = new_word + user_string[character]

    return(user_list)


def sort_list_alphabetically(user_list):
    list_of_words = user_list
    changes = False

    while(True):
        changes = False
        for counter in range(len(list_of_words)-1):
            if(list_of_words[counter].upper() > list_of_words[counter+1].upper()):
                first = list_of_words[counter]
                second = list_of_words[counter+1]
                list_of_words[counter] = second
                list_of_words[counter+1] = first
                changes = True
        if not changes:
            break
                
    return(list_of_words)


def final_string(list_of_user):
    user_list = list_of_user
    final_string = ""

    for index, word in enumerate(user_list):
        final_string = final_string + word

    return (final_string)


def main(init_string):
    string_of_user = init_string
    user_list = convert_string_to_list(string_of_user)
    list_of_user= sort_list_alphabetically(user_list)
    output_string = (final_string(list_of_user))
    return output_string


user_words = input(str("Insert Words with a - in the end: "))
print(main(user_words))

