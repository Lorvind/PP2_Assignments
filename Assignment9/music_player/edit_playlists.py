import json

with open('playlists.json', 'r') as f:
    playlists = json.load(f)

current_playlist: list

def show_playlists():
    if len(playlists) == 0:
        print("No playlists available")
    else:
        print("Playlists:")
        print(*playlists, sep=', ')


def show_songs():
    global current_playlist

    if len(current_playlist) == 0:
        print("This playlist is currently empty")
    else:
        for song in current_playlist:
            print(song, end=' ')


def select_playlist(name: str):
    global current_playlist
    current_playlist = playlists[name]
    playlist_menu()


def add_playlist(name: str):
    if name not in playlists:
        playlists[name] = []
        print(f"Playlist {name} succesfully added")
    else:
        print(f"Playlist {name} already exists")

def add_songs():
    global current_playlist

    songs = input("Input songs sepated by ';' symbol: ").split(';')

    current_playlist += songs

    print(f"Successgully added {len(songs)} songs")


def remove_playlist(name: str):
    if name in playlists:
        del playlists[name]
        print(f"Play {name} succesgully deleted")
    else:
        print(f"Playlist {name} doesn't exist")


def remove_songs():
    global current_playlist

    songs = input("Input songs separated by ';' symbol: ")

    removed_songs = songs.split(';')

    for song in current_playlist:
        if song in remove_songs:
            current_playlist.remove(song)

    print(f"Succefully removed {len(removed_songs)} songs")


def playlist_menu():
    while True:
        print("""
        List of commands:
        1 - Add songs
        2 - Remove songs
        3 - Back to playlists menu
        """)

        show_songs()

        command = input("Enter a command: ")

        match command:
            case '1':
                add_songs()
            case '2':
                remove_songs()
            case '3':
                break

def main_menu():
    while True:
        print("""
        List of commands:
        1 - Select a playlist
        2 - Add a playlist
        3 - Remove a playlist
        4 - quit
        5 - commit changes
        """)

        show_playlists()

        command = input("Enter a command: ")

        match command:
            case '1':
                select_playlist(input("Enter playlist name to select: "))
            case '2':
                add_playlist(input("Enter playlist name to add: "))
            case '3':
                remove_playlist(input("Enter playlist name to remove: "))
            case '4':
                break
            case '5':
                with open("playlists.json", 'w') as f:
                    json.dump(playlists, f)

                print("Changes commited successfully")

if __name__ == "__main__":
    main_menu()