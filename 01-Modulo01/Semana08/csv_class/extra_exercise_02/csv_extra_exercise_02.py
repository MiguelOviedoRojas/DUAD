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
    try:
        for index in range(len(data_list)):
            if(data_list[index]['classification'] == user_value):
                print(data_list[index]['name'])
    except ValueError as ex:
        return(ex)


def main(path):
    try:
        file_to_list = convert_csv_to_list(path)
        value_user = str(input("Insert a Classificaction: ")).upper()
        search_values_in_list(value_user, file_to_list)
    except Exception as ex:
        return(ex)


video_game_list = "video_game.csv"
main(video_game_list)
