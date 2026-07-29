'''
Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
'''

def count_characters(sentence, character):
    user_string = sentence.lower()
    user_character = character.lower()
    counter_character = 0

    for character in range(len(user_string)):
        if(user_string[character] == user_character):
            counter_character += 1
    return(counter_character)


def main():
    user_sentence = input(str("Insert your sentence: "))
    character_of_user = input(str("Insert a character: "))
    final_counter = (count_characters(user_sentence,character_of_user))
    print(f"We found the character '{final_counter}' time(s) in the sentence")

main()


