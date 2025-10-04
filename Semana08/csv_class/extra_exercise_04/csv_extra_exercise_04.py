import csv

def convert_csv_to_list(file_path):
    data_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)
            return(data_list)
    except FileNotFoundError as ex:
        return(ex)


def search_values_in_list(user_value, data_list):
    user_list = []
    try:
        for index in range(len(data_list)):
            if(data_list[index]['developer'].upper() == user_value.upper()):
                user_list.append(data_list[index])
        return(user_list)
    except ValueError as ex:
        return(ex)
    

def print_list(video_game_list):
    try:
        for index in range(len(video_game_list)):
            print(f"-{video_game_list[index]['name']} (Classification: {video_game_list[index]['classification']}, Genre: {video_game_list[index]['genre']})")
    except ValueError as ex:
        return(ex)


def main(path):
    try:
        file_to_list = convert_csv_to_list(path)
        value_user = str(input("Insert a Developer: "))
        final_list = search_values_in_list(value_user, file_to_list)
        print_list(final_list)
    except Exception as ex:
        return(ex)


video_game_list = "video_game.csv"
main(video_game_list)
