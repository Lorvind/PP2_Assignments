import pygame, clock

def scale_image(image, factor):
    new_width = int(32 * scale_factor)
    new_height = int(32 * scale_factor)
    return pygame.transform.scale(image, (new_width, new_height))


def draw_image(image, position: tuple[int, int], rotation: int =0):
    width, height = image.get_size()

    x_offset = -width/2
    y_offset = -height/2

    rotated_image = pygame.transform.rotate(image, rotation)

    rect = rotated_image.get_rect(center=(position[0], position[1]))

    screen.blit(rotated_image, rect)


pygame.init()
screen_width = 1080
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))

CLOCK_IMAGE = pygame.image.load("images/Clock.png")
MINUTE_HAND_IMAGE = pygame.image.load("images/Minute_hand.png")
SECONG_HAND_IMAGE = pygame.image.load("images/Second_hand.png")

scale_factor = 16

CLOCK_IMAGE = scale_image(CLOCK_IMAGE, scale_factor)
MINUTE_HAND_IMAGE = scale_image(MINUTE_HAND_IMAGE, scale_factor)
SECONG_HAND_IMAGE = scale_image(SECONG_HAND_IMAGE, scale_factor)

CENTER = (screen_width/2, screen_height/2)

done = False
game_clock = pygame.time.Clock()

clock_object = clock.Clock()

while not done:

    #Event handling to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Calculating hand positions

    minute_hand_angle, second_hand_angle = clock_object.calculate_hand_angles()
    clock_object.move_forward()

    #Drawing staff
    screen.fill((255, 255, 255))

    draw_image(CLOCK_IMAGE, CENTER)
    draw_image(MINUTE_HAND_IMAGE, CENTER, minute_hand_angle)
    draw_image(SECONG_HAND_IMAGE, CENTER, second_hand_angle)

    pygame.display.flip()

    #Set game to update once a second
    game_clock.tick(1)