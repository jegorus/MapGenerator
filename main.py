import pygame

# for easier access to key coordinates
from pygame.locals import *



# initialize pygame
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
gameOn = True
clock = pygame.time.Clock()


# instantiate objects
x = 200
y = 200
vel = 15
image = [pygame.image.load('img/example_character/not_moving.png'),
         pygame.image.load('img/example_character/move_left.png'),
         pygame.image.load('img/example_character/move_right.png'),
         pygame.image.load('img/example_character/move_down.png'),
         pygame.image.load('img/example_character/move_up.png')]
image_size = (40, 40)
for i in range(len(image)):
    image[i] = pygame.transform.scale(image[i], image_size)
direction = 0



fps = 30

while gameOn:

    clock.tick(fps)


    for event in pygame.event.get():

        if event.type == QUIT:
            gameOn = False

    direction = 0

    key_pressed_is = pygame.key.get_pressed()
    if key_pressed_is[K_LEFT]:
        if x - vel > 0:
            x -= vel
        else:
            x = 0
        direction = 1
    if key_pressed_is[K_RIGHT]:
        if x + vel < screen_size[0] - image_size[0] - 1:
            x += vel
        else:
           x = screen_size[0] - image_size[0] - 1
        direction = 2
    if key_pressed_is[K_DOWN]:
        if y + vel < screen_size[1] - image_size[1] - 1:
            y += vel
        else:
            y = screen_size[1] - image_size[1] - 1
        direction = 3
    if key_pressed_is[K_UP]:
        if y - vel > 0:
            y -= vel
        else:
            y = 0
        direction = 4


    # Draw
    screen.fill((0,0,0))
    screen.blit(image[direction], (x, y))

    pygame.display.flip()

pygame.quit()

