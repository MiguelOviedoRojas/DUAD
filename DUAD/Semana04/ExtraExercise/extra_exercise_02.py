#2. Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “*Mayor*”. Si es exactamente igual, muestre “*Igual*”.
    #1. *Ejemplos*:
        #1. 1040 → Mayor
        #2. 140 → 460
        #3. 600 → Igual
        #4. 599 → 1


rest_time = 0

second_time = float(input("Insert the time in seconds: "))
minute_time = 600

if(second_time < minute_time):
    rest_time = minute_time - second_time
    print(f"The rest time is: {rest_time} seconds")
elif(second_time == minute_time):
    print("Equal")
else:
    print("Mayor")



