import os
import pygame
import json
import random
from sys import exit

# Fixing audio issue
os.environ['SDL_AUDIODRIVER'] = 'dsp'

# Initializing pygame and window size
pygame.init()
screen = pygame.display.set_mode((1280, 720))

# Setting title of window
pygame.display.set_caption("Rise and Dine: Wes's Cozy Kitchen")

# Importing Json dictionary of meals and ingredients
with open('breakfast_meal.json') as json_file:
    data = json.load(json_file)

# Load font
font_path = "./Minecraft.ttf"
font = pygame.font.Font(None, 30)

# Instantiating Ingredient Buttons
from button import Button
current_level = 5 # Set the inital level
level_ingredients = {}

for breakfast in data["breakfasts"]:
    level = int(breakfast["level"])
    ingredients = breakfast["all_ingredients"]

    if level not in level_ingredients:
        level_ingredients[level] = []

    level_ingredients[level].extend(ingredients)
 
# Ingredient lists needed for current level to be compared
current_ingredients = level_ingredients.get(current_level, []) # List of all ingredients for level
split_index = len(current_ingredients) // 2 # Splitting all ingredients by 2
right_ingredients = current_ingredients[:split_index] # List of right ingredients for level
selected_ingredients = [] # Current ingredients selected by user
random.shuffle(current_ingredients) # Make the ingredient buttons random
ingredients_compared = False # For displaying result message
result_message = "" # Message to show user based on level success

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

# Define start cooking button
start_cooking_button = Button("Start Cooking!", (913, 560), font_size=30, size=(200, 50), hover_size=(200, 40))
start_cooking_button.button_color = (0, 0, 0, 0)

# Extract sentences for level 1 from JSON data
level_sentences = data["breakfasts"][current_level - 1]["wes_says"]

# Create TextAnimation instance for level 1
from text_animation import TextAnimation
text_animation = TextAnimation(level_sentences, 800, 150, font, (255, 255, 255), 800, 0.00001, 0)

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

# Game loop
clock = pygame.time.Clock() # Creating a clock object
run = True

while run:
    # Things to clear each loop iteration

    # Update the text animation
    text_animation.update()

    # Event to quit loop when user hits X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if text_animation.finished:
            # Event for ingredient button clicks
            for button in buttons:
                button.handle_events(event)
                # Adding selected buttons to list
                if button.selected and button.text not in selected_ingredients:
                    selected_ingredients.append(button.text)
                    print(selected_ingredients)
                elif button.selected == False and button.text in selected_ingredients:
                    selected_ingredients.remove(button.text)
                    print(selected_ingredients)

            # Event for start cooking button
            start_cooking_button.handle_events(event)
            if start_cooking_button.clicked:
                start_cooking_button.clicked = False
                start_cooking_button.selected = False
                print("Start Cooking button clicked!")

                # Compare user-selected ingredients with correct ingredients
                if sorted(selected_ingredients) == sorted(right_ingredients):
                    print("Ingredients match!")
                    result_message = "THERE IS A GOD!"  # Update the result_message
                else:
                    print("Ingredients do not match..")
                    result_message = "Darn it!"  # Update the result_message

                ingredients_compared = True # Update the rect attribute of the start_cooking_button
                selected_ingredients = [] # Clear the user-selected ingredients list for the next level

    # Blit Background and Assets to the screen
    screen.blit(background, (-110, -50))
    screen.blit(standard_pose, (530, 45))
    #screen.blit(disgusted, (530, 45))
    #screen.blit(almost, (530, 15))
    #screen.blit(delicioso, (560, 15))
    #screen.blit(nope, (560, 15))
    #screen.blit(puke, (560, 20))
    screen.blit(table, (40, 300))

    # Blit textbox when text is done looping
    if text_animation.finished:
        screen.blit(textbox, (40, 450))
        screen.blit(cook_it, (930, 536))
    
    # Draw text animation
    text_animation.draw(screen) 

    # Draw the buttons
    if text_animation.finished:  
        for button in buttons:
            button.draw()
        start_cooking_button.draw()

    # Draw result message if ingredients are compared
    if ingredients_compared:
        result_font = pygame.font.Font(None, 36)
        result_surf = result_font.render(result_message, True, (0, 0, 0))
        result_rect = result_surf.get_rect(center=(screen.get_width() // 2, 650))
        screen.blit(result_surf, result_rect)

    # Update the display
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    clock.tick(60)
    #print(clock)

pygame.quit()
exit()
