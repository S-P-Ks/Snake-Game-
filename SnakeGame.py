import pygame
import random

pygame.init()

s_width = 1200
s_height = 600

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Game Specific Variables
exit_game = False
game_over = False
init_velocity = 5
velocity_x = 0
velocity_y = 0
snake_x = 45
snake_y = 45
food_x = random.randint(20, s_width/2)
food_y = random.randint(20, s_height/2)
snake_size = 10
fps = 30
score = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x, y])


def plot_snake(win, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(win, color, [x, y, snake_size, snake_size])


def gameloop():

    exit_game = False

    game_over = False
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    snake_x = 45
    snake_y = 45
    food_x = random.randint(20, s_width/2)
    food_y = random.randint(20, s_height/2)
    snake_size = 10
    fps = 30
    score = 0

    with open("hiscore.txt", "r") as f:
        hiscore = int(f.read())

    snake_list = []
    snake_len = 1

    while not exit_game:

        if game_over == True:
            win.fill(white)
            text_screen("Game Over ", red, 100, 300)

            if score > hiscore:
                with open("hiscore.txt", "w") as f:
                    f.write(str(hiscore))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                        snake_x = snake_x + 10

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                        snake_x = snake_x - 10

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                        snake_y = snake_y - 10

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        snake_y = snake_y + 10
                        
                    if event.key == pygame.K_q:
                        score += 5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 1
                print("Score : ", score)
                food_x = random.randint(20, s_width/2)
                food_y = random.randint(20, s_height/2)
                snake_len += 1
                print("HiScore: " + str(hiscore))

            win.fill(white)
            text_screen("Score : " + str(score * 10), blue, 5, 5)
            pygame.draw.rect(
                win, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                if score > hiscore:
                    hiscore = score

            if snake_x < 0 or snake_x > s_width or snake_y < 0 or snake_y > s_height:
                game_over = True
                if score > hiscore:
                    hiscore = score

            plot_snake(win, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


gameloop()
