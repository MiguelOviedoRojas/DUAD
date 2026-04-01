from exerc_7 import list_of_prime_numbers

def test_primes_small_list():
    #Arrange
    input_list = [1,2,3,4,5]
    #Act
    expected = [2,3,5]
    #Assert
    assert list_of_prime_numbers(input_list) == expected

def test_primes_with_non_primes():
    #Arrange
    input_list = [10,11,12,13,14,15]
    #Act
    expected = [11,13]
    #Assert
    assert list_of_prime_numbers(input_list) == expected


def test_primes_all_primes():
    #Arrange
    input_list = [2,3,5,7,13]
    #Act
    expected = [2,3,5,7,13]
    #Assert
    assert list_of_prime_numbers(input_list) == expected

