import json

def convert_json_file_to_python(path):
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            python_list = json.load(json_file)
        return(python_list)
    except FileNotFoundError as ex:
        
        return []


def append_new_pokemon_to_list(python_list):
    user_name = str(input("Insert name of Pokemon: "))
    user_type = str(input("Insert type of Pokemon: "))
    user_base_hp = int(input("Insert HP of Pokemon: "))
    user_base_attack = int(input("Insert Attack of Pokemon: "))
    user_base_defense = int(input("Insert Defense of Pokemon: "))
    user_base_sp_attack = int(input("Insert SP Attack of Pokemon: "))
    user_base_sp_defense = int(input("Insert SP Defense of Pokemon: "))
    user_base_speed = int(input("Insert Speed of Pokemon: "))
    try:
        user_pokemon_list = {"name":{"english": user_name},"type":[user_type],"base":{"HP": user_base_hp,"Attack": user_base_attack,"Defense": user_base_defense,"Sp. Attack": user_base_sp_attack,"Sp. Defense": user_base_sp_defense,"Speed": user_base_speed}}
        python_list.append(user_pokemon_list)
        return(python_list)
    except ValueError as ex:
        return(ex)


def convert_python_file_to_json(python_list, path):
    try:
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(python_list, json_file, indent=4)
    except ValueError as ex:
        return(ex)


def main(file_path):
    python_list = convert_json_file_to_python(file_path)
    python_list = append_new_pokemon_to_list(python_list)
    convert_python_file_to_json(python_list, file_path)

main("json_file.json")
    
