from exerc_5 import count_words

def test_count_words_basic_case():
    #Arrange
    input_data = "HellO"
    #Act
    result = count_words(input_data)
    #Assert
    assert result == "HellO -> There's a 2 upper cases and 3 lower cases"


def test_count_words_with_spaces():
    #Arrange
    input_data = "Hello World"
    #Act
    result = count_words(input_data)
    #Assert
    assert result == "Hello World -> There's a 2 upper cases and 9 lower cases"


def test_count_upper_words():
    #Arrange
    input_data = "HELLO"
    #Act
    result = count_words(input_data)
    #Assert
    assert result == "HELLO -> There's a 5 upper cases and 0 lower cases"