#1. Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (`primero` y `segundo`) y los ordene de menor a mayor en dichas variables.
    #1. Ejemplos:
        #1. A: 56, B: 32 → A: 32, B: 56
        #2. A: 24, B: 76 → A: 24, B: 76
        #3. A: 45, B: 12 → A: 12, B: 45


higher_number = 0
lower_number = 0

first_number = int(input("Insert the first number: "))
second_number = int(input("Insert the second number: "))
if(first_number < second_number):
    lower_number = first_number
    higher_number = second_number
    print(f"Higher Number is: {higher_number}")
    print(f"Lower Number is: {lower_number}")
elif(first_number > second_number):
    lower_number = second_number
    higher_number = first_number
    print(f"Higher Number is: {higher_number}")
    print(f"Lower Number is: {lower_number}")
else:
    print("Are Equals")
