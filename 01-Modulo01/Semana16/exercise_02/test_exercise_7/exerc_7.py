def list_of_prime_numbers(user_list):
    list_of_numbers = user_list
    final_list= []
    for number in range(len(list_of_numbers)):
        if(list_of_numbers[number] > 1):
            number_rice = list_of_numbers[number]**0.5
            counter = 2
            is_prime = True
            while(counter <= number_rice):
                if(list_of_numbers[number] % counter == 0):
                    is_prime = False
                    break
                counter += 1
            if(is_prime == True):
                final_list.append(list_of_numbers[number])
    return(final_list)


#print(f"List of Prime Numbers: {list_of_prime_numbers([1,2,3,4,5,6,7,8,9,10,11,12,13])}")
