'''
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
'''

def count_words(word):
    sum_upper = 0
    sum_lower = 0
    for character in range(len(word)):
        if(word[character].isupper()):
            sum_upper += 1
        else:
            sum_lower +=1
    
    return(f"{word} -> There's a {sum_upper} upper cases and {sum_lower} lower cases")

print(count_words("HellO WOrLd"))

