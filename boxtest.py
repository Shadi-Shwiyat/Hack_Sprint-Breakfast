import pygame
import json
import os

# Initialize Pygame
pygame.init()

# Load game data from JSON
with open("breakfast_meal.json", "r") as json_file:
    game_data = json.load(json_file)

# Set up display
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Breakfast Matching Game")

# Define colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 36)

# Initialize variables
current_level = 0
selected_ingredients = set()
correct_ingredients = set(game_data["breakfasts"][current_level]["right_ingredients"])

running = True
while running:
    screen.fill(WHITE)
    
    # Display breakfast name
    breakfast_name = game_data["breakfasts"][current_level]["name"]
    breakfast_name_text = FONT.render(breakfast_name, True, BLACK)
    screen.blit(breakfast_name_text, (10, 10))
    
    # Display wrong ingredients selection
    wrong_ingredients = game_data["breakfasts"][current_level]["wrong_ingredients"]
    y_position = 60
    for ingredient in wrong_ingredients:
        pygame.draw.rect(screen, GRAY, (10, y_position, 200, 30))
        ingredient_text = FONT.render(ingredient, True, BLACK)
        screen.blit(ingredient_text, (20, y_position))
        
        # Check if player selects an ingredient
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 10 <= mouse_x <= 210 and y_position <= mouse_y <= y_position + 30:
            pygame.draw.rect(screen, BLACK, (10, y_position, 200, 30), 2)
            if pygame.mouse.get_pressed()[0]:
                selected_ingredients.add(ingredient)
        
        y_position += 40
    
    # Display cook button
    cook_button_rect = pygame.Rect(10, 500, 100, 40)
    pygame.draw.rect(screen, BLACK, cook_button_rect, 2)
    cook_button_text = FONT.render("Cook It", True, BLACK)
    screen.blit(cook_button_text, (20, 510))
    
    # Check for cook button click
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if cook_button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, GRAY, cook_button_rect, 2)
        if pygame.mouse.get_pressed()[0]:
            if selected_ingredients == correct_ingredients:
                print("Correct Ingredients! Cooking...")
                current_level += 1
                selected_ingredients.clear()
                correct_ingredients = set(game_data["breakfasts"][current_level]["right_ingredients"])
                if current_level >= len(game_data["breakfasts"]):
                    print("Congratulations! You've completed all levels.")
                    running = False
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limit to 60 FPS
    pygame.time.Clock().tick(60)

pygame.quit()
