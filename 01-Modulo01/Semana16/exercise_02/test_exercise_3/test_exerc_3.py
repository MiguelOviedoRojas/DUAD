from exerc_3 import sum_list


def test_sum_all_numbers_of_list():
    #Arrange
    list_input = [1,2,3]
    #Act
    result = sum_list(list_input)
    #Assert
    assert result == 6


def test_sum_list_with_negative_numbers():
    #Arrange
    list_input = [1,-2,3]
    #Act
    result = sum_list(list_input)
    #Assert
    assert result == 2


def test_sum_list_with_single_element():
    #Arrange
    list_input = [5]
    #Act
    result = sum_list(list_input)
    #Assert
    assert result == 5