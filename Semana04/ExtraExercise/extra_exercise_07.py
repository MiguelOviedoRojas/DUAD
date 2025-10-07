#3. Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “*Correcto*”. Sino, mostrar “*incorrecto*”.
    #1. *Ejemplos*:
        #1. 23, 30, 768 → Correcto (hay un 30)
        #2. 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
        #3. 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)


first_number = int(input("Insert the first number: "))
second_number = int(input("Insert the second number: "))
third_number = int(input("Insert the third number: "))

if(first_number == 30):
    print("Correct")
elif(second_number == 30):
    print("Correct")
elif(third_number == 30):
    print("Correct")
else:
    total_sum = first_number + second_number + third_number
    if(total_sum == 30):
        print("Correct")
    else:
        print("Incorrect")