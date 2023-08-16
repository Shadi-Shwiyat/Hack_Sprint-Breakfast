import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakfast Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load font
font = pygame.font.Font(None, 36)

# Define the message
message = "Select the correct ingredients!"

# Render the message
text = font.render(message, True, black)

# Ingredients list
ingredients = ["Egg", "Bacon", "Toast", "Cereal", "Milk", "Orange Juice", "Coffee", "Jam", "Butter", "Sausage", "Pancake", "Maple Syrup", "Fruit", "Yogurt", "Honey"]

# Select a random meal and its correct ingredients
meal = random.choice(ingredients)
correct_ingredients = random.sample(ingredients, 3)
correct_ingredients.append(meal)
random.shuffle(correct_ingredients)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)
    screen.blit(text, (100, 100))
    
    y = 150
    for ingredient in correct_ingredients:
        ingredient_text = font.render(ingredient, True, black)
        screen.blit(ingredient_text, (100, y))
        y += 50
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
