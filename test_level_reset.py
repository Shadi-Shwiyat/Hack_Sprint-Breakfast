import pygame
import json

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakfast Cooking Game")

# Define colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
FONT = pygame.font.Font(None, 24)

# Load JSON data from file
with open("breakfast_meal.json") as json_file:
    breakfasts_data = json.load(json_file)

# Define variables for the current level and ingredients
current_level = 1
selected_ingredients = []

# Load all ingredients and right ingredients for the current level
all_ingredients = breakfasts_data["breakfasts"][current_level - 1]["all_ingredients"]
right_ingredients = breakfasts_data["breakfasts"][current_level - 1]["right_ingredients"]

# Define the "Cook it!" button
button_rect = pygame.Rect(screen_width - 120, screen_height - 50, 100, 40)
button_color = BLACK
button_text = "Cook it!"

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Compare selected ingredients with right ingredients
                if sorted(selected_ingredients) == sorted(right_ingredients):
                    # Go to the next level if the ingredients are correct
                    current_level += 1
                    if current_level <= len(breakfasts_data["breakfasts"]):
                        all_ingredients = breakfasts_data["breakfasts"][current_level - 1]["all_ingredients"]
                        right_ingredients = breakfasts_data["breakfasts"][current_level - 1]["right_ingredients"]
                        selected_ingredients = []
                    else:
                        running = False  # Game over
                else:
                    selected_ingredients = []  # Reset selected ingredients
        
        elif event.type == pygame.KEYDOWN:
            if chr(event.key).isalpha():
                ingredient = chr(event.key)
                if ingredient in all_ingredients:
                    if ingredient in selected_ingredients:
                        selected_ingredients.remove(ingredient)
                    else:
                        selected_ingredients.append(ingredient)

    screen.fill(WHITE)
    
    # Draw all ingredients
    ingredients_text = ", ".join(all_ingredients)
    ingredients_surface = FONT.render(ingredients_text, True, BLACK)
    ingredients_rect = ingredients_surface.get_rect(center=(screen_width // 2, screen_height - 30))
    screen.blit(ingredients_surface, ingredients_rect)
    
    # Draw selected ingredients
    selected_text = ", ".join(selected_ingredients)
    selected_surface = FONT.render(selected_text, True, GREEN)
    selected_rect = selected_surface.get_rect(center=(screen_width // 2, screen_height - 10))
    screen.blit(selected_surface, selected_rect)
    
    # Draw "Cook it!" button
    pygame.draw.rect(screen, button_color, button_rect)
    button_text_surface = FONT.render(button_text, True, WHITE)
    button_text_rect = button_text_surface.get_rect(center=button_rect.center)
    screen.blit(button_text_surface, button_text_rect)
    
    pygame.display.flip()

pygame.quit()
