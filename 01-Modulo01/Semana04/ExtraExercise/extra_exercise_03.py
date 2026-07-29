#3. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
    #1. 5 → 15 (1 + 2 + 3 + 4 + 5)
        #1. 3 → 6 (1 + 2 + 3)
    #2. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)


user_number = int(input("Enter a number: "))
counter = 1
total_amount = 0

while(counter <= user_number):
    total_amount = total_amount + counter
    counter = counter + 1

print(f"The result is: {total_amount}")