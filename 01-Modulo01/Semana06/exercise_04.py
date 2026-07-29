'''
4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”
'''

#word = "eugiM"
def change_name(word):
    new_word = ""
    for character in range(len(word)-1, -1, -1):
        new_word = new_word + word[character]
        
    return (new_word)

print(change_name("Hola Mundo"))
