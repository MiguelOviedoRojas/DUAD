'''
Cree un programa que le pida al usuario ingresar 5 palabras.
Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
'''

user_list = []


for number in range(5):
    counter_word = 0
    user_word = str(input("Insert a new word: "))

    for word in user_word:
        counter_word += 1
        
    if(counter_word > 4):
        user_list.append(user_word)

print(f"This is your List: {user_list}")
