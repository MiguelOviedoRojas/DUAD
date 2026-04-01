from exerc_4 import change_name


def test_change_name_basic_case():
    #Arrange
    input_data = "Hola"
    #Act
    result = change_name(input_data)
    #Assert
    assert result == "aloH"


def test_change_name_with_spaces():
    #Arrange
    input_data = "Hola Mundo"
    #Act
    result = change_name(input_data)
    #Assert
    assert result == "odnuM aloH"


def test_change_name_empty_string():
    #Arrange
    input_data = ""
    #Act
    result = change_name(input_data)
    #Assert
    assert result == ""