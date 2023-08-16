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
message = "Wes Says select the correct ingredients!"

# Render the message
text = font.render(message, True, black)

#Meals with their ingredients would go here
# Like Chicekn and Waffles = Chicken, Waffles, Syrup, Butter, blah blah blah

# Ingredients list not right, just copy and pasted some stuff from the internet
ingredients = ["Egg",
    "Bacon",
    "Sausage",
    "Ham",
    "Hash Browns",
    "Pancake",
    "Waffle",
    "French Toast",
    "Omelette",
    "Scrambled Eggs",
    "Bagel",
    "Cream Cheese",
    "Croissant",
    "Cereal",
    "Milk",
    "Yogurt",
    "Fresh Fruit (e.g., berries, banana)",
    "Maple Syrup",
    "Honey",
    "Jam",
    "Peanut Butter",
    "Oatmeal",
    "Granola",
    "Greek Yogurt",
    "Cottage Cheese",
    "Avocado",
    "Tomato",
    "Spinach",
    "Coffee",
    "Orange Juice"]

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
