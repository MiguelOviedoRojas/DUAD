'''
Cree una función que reciba un string y retorne cuántas vocales contiene
'''

def count_vocals(str_user):
    user_string = str_user.lower()
    count_vocals = 0

    for character in range(len(user_string)):
        if(user_string[character] == "a"):
            count_vocals += 1
        elif(user_string[character] == "e"):
            count_vocals += 1
        elif(user_string[character] == "i"):
            count_vocals += 1
        elif(user_string[character] == "o"):
            count_vocals += 1
        elif(user_string[character] == "u"):
            count_vocals += 1
    return(count_vocals)

def main():
    string_user = str(input("Insert your String: "))
    return(count_vocals(string_user))

print(main())