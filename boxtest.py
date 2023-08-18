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

# Load images
images = {}
image_folder = os.path.join("/root/Hack_Sprint-Breakfast", "images")
for breakfast in game_data["breakfasts"]:
    image_path = os.path.join(image_folder, breakfast["meal_picture"])
    image = pygame.image.load(image_path).convert_alpha()
    images[breakfast["name"]] = image

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 36)

current_level = 0  # Starting level
selected_ingredients = set()

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    
    # Display current level
    level_text = FONT.render(f"Level {current_level + 1}", True, BLACK)
    screen.blit(level_text, (10, 10))
    
    # Display ingredients for the current level
    ingredients_for_level = game_data["ingredients_per_level"][str(current_level)]
    ingredients_text = FONT.render("Ingredients: " + ", ".join(ingredients_for_level), True, BLACK)
    screen.blit(ingredients_text, (10, 50))
    
    # Display breakfast meals for the current level
    breakfasts_for_level = game_data["levels"][current_level]
    y_position = 100
    for breakfast_index in breakfasts_for_level:
        breakfast = game_data["breakfasts"][breakfast_index]
        breakfast_name = breakfast["name"]
        breakfast_ingredients = breakfast["ingredients"]
        
        # Display breakfast meal name and ingredients
        breakfast_text = FONT.render(f"{breakfast_name}: {', '.join(breakfast_ingredients)}", True, BLACK)
        screen.blit(breakfast_text, (10, y_position))
        
        # Display breakfast meal image
        if breakfast_name in images:
            image = images[breakfast_name]
            screen.blit(image, (600, y_position))
        
        # Check if player clicks on ingredients
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 10 <= mouse_x <= 300 and y_position <= mouse_y <= y_position + 36:
            pygame.draw.rect(screen, GRAY, (10, y_position, 290, 36), 2)
            if pygame.mouse.get_pressed()[0]:
                selected_ingredients = set(breakfast_ingredients)
        
        y_position += 50
    
    # Draw "Cook It" button
    cook_button_rect = pygame.Rect(1150, 650, 100, 40)
    pygame.draw.rect(screen, BLACK, cook_button_rect, 2)
    cook_button_text = FONT.render("Cook It", True, BLACK)
    screen.blit(cook_button_text, (1160, 660))
    
    # Draw "Quit" button
    quit_button_rect = pygame.Rect(1050, 650, 80, 40)
    pygame.draw.rect(screen, BLACK, quit_button_rect, 2)
    quit_button_text = FONT.render("Quit", True, BLACK)
    screen.blit(quit_button_text, (1060, 660))
    
    # Check for button clicks
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if cook_button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, GRAY, cook_button_rect, 2)
        if pygame.mouse.get_pressed()[0]:
            if selected_ingredients == set(game_data["ingredients_per_level"][str(current_level)]):
                print("Correct Ingredients! Cooking...")
                current_level += 1
                selected_ingredients = set()
                if current_level >= len(game_data["levels"]):
                    print("Congratulations! You've completed all levels.")
                    running = False
    elif quit_button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, GRAY, quit_button_rect, 2)
        if pygame.mouse.get_pressed()[0]:
            running = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
