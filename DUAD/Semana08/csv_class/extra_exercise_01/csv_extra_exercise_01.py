import csv

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
    return(data)


def print_list(video_game_list):
    for row in video_game_list[1:]:
        if len(row) < 4:
            continue
        print(f"Name: {row[0]}")
        print(f"Genre: {row[1]}")
        print(f"Developer: {row[2]}")
        print(f"Classification: {row[3]}")
        print("-" * 30)


def main(file_path):
    file_list = read_file(file_path)
    print_list(file_list)


video_game_list = "video_game.csv"
main(video_game_list)