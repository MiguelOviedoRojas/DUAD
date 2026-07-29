#4. **Tabla de multiplicar personalizada**
    #- Pida al usuario un número del 1 al 10
    #- Muestre su tabla de multiplicar del 1 al 12

result_list = []
user_number = int(input("Enter a Number 1 to 10: "))
counter = 1

if(user_number >= 1 and user_number <= 10):
    while(counter <= 12):
        result = user_number * counter
        result_list.append(result)
        counter = counter + 1

    index_counter = 1    
    for index_number in result_list:
        print(f"{user_number} * {index_counter} = {index_number}")
        index_counter = index_counter + 1
else:
    print("Invalid Number, Insert a Number in range 1 to 10")