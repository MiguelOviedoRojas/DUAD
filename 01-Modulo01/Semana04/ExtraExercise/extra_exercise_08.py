#2. Cree un diagrama de flujo que le pida un numero al usuario y muestre “*Fizz*” si es divisible entre 3, “*Buzz*” si es divisible entre 5, y “*FizzBuzz*” si es divisible entre ambos.
    #1. *Ejemplos*:
        #1. 33 → Fizz
        #2. 25 → Buzz
        #3. 30 → FizzBuzz

user_number = int(input("Insert a Number: "))

if(user_number % 3 == 0):
    if(user_number % 5 == 0):
        print("FizzBuzz")
    else:
        print("Fizz")
elif(user_number % 5 == 0):
    print("Buzz")
else:
    print("Number is not divisible by 3 or 5")