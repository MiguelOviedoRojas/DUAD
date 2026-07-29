#3. Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
    #1. *Ejemplos*:
        #1. 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
        #2. 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
        #3. 1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres

counter = 1
women_average = 0
men_average = 0

print("You should put 1 for Women and 2 for Men")
while(counter <= 6):
    print(f"Insert the sex for person {counter}")
    sex = int(input("Select the sex: "))

    if(sex == 1):
        women_average = women_average + 1
        counter = counter + 1
    else:
        men_average = men_average + 1
        counter = counter + 1

women_average = (women_average / 6) * 100
men_average = (men_average / 6) * 100
print(f"The Women Average is: {women_average} %")
print(f"The Men Average is: {men_average} %")