def convert_string_to_list(string_of_user):
    user_string = string_of_user
    user_list = []
    new_word = ""

    for character in range(len(user_string)):
        if(user_string[character] == "-"):
            new_word = new_word + user_string[character]
            user_list.append(new_word)
            new_word = ""
        else:
            new_word = new_word + user_string[character]

    return(user_list)


def sort_list_alphabetically(user_list):
    list_of_words = user_list
    changes = False

    while(True):
        changes = False
        for counter in range(len(list_of_words)-1):
            if(list_of_words[counter].upper() > list_of_words[counter+1].upper()):
                first = list_of_words[counter]
                second = list_of_words[counter+1]
                list_of_words[counter] = second
                list_of_words[counter+1] = first
                changes = True
        if not changes:
            break
                
    return(list_of_words)


def final_string(list_of_user):
    user_list = list_of_user
    final_string = ""

    for index, word in enumerate(user_list):
        final_string = final_string + word

    return (final_string)


def main(init_string):
    string_of_user = init_string
    user_list = convert_string_to_list(string_of_user)
    list_of_user= sort_list_alphabetically(user_list)
    output_string = (final_string(list_of_user))
    return output_string

if __name__ == "main":
    user_words = input(str("Insert Words with a - in the end: "))
    print(main(user_words))

