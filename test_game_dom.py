import os
import pygame
import json
from sys import exit
from button import Button

# Fixing audio issue
os.environ['SDL_AUDIODRIVER'] = 'dsp'

# Importing Json dictionary of meals and ingredients
with open('breakfast_meal.json') as json_file:
    data = json.load(json_file)

# Initializing pygame and window size
pygame.init()
screen = pygame.display.set_mode((1280, 720))

# Setting title of window
pygame.display.set_caption("Rise and Dine: Wes's Cozy Kitchen")

# Instantiating Ingredient Buttons
from button import Button
level_ingredients = {}

for breakfast in data["breakfasts"]:
    level = int(breakfast["level"])
    ingredients = breakfast["all_ingredients"]

    if level not in level_ingredients:
        level_ingredients[level] = []

    level_ingredients[level].extend(ingredients)

# Instantiating start_cooking_button
start_cooking_button = Button("Start\nCooking", (1000, 536), font_size=26)

start_cooking_clicked = False # initialize the flag
result_message = ""
ingredients_compared = True

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
cook_it = pygame.transform.scale(cook_it, (100, 100))

# Game loop
clock = pygame.time.Clock() # Creating a clock object
current_level = 8 # Set the inital level
run = True
selected_ingredients = [] # to store users selected ingredients

while run:
    # Event to quit loop when user hits X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_cooking_button.rect.collidepoint(event.pos):
                start_cooking_clicked = True
                selected_ingredients = []  # Reset the selected ingredients when "Start Cooking" is clicked

                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        selected_ingredients.append(button.text)

    # Update the position and size of the start_cooking_button based on conditions
    start_cooking_button.pos = (1000, 536 )  # Update the position
    start_cooking_button.size = (200, 50)  # Update the size

    # Update the rect attribute of the start_cooking_button
    start_cooking_button.update_rect()
                        
    if start_cooking_clicked:
        print("Start Cooking button clicked!")

        # Get the correct ingredients for the current level
        correct_ingredients = level_ingredients.get(current_level, [])

        # Compare user-selected ingredients with correct ingredients
        if sorted(selected_ingredients) == sorted(correct_ingredients):
            print("Ingredients match! You can start cooking.")
            result_message = "Ingredients matched!"  # Update the result_message
        else:
            print("Ingredients do not match. Try again.")
            result_message = "Ingredients did not match!"  # Update the result_message

            
        # Set the flag to indicate that the comparison has been performed
        ingredients_compared = True
    
        # Clear the user-selected ingredients list for the next level
        user_selected_ingredients = []

        # Reset the flag to prevent repeated actions
        start_cooking_clicked = False
        
    # Blit Background and Assets to the screen
    screen.blit(background, (-110, -50))
    #screen.blit(standard_pose, (530, 45))
    #screen.blit(disgusted, (530, 45))
    #screen.blit(almost, (530, 15))
    #screen.blit(delicioso, (560, 15))
    #screen.blit(nope, (560, 15))
    screen.blit(puke, (560, 20))
    screen.blit(table, (40, 300))
    screen.blit(textbox, (40, 450))
    screen.blit(cook_it, (1000, 536))

    # Select ingredient list for current level
    current_ingredients = level_ingredients.get(current_level, [])

    # Calculate available width and height for placing the buttons
    available_width = 960
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
    buttons = []  # Clear the buttons list for each iteration

    for ingredient in current_ingredients:
        buttons.append(Button(ingredient, (x, y), font_size=26))
        x += 100 + button_spacing

        if len(buttons) % max_buttons_per_row == 0:
            x = start_x
            y += row_spacing

    
    # Draw the buttons
    for button in buttons:
        button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_cooking_button.rect.collidepoint(event.pos):
                start_cooking_clicked = True


    if start_cooking_clicked:
        print("Start Cooking button clicked!")
        # Reset the flag to prevent repeated actions
        start_cooking_clicked = False


    start_cooking_button.draw()
    
    if ingredients_compared:
        result_font = pygame.font.Font(None, 36)
        result_surf = result_font.render(result_message, True, (0, 0, 0))
        result_rect = result_surf.get_rect(center=(screen.get_width() // 2, 650))
        screen.blit(result_surf, result_rect)

    # Update the display
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
exit()
