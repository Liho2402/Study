import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((650,650))
image = pygame.image.load("images/apple-music-note.jpg")
image_rect = image.get_rect(center=(360, 320))

songs = ["21 Savage - a lot (original version).mp3",
         "redrum.mp3",
         "Will.i.am - Heart Breaker.mp3",
         "Yeat - Breathe.mp3"]

done = False
pause = False

cnt = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                cnt += 1
                if cnt >= len(songs):
                    cnt = 0
                pygame.mixer.music.load(f"music/{songs[cnt]}")
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                cnt -= 1
                if cnt < 0:
                    cnt = len(songs) - 1
                pygame.mixer.music.load(f'music/{songs[cnt]}')
                pygame.mixer.music.play()
        # cnt += 1

    screen.blit(image, image_rect)
    pygame.display.flip()

