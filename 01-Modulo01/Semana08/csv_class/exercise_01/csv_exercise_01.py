import csv


def receive_video_games_user(def_tuple):
    #video_game_headers = ("name","genre","developer","classification",)
    video_game_list = []
    video_game_dictionary = {}
    counter = 1
    counter_list = 0
    try:
        user_counter = int(input("Insert how much Video Game do you want: "))
    except ValueError as ex:
        print("Please Select a Number")
        return(ex) 
    try:
        while counter <= user_counter:
            user_list = []
            try:
                name_str = str(input("Insert Name of Video Game: "))
                genre_str = str(input("Insert the Genre of Video Game: "))
                developer_Str = str(input("Insert Developer of Video Game: "))
                classification_str = str(input("Insert Classification of Video Game: "))
            except ValueError as ex:
                return(ex)
            user_list.append(name_str)
            user_list.append(genre_str)
            user_list.append(developer_Str)
            user_list.append(classification_str)     
            while counter_list < len(user_list):
                record_one = def_tuple[counter_list]
                record_two = user_list[counter_list]
                video_game_dictionary[record_one] = record_two
                counter_list += 1
            video_game_list.append(video_game_dictionary)
            counter_list = 0
            video_game_dictionary = {}
            counter += 1
        return(video_game_list)
    except ValueError as ex:
        return(ex)


def write_csv_file(file_path, list_of_dict, headers):
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as arch:
            writer = csv.DictWriter(arch, fieldnames=headers)
            writer.writeheader()
            writer.writerows(list_of_dict)
    except ValueError as ex:
        return(ex)


def main(path, def_tuple):
    try:
        video_game_list = receive_video_games_user(def_tuple)
        write_csv_file(path, video_game_list, def_tuple)
    except Exception as ex:
        return(ex)


video_game_headers = ("name","genre","developer","classification",)
main("video_game.csv", video_game_headers)





