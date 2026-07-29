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


def search_values_in_list(data_list):
    action_counter = 0
    familiar_counter = 0
    sport_counter = 0
    rpg_counter = 0
    try:
        for index in range(len(data_list)):
            if(data_list[index]['genre'] == 'Action'):
                action_counter += 1
            elif(data_list[index]['genre'] == 'Familiar'):
                familiar_counter += 1
            elif(data_list[index]['genre'] == 'Sport'):
                sport_counter += 1
            else:
                rpg_counter += 1
        print(f"Genres Founded \nAction: {action_counter}\nFamiliar: {familiar_counter}\nSports: {sport_counter}\nRPG: {rpg_counter}")
    except ValueError as ex:
        return(ex)


def main(path):
    try:
        file_to_list = convert_csv_to_list(path)
        search_values_in_list(file_to_list)
    except Exception as ex:
        return(ex)


video_game_list = "video_game.csv"
main(video_game_list)
