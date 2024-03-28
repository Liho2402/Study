import pygame
from math import *
from datetime import *

pygame.init()

screen = pygame.display.set_mode((1024, 1024))
clock = pygame.time.Clock()

body = pygame.image.load("images/mainclock.png")
minute = pygame.image.load("images/rightarm.png")
seconds = pygame.image.load("images/leftarm.png")

body_rect = body.get_rect(center=(512, 512))
minute_rect = minute.get_rect(center=body_rect.center)
second_rect = seconds.get_rect(center=body_rect.center)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.now().time()

    seconds_angle = current_time.second * 6
    minute_angle = (current_time.minute * 6) + (current_time.second / 10)

    rotated_second = pygame.transform.rotate(seconds, -seconds_angle)
    rotated_minute = pygame.transform.rotate(minute, -minute_angle)

    rotated_rect_min = rotated_minute.get_rect(center=body_rect.center)
    rotated_rect_sec = rotated_second.get_rect(center=body_rect.center)

    screen.blit(body, body_rect)
    screen.blit(rotated_second, rotated_rect_sec)
    screen.blit(rotated_minute, rotated_rect_min)

    pygame.display.flip()
    clock.tick(60)
