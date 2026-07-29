'''
Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
'''

def size_of_word(list_of_user, number_of_user):
    user_list = list_of_user
    user_num = number_of_user
    new_list = []

    for index in range(len(user_list)):
        counter = len(user_list[index])
        if(counter > user_num):
            new_list.append(user_list[index])

    return(new_list)


def main():
    list_the_user = ["Hola", "Juanita", "Camion"]
    number_user = int(input("Insert a number: "))
    return(size_of_word(list_the_user, number_user))

print(main())