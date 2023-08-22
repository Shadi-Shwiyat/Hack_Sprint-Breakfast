import pygame
from pygame import mixer
from level_setup import *
from sys import exit
from audio import GameAudio

# Initializing pygame and window size
pygame.init()
screen = pygame.display.set_mode((1280, 720))

# initializing audio
pygame.mixer.init()
audio = GameAudio()

# Play background music
audio.play_background_music('intro')

# Setting title of window
pygame.display.set_caption("Rise and Dine: Wes's Cozy Kitchen")

# Load font
text_font = pygame.font.Font("PixeloidSans-mLxMm.ttf", 30)

# Define start menu, cooking and continue buttons
from button import Button
start_cooking_button = Button("Start Cooking!", (913, 560), font_size=19, size=(200, 50), hover_size=(200, 40))
start_cooking_button.button_color = (0, 0, 0, 0)
progress = Button("Continue", (800, 480), font_size=23, size=(200, 50), hover_size=(200, 40))
progress.button_color = (0, 0, 0, 0)
start_button = Button("Start", (476, 439), font_size=66, size=(260, 60), hover_size=(260, 50))
start_button.button_color = (0, 0, 0, 0)
quit_button = Button("Exit", (476, 566), font_size=66, size=(260, 60), hover_size=(260, 50))
quit_button.button_color = (0, 0, 0, 0)

# Load level setup from function
current_level = 10
if current_level == 0:
    menu = pygame.image.load("images/start_menu.png")
    menu = pygame.transform.scale(menu, (500, 720))
    cozy = pygame.image.load("images/cozy.png")
    cozy = pygame.transform.scale(cozy, (403, 303))
    rise_dine = pygame.image.load("images/rise_dine.png")
    rise_dine = pygame.transform.scale(rise_dine, (330, 260))
    
level_data = current_level_setup(current_level)
current_ingredients = level_data["current_ingredients"]
right_ingredients = level_data["right_ingredients"]
level_text = level_data["level_text"]
if current_level > 0:
    current_meal_picture = level_data["current_meal_picture"]
buttons = level_data["buttons"]
selected_ingredients = []

# Background Image
background = pygame.image.load("images/kitchen_background.jpeg")
background = pygame.transform.scale(background, (1480, 900))

# Images to display over background
table = pygame.image.load("images/table.png")
table = pygame.transform.scale(table, (1200, 530))
textbox = pygame.image.load("images/textbox.png")
textbox = pygame.transform.scale(textbox, (1200, 276))
chatbox = pygame.image.load("images/chat.png")
chatbox = pygame.transform.scale(chatbox, (400, 150))
plate = pygame.image.load("images/servingPlate.png")
plate = pygame.transform.scale(plate, (230, 160))
dubious = pygame.image.load("images/dubious.png")
dubious = pygame.transform.scale(dubious, (260, 260))
# Chef Wes Poses
standard_pose = pygame.image.load("images/standard_pose.png")
standard_pose = pygame.transform.scale(standard_pose, (530, 690))
disgusted = pygame.image.load("images/disgusted.png")
disgusted = pygame.transform.scale(disgusted, (760, 900))
almost = pygame.image.load("images/almost.png")
almost = pygame.transform.scale(almost, (600, 760))
delicioso = pygame.image.load("images/delicioso.png")
delicioso = pygame.transform.scale(delicioso, (660, 803))
nope = pygame.image.load("images/nope.png")
nope = pygame.transform.scale(nope, (600, 700))
puke = pygame.image.load("images/puke.png")
puke = pygame.transform.scale(puke, (600, 700))
cook_it = pygame.image.load("images/cook_it.png")
cook_it = pygame.transform.scale(cook_it, (160, 100))
# Nessesary dish images
english = pygame.image.load("images/english.png")
english = pygame.transform.scale(english, (360, 160))
congee = pygame.image.load("images/congee.png")
congee = pygame.transform.scale(congee, (290, 199))
japanese = pygame.image.load("images/japanese.png")
japanese = pygame.transform.scale(japanese, (360, 230))

# Game setup
level_success = False # For displaying result message
ingredients_compared = False # For displaying different wes poses
image_flip = True
result_message = level_results(current_level)
max_levels = 10

# Game loop
clock = pygame.time.Clock() # Creating a clock object
run = True

while run:
    # Things to clear each loop iteration
    
    # Update the text animation
    if current_level >= 1 and current_level < 11:
        level_text.update()

        # Event to quit loop when user hits X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if level_text.finished:
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
                    progress.clicked = False
                    print("Start Cooking button clicked!")
                    audio.play_sound_effect('cooking food')
                    pygame.time.delay(2000)

                    # Compare user-selected ingredients with correct ingredients
                    if sorted(selected_ingredients) == sorted(right_ingredients):
                        print("Ingredients match!")
                        level_success = True
                        audio.play_sound_effect('level success')
                        audio.play_sound_effect('level success 2', delay_ms=2500)
                        screen.blit(background, (-110, -50))
                        screen.blit(delicioso, (630, 15))
                        screen.blit(table, (40, 300))
                        screen.blit(chatbox, (273, 76))
                        # Blit the meal_picture on the screen
                        if current_level <= 7:
                            screen.blit(plate, (300, 430))
                            screen.blit(current_meal_picture, (336, 390))
                        else:
                            if current_level == 8:
                                screen.blit(english, (300, 390))
                            elif current_level == 9:
                                screen.blit(congee, (336, 330))
                            elif current_level == 10:
                                screen.blit(japanese, (290, 330))
                    else:
                        ingredients_compared = True
                        image_flip = not image_flip
                        print("Ingredients do not match..")
                        audio.play_sound_effect('failing level', delay_ms=1000)
                        audio.play_sound_effect('vomiting')

                # Continue button to go to next level
                if level_success:
                    progress.handle_events(event)
                    screen.blit(cook_it, (819, 456))
                    if progress.clicked:
                        #print("progress clicked")
                        progress.clicked = False
                        progress.selected = False
                        if current_level <= max_levels:
                            current_level += 1
                            level_data = current_level_setup(current_level)
                            current_ingredients = level_data["current_ingredients"]
                            right_ingredients = level_data["right_ingredients"]
                            level_text = level_data["level_text"]
                            current_meal_picture = level_data["current_meal_picture"]
                            buttons = level_data["buttons"]
                            ingredients_compared = False
                            level_text.finished = False
                            level_success = False

                    selected_ingredients = [] # Clear the user-selected ingredients list for the next level

    elif current_level == 11:
        audio.stop_music()
        #audio.play_background_music('credits')
        level_text.update()
        if level_text.finished:
            run = False
            pygame.quit()
            exit()

    # If the current level is 0 (Start Menu)
    else:
        # Event to quit loop when user hits X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Event listeners for start menu
            start_button.handle_events(event)
            if start_button.clicked:
                start_button.clicked = False
                start_button.selected = False
                current_level += 1
                level_data = current_level_setup(current_level)
                current_ingredients = level_data["current_ingredients"]
                right_ingredients = level_data["right_ingredients"]
                level_text = level_data["level_text"]
                current_meal_picture = level_data["current_meal_picture"]
                buttons = level_data["buttons"]
            quit_button.handle_events(event)
            if quit_button.clicked:
                pygame.quit()
                exit()

    # Blit pose based on current player status
    if current_level == 0:
        screen.blit(background, (-110, -50))
        screen.blit(menu, (360, 0))
        screen.blit(cozy, (869, 230))
        screen.blit(rise_dine, (23, 230))
           
        
    else:
        if level_success == False:
            screen.blit(background, (-110, -50))
            if ingredients_compared == False:
                screen.blit(standard_pose, (530, 45))
            elif image_flip:
                screen.blit(disgusted, (530, 45))
            else:
                screen.blit(puke, (560, 20))
            screen.blit(chatbox, (273, 76))
            screen.blit(table, (40, 300))
            if ingredients_compared:
                screen.blit(dubious, (326, 190))
    #screen.blit(almost, (530, 15))
    #screen.blit(nope, (560, 15))

    # Blit textbox when text is done looping
    if level_text.finished and level_success == False:
        screen.blit(textbox, (40, 450))
        screen.blit(cook_it, (930, 536))
    
    # Draw text animation and result messages
    if not level_success:
        level_text.draw(screen)
    else:
        result_message.update()
        result_message.draw(screen)
        progress.draw()

    # Draw the buttons
    if current_level == 0:
        start_button.draw()
        quit_button.draw()
    if level_text.finished and level_success == False:  
        for button in buttons:
            button.draw()
        start_cooking_button.draw()

    # Update the display
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    clock.tick(60)
    #print(clock)

pygame.quit()
exit()
