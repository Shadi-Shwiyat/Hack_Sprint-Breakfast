import os
from sys import exit
import pygame

# Fixing audio issue
os.environ['SDL_AUDIODRIVER'] = 'dsp'

# Initializing pygame and window size
pygame.init()
screen = pygame.display.set_mode((1280, 720))

# Setting title of window
pygame.display.set_caption("Title")

# Background Image
background = pygame.image.load("images/kitchen_background.jpeg")
background = pygame.transform.scale(background, (1280, 720))

# Game loop
run = True
while run:
    # Event to quit loop when user hits X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Blit Background to the screen
    screen.blit(background, (0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()
exit()