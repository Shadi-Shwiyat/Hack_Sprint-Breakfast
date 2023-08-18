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
background = pygame.transform.scale(background, (1480, 900))

# Images to display over background
table = pygame.image.load("images/table.png")
table = pygame.transform.scale(table, (1200, 530))
texbox_table = pygame.image.load("images/textbox_table.png")
texbox_table = pygame.transform.scale(texbox_table, (1200, 530))
plate = pygame.image.load("images/plate.png")
plate = pygame.transform.scale(plate, (50, 50))

# Game loop
clock = pygame.time.Clock() # Creating a clock object
run = True
while run:
    # Event to quit loop when user hits X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Blit Background and Assets to the screen
    screen.blit(background, (-110, -50))
    screen.blit(table, (40, 300))
    #screen.blit(texbox_table, (40, 200))

    # Update the display
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
exit()