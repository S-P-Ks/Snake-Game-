import pygame

pygame.init()
fps = 30

s_width = 800
s_height = 600

screen = pygame.display.set_mode((s_width, s_height))
icon = pygame.image.load("target.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

img = pygame.image.load("s.png")
x = 350
y = 500

player_x_change = 5

a_x = 0
a_y = 0
a_x_change = 5
a_y_change = 10
a_img = pygame.image.load("alien.png")


def player():
    screen.blit(img, (x, y))


def alien():
    screen.blit(a_img, (a_x, a_y))


screen.fill((0, 0, 0))
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change = 5

            if event.key == pygame.K_LEFT:
                player_x_change = -5

    x += player_x_change

    a_x += a_x_change
    if a_x < 4:
        a_y += a_y_change
        a_x_change = 5
        a_x += a_x_change
    if a_x > s_width - 64:
        a_y += a_y_change
        a_x_change = -5
        a_x += a_x_change

    if x > s_width-64:
        x = 734
    if x < 4:
        x = 0

    alien()
    player()
    pygame.display.update()
    clock.tick(fps)
