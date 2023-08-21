import os
import pygame
import json
import random

def current_level_setup(current_level):
    # Importing Json dictionary of meals and ingredients
    with open('breakfast_meal.json') as json_file:
        data = json.load(json_file)

    # Load font
    font_path = "./Minecraft.ttf"
    font = pygame.font.Font(None, 30)

    # Instantiating Ingredient Buttons
    from button import Button
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
    random.shuffle(current_ingredients) # Make the ingredient buttons random

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

    # Extract sentences for level 1 from JSON data
    level_sentences = data["breakfasts"][current_level - 1]["wes_says"]

    # Create TextAnimation instance for level 1
    from text_animation import TextAnimation
    level_text = TextAnimation(level_sentences, 830, 96, font, (0, 0, 0), 1030, 0.03, 1)

    # Load the meal_picture for the current level
    if current_level >= 1:
        current_meal_picture_url = "images/" + data["breakfasts"][current_level - 1]["meal_picture"]
        current_meal_picture = pygame.image.load(current_meal_picture_url)
        current_meal_picture = pygame.transform.scale(current_meal_picture, (160, 160))

        return {
            "current_ingredients": current_ingredients,
            "right_ingredients": right_ingredients,
            "level_text": level_text,
            "current_meal_picture": current_meal_picture,
            "buttons": buttons
        }
    elif current_level == 11:
        return {
            "level_text": level_text
        }
    else:
        return {
            "current_ingredients": current_ingredients,
            "right_ingredients": right_ingredients,
            "level_text": level_text,
            "buttons": buttons
        }