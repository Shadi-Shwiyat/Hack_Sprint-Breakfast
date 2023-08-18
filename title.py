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
texbox = pygame.image.load("images/textbox.png")
texbox = pygame.transform.scale(texbox, (1200, 260))
plate = pygame.image.load("images/plate.png")
plate = pygame.transform.scale(plate, (50, 50))
# Chef Wes Poses
standard_pose = pygame.image.load("images/standard_pose.png")
standard_pose = pygame.transform.scale(standard_pose, (530, 690))
disgusted = pygame.image.load("images/disgusted.png")
disgusted = pygame.transform.scale(disgusted, (760, 900))
almost = pygame.image.load("images/almost.png")
almost = pygame.transform.scale(almost, (600, 760))
delicioso = pygame.image.load("images/delicioso.png")
delicioso = pygame.transform.scale(delicioso, (690, 830))
nope = pygame.image.load("images/nope.png")
nope = pygame.transform.scale(nope, (600, 700))
puke = pygame.image.load("images/puke.png")
puke = pygame.transform.scale(puke, (600, 700))
cook_it = pygame.image.load("images/cook_it.png")
cook_it = pygame.transform.scale(cook_it, (100, 100))

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
    #screen.blit(standard_pose, (530, 45))
    #screen.blit(disgusted, (530, 45))
    #screen.blit(almost, (530, 15))
    #screen.blit(delicioso, (560, 15))
    #screen.blit(nope, (560, 15))
    #screen.blit(puke, (560, 20))
    screen.blit(table, (40, 300))
    screen.blit(texbox, (40, 460))
    screen.blit(cook_it, (1000, 536))

    # Update the display
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
exit()