import pygame

class Music_player:
    def __init__(self, playlists: dict[list], path_to_songs: str):
        self.playlists: dict = playlists
        self.current_playlist: list = list(playlists.values())[0]
        self.current_song_id: int = 0
        self.path_to_songs = path_to_songs

        pygame.mixer.music.load(self.path_to_songs + self.current_playlist[0])
        pygame.mixer.music.play()
        pygame.mixer.music.pause()


    def choose_playlist(self, playlist_name: str):
        if self.playlists.get(playlist_name) != None:
            self.current_playlist = self.playlists.get(playlist_name)
        else:
            print(f'No playlist "{playlist_name}" found')

    
    def play(self):
        pygame.mixer.music.unpause()


    def stop(self):
        pygame.mixer.music.pause()


    def next(self):
        if self.current_song_id + 1 == len(self.current_playlist):
            self.current_song_id = 0
        else:
            self.current_song_id += 1
        
        pygame.mixer.music.load(self.path_to_songs + self.current_playlist[self.current_song_id])
        pygame.mixer.music.play()

    def back(self):
        if self.current_song_id == 0:
            self.current_song_id = len(self.current_playlist) - 1
        else:
            self.current_song_id -= 1
        
        pygame.mixer.music.load(self.path_to_songs + self.current_playlist[self.current_song_id])
        pygame.mixer.music.play()