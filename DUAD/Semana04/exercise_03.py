#3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
    #1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

secret_number = random.randint(1,10)
bool_result = False

while(bool_result != True):
    user_number = int(input("Enter a number than 1 to 10: "))
    if(secret_number == user_number):
        print(f"Congratulations, the Secret number is: {secret_number}")
        bool_result = True
    else:
        print("Intentelo de nuevo")
        bool_result = False
        secret_number = random.randint(1,10)
        