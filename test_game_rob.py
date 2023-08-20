import pygame
import time
import json
import os
from pygame import mixer
from sys import exit
from button import Button
from text_animation import TextAnimation

# Fixing audio issue
os.environ['SDL_AUDIODRIVER'] = 'dsp'

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
# Instantiating Ingredient Buttons#########################
from button import Button
current_level = 1 # Set the inital level
buttons = []
level_ingredients = {}

for breakfast in data["breakfasts"]:
    level = int(breakfast["level"])
    ingredients = breakfast["all_ingredients"]

    if level not in level_ingredients:
        level_ingredients[level] = []

    level_ingredients[level].extend(ingredients)
    
# Select ingredient list for current level
current_ingredients = level_ingredients.get(current_level, [])

# Calculate available width and height for placing the buttons
available_width = 900
available_height = 690
max_buttons_per_row = 4  # Maximum buttons that can fit in a row

# Calculate the required number of rows
num_rows = (len(current_ingredients) + max_buttons_per_row - 1) // max_buttons_per_row

# Calculate the spacing between rows and buttons
row_spacing = (available_height - 430) / (num_rows + 1)
button_spacing = (available_width - (max_buttons_per_row * 100)) / (max_buttons_per_row + 1)

# Specify the starting position for the buttons
start_x = 46 + button_spacing  # Adjust as needed
start_y = 440 + row_spacing  # Adjust as needed

# Create buttons for ingredients of the current level
x, y = start_x, start_y  # Starting coordinates
buttons = []  # List used to draw the buttons

# Adding buttons to the list to be drawn
for ingredient in current_ingredients:
    buttons.append(Button(ingredient, (x, y), font_size=26))
    x += 100 + button_spacing
    if len(buttons) % max_buttons_per_row == 0:
        x = start_x
        y += row_spacing

# Creating instances of the Start Cooking Button class
start_cooking_button = Button("Start Cooking!", (160, 100), 30)

##############################
# Game loop ####################################################################################################################
##############################
clock = pygame.time.Clock()
running = True


# Background Music
mixer.music.load("music/Intro Music for hack.mp3")
mixer.music.play(-1) # -1 means loop forever
mixer.music.set_volume(0.3)



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
    
    
    ####################  Everything Happens here in this loop
    # Draw the text animation
    text_animation.draw(screen)
    
    if text_animation.finished:
        # Blit textbox image
        screen.blit(textbox, (40, 450))
        # Blit start cooking button
        screen.blit(cook_it, (930, 536))
        
        # Draw the buttons
        for button in buttons:
            button.draw()
            # drawing start cooking button
            start_cooking_button.draw()
            
                # Draw result message if ingredients are compared
            
        
        
    
    

    
    

    
    # Draw the text animation
    text_animation.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
