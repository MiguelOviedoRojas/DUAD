#Cree un programa que le pida tres números al usuario y muestre el mayor.

number_one = int(input("Enter a first number: "))
number_two = int(input("Enter a second number: "))
number_three = int(input("Enter a third number: "))

list_of_numbers = []
list_of_numbers.append(number_one)
list_of_numbers.append(number_two)
list_of_numbers.append(number_three)

mayor_number = 0
for number in list_of_numbers:
    if(number > mayor_number):
        mayor_number = number
    else:
        mayor_number = mayor_number

print(f"El numero mayor es: {mayor_number}")