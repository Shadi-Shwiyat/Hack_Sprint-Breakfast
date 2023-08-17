import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1280, 720
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

# Define breakfast meals with ingredients
breakfast_meals = [
    ("Classic American Breakfast", ["Eggs", "Bacon", "Toast", "Hash Browns"]),
    ("Pancakes with Maple Syrup", ["Pancake Batter", "Maple Syrup", "Butter"]),
    # ... add other breakfast meals here ...
    ("Breakfast Burrito", ["Tortilla", "Scrambled Eggs", "Sausage", "Cheese", "Salsa"]),
    ("Fresh Fruit Salad", ["Mixed Fresh Fruit"]),
    ("Bacon and Egg Breakfast Sandwich", ["English Muffin", "Bacon", "Egg", "Cheese"]),
    ("Avocado Toast", ["Toasted Bread", "Avocado", "Tomato", "Red Onion"]),
    # ... add more breakfast meals ...
    ("Italian Breakfast Frittata", ["Eggs", "Tomatoes", "Basil", "Mozzarella"]),
    ("Cinnamon Roll with Cream Cheese Frosting", ["Cinnamon Roll", "Cream Cheese Frosting"]),
    ("Chia Seed Pudding", ["Chia Seeds", "Almond Milk", "Honey"]),
    ("Veggie Breakfast Bowl", ["Scrambled Eggs", "Avocado", "Tomato", "Black Beans"]),
    # ... add more breakfast meals ...
]

# Randomly select a meal
meal = random.choice(breakfast_meals)
# Get the meal name
meal_name = meal[0]
# Get the meal ingredients
meal_ingredients = meal[1]
# Add the meal name to the meal ingredients
meal_ingredients.append(meal_name)
# Randomly shuffle the meal ingredients
random.shuffle(meal_ingredients)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)
    screen.blit(text, (100, 100))
    
    y = 150
    for ingredient in meal_ingredients:
        ingredient_text = font.render(ingredient, True, black)
        screen.blit(ingredient_text, (100, y))
        y += 50
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
