import pygame
import json

# Initialize Pygame
pygame.init()

# Load game data from JSON
with open("breakfast_meal.json", "r") as json_file:
    game_data = json.load(json_file)

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakfast Matching Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

current_level = 0  # Starting level

running = True
while running:
    screen.fill(WHITE)
    
    # Display current level
    level_text = FONT.render(f"Level {current_level + 1}", True, BLACK)
    screen.blit(level_text, (10, 10))
    
    # Display breakfast meals for the current level
    breakfasts_for_level = game_data["levels"][current_level]
    y_position = 60
    for breakfast_index in breakfasts_for_level:
        breakfast = game_data["breakfasts"][breakfast_index]
        breakfast_name = breakfast["name"]
        breakfast_ingredients = breakfast["ingredients"]
        
        breakfast_text = FONT.render(f"{breakfast_name}: {', '.join(breakfast_ingredients)}", True, BLACK)
        screen.blit(breakfast_text, (10, y_position))
        y_position += 40
    
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Here you would compare the player's selected ingredients with the correct ones for the current level
                # For demonstration purposes, let's assume they are always correct
                print("Correct Ingredients!")
                current_level += 1
                if current_level >= len(game_data["levels"]):
                    print("Congratulations! You've completed all levels.")
                    running = False
    
    pygame.display.flip()

pygame.quit()
