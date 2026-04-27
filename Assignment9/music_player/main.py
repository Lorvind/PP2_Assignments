import pygame, player, json

pygame.init()
screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
clock = pygame.time.Clock()

with open("playlists.json", 'r') as f:
    playlists = json.load(f)

music_player = player.Music_player(playlists, "music/")

font = pygame.font.SysFont("comicsans", 72)

_cached_text = {}

def create_text(text, size, color):
    global _cached_text, font
    key = '|'.join(map(str, (size, color, text)))
    image = _cached_text.get(key)
    if image == None:
        image = font.render(text, True, color)
        _cached_text[key] = image

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                music_player.play()
            elif event.key == pygame.K_s:
                music_player.stop()
            elif event.key == pygame.K_n:
                music_player.next()
            elif event.key == pygame.K_b:
                music_player.back()