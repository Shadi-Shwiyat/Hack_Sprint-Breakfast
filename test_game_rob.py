import pygame
import time
import json
from sys import exit
from button import Button
from text_animation import TextAnimation


# Initialize pygame
pygame.init()

# Create the display window
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rise and Dine: Wes's Cozy Kitchen")

# Background Image
background = pygame.image.load("images/kitchen_background.jpeg")
background = pygame.transform.scale(background, (1480, 900))

# Images to display over background
table = pygame.image.load("images/table.png")
table = pygame.transform.scale(table, (1200, 530))
textbox = pygame.image.load("images/textbox.png")
textbox = pygame.transform.scale(textbox, (1200, 276))
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
cook_it = pygame.transform.scale(cook_it, (160, 100))

# Load JSON data
with open('breakfast_meal.json') as json_file:
    data = json.load(json_file)
    
# Extract sentences for level 1 from JSON data
level_1_sentences = data["breakfasts"][0]["wes_says"]

# Load font
font = pygame.font.Font(None, 30)

# Create TextAnimation instance for level 1
text_animation = TextAnimation(level_1_sentences, 800, 150, font, (255, 255, 255), 800, 0.001, 2)

# Game loop####################################################################################################################
clock = pygame.time.Clock()
running = True

while running:
    # Things to clear each loop iteration
    current_frame_selected = []
    #screen.fill((0, 0, 0))
    
    # Event to quit loop when user hits X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            running = False
    
    # Update the text animation
    text_animation.update()
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    #These images stack on top of each other, so the order matters
    # Blit background image
    screen.blit(background, (0, 0))
    # Blit Wes image
    screen.blit(standard_pose, (640, 30))
    # Blit table image
    screen.blit(table, (40, 300))
    
    if text_animation.finished:
        # Blit textbox image
        screen.blit(textbox, (40, 30))
        # Blit plate image
        screen.blit(plate, (100, 500))
        # Blit start cooking button
        screen.blit(cook_it, (913, 560))
        
    
    

    
    

    
    # Draw the text animation
    text_animation.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
