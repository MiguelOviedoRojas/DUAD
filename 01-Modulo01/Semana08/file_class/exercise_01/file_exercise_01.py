
def convert_file_in_list(file_path):
    path = file_path 
    song_list = []
    try:
        with open(path) as arch:
            for line in arch.readlines():
                song_list.append(line)
    except ValueError as ex:
        return(ex)
    
    return(song_list)


def order_list(song_list):
    song_of_list = song_list
    new_list = sorted(song_of_list, key = str.lower)
    return(new_list)


def write_file(new_path, new_list):
    path = new_path
    new_song_list = new_list
    try:
        for index in range (len(new_song_list)):
            with open(path, "a", encoding='utf-8') as arch:
                arch.write(new_song_list[index])
    except ValueError as ex:
        return(ex)


def main():
    try:
        song_list = (convert_file_in_list("C:\Lyfter\Semana08\songs_file.txt"))
        new_list = (order_list(song_list))
        write_file("C:\Lyfter\Semana08\songs_new_file.txt", new_list)
    except Exception as ex:
        return(ex)
    

main()


