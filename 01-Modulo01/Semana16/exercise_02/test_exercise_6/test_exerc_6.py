from exerc_6 import main

def test_main_simple_case():
    # Arrange
    input_string = "mundo-hola-"
    # Act
    result = main(input_string)
    # Assert
    assert result == "hola-mundo-"

def test_main_mixed_case():
    # Arrange
    input_string = "Zebra-apple-Mango-"
    # Act
    result = main(input_string)
    # Assert
    assert result == "apple-Mango-Zebra-"

def test_main_multiple_words():
    # Arrange
    input_string = "banana-apple-cherry-date-"
    # Act
    result = main(input_string)
    # Assert
    assert result == "apple-banana-cherry-date-"