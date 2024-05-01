import pygame
import time
import random
from insert import insert_nickname
from create_db import create
from high import high

snake_speed = 10

window_x = 720
window_y = 480

black = pygame.Color(0 ,0 ,0)
white = pygame.Color(255 , 255, 255)
red = pygame.Color(255 , 0 , 0 )
green = pygame.Color(0,255,0)

pygame.init()

pygame.display.set_caption("SNAKE")
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              ]

fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                   random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

direction = "RIGHT"
change_to = direction

score = 0

player_name = ""  # Инициализация переменной player_name
# Создание бд
create()
def draw_text_input(font, size, color):
    input_font = pygame.font.SysFont(font, size)
    input_surface = input_font.render("Enter your name: " + player_name, True, color)
    input_rect = input_surface.get_rect()
    input_rect.midtop = (window_x/2, window_y/2)
    game_window.blit(input_surface, input_rect)

def handle_input(event):
    global player_name
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            player_name = player_name[:-1]
        else:
            player_name += event.unicode

def menu():
    global player_name
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                else:
                    handle_input(event)  # Обрабатываем ввод текста
        game_window.fill(black)
        draw_text_input('times new roman', 20, white)
        pygame.display.update()

    game()  # Запускаем игру после ввода имени

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    global score
    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, white
    )

    max_score_info = high()
    max_score = max_score_info[1] if max_score_info else 0
    max_score_user = max_score_info[0] if max_score_info else "Unknown"

    high_surface = my_font.render(
        f'High score is {max_score} user: {max_score_user}', True, white
    )

    # Запись результата в бд
    insert_nickname(player_name, score)
    high_rect = high_surface.get_rect()
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/4)
    high_rect.midtop = (window_x / 2, window_y / 2)

    game_window.blit(high_surface, high_rect)
    game_window.blit(game_over_surface, game_over_rect)

    pygame.display.flip()

    time.sleep(5)
    pygame.quit()
    quit()

def game():
    global snake_speed, change_to, snake_position, direction, fruit_position, fruit_spawn, score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            handle_input(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                if event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                if event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                if event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"

        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        if change_to == "DOWN" and direction != "UP":
            direction = "DOWN"
        if change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"

        if direction == "UP":
            snake_position[1] -= 10
        if direction == "DOWN":
            snake_position[1] += 10
        if direction == "LEFT":
            snake_position[0] -= 10
        if direction == "RIGHT":
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))

        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            snake_speed += 0.5
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, green, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
        show_score(1, white, 'times new roman', 20)
        pygame.display.update()

        fps.tick(snake_speed)

menu()  # Вызов меню перед основным циклом

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:  # Обработка нажатия клавиши Enter
            if event.key == pygame.K_KP_ENTER:
                game()  # Запуск игры
