import json

# Breakfast Meal class
class BreakfastMeal:
    def __init__(self, name, ingredients, meal_picture):
        self.name = name
        self.ingredients = ingredients
        self.meal_picture = meal_picture
        
# Breakfast Meals to be used per level
breakfasts = [
    eggs_sausage = BreakfastMeal("Eggs and Sausage", ["Eggs", "Sausage"], "Eggs_and_Sausage.jpg"),
    BreakfastMeal("Bagel and Cream Cheese",["Bagel", "Cream Cheese"], "Bagel_and_Cream_Cheese.jpg"),
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Pie Crust"], "Quiche.jpg"),
    # Breakfast Meals to be used per level (More Difficult)
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Water", "Flour", "Salt", "Butter" ], "Quiche.jpg"),
    BreakfastMeal("Bacon Pancakes",["Pancake Batter", "Bacon", "Maple Syrup", "Butter"], "Bacon_Pancakes.jpg"),
    BreakfastMeal("Breakfast Burrito",["Tortilla", "Scrambled Eggs", "Sausage", "Cheese", "Salsa"], "Breakfast_Burrito.jpg"),
    BreakfastMeal("Chocolate Chip Waffles", ["Milk", "Eggs", "Flour", "Baking Powder", "Sugar", "Butter", "Chocolate Chips", "Syrup"], "Chocolate_Chip_Waffles.jpg"),
    BreakfastMeal("Full English Breakfast",["Eggs", "Bacon", "Toast", "Jam" "Hash Browns", "Sausage", "Baked Beans", "Tomato", "Mushrooms"], "Full_English_Breakfast.jpg"),
    BreakfastMeal("Chinese Congee", ["Rice", "Water", "Fried Egg", "Ginger", "Green Onion", "Soy Sauce"], "Chinese_Congee.jpg"),
    BreakfastMeal("Japanese Breakfast", ["Rice", "Miso Soup", "Grilled Fish", "Pickled Vegetables", "Fermented Soybean", "Rolled Omelette", "Seaweed"], "Japanese_Breakfast.jpg")
]
# Levels 1 to 10
levels = [
    [0], [1], [2], [3], [4], [5], [6], [7], [8], [9]
]

# List of right and wrong ingredients to be used per level
ingredients_per_level = {
    0: ["Eggs", "Sasuage", "Toast", "Bacon"],
    1: ["Bagel", "Cream Cheese", "Tortilla", "Hash Browns"],
    2: ["Eggs", "Cheese", "Milk", "Vegetables", "Pie Crust" "Tortilla", "Syrup", "Hash Browns", "Bacon", "Sasuage"],
    # List of right and wrong ingredients to be used per level (More Difficult)
    3: ["Eggs", "Cheese", "Milk", "Vegetables", "Water", "Flour", "Salt", "Butter", "Torilla", "Syrup", "Hash Browns", "Bacon", "Sasuage", "Bagel", "Cream Cheese", "Seaweed", "Baked Beans"],
    4: ["Pancake Batter", "Bacon", "Maple Syrup", "Butter", "Eggs", "Cheese", "Toast", "Sausage"],
    5: ["Tortilla", "Scrambled Eggs", "Sausage", "Cheese", "Salsa", "Toast", "Pie Crust", "Bagel", "Panckae Batter", "Chocolate Chips"],
    6: ["Milk", "Eggs", "Flour", "Baking Powder", "Sugar", "Butter", "Chocolate Chips", "Syrup", "Bacon", "Green Onion", "Cheese", "Pie Crust", "Ginger", "Soy Sauce", "Vegetables", "Mushrooms"],
    7: ["Eggs", "Bacon", "Toast", "Jam", "Hash Browns", "Sausage", "Baked Beans", "Tomato", "Mushrooms", "Rice", "Pancake Batter", "Vegetables", "Milk", "Flour", "Soy Sauce", "Fermented Soybean", "Green Onion", "Pickled Vegetables"],
    8: ["Rice", "Water", "Fried Egg", "Ginger", "Green Onion", "Soy Sauce", "Miso Soup", "Pickled Vegetables", "Rolled Omelette", "Milk", "Flour", "Syrup"],
    9: ["Rice", "Miso Soup", "Grilled Fish", "Pickled Vegetables", "Fermented Soybean", "Rolled Omelette", "Seaweed", "Eggs", "Baking Powder", "Jam", "Cheese", "Muhsrooms", "Butter", "Milk"] 
        
}

# Combine all data into a dictionary
game_data = {
    "breakfasts": [
        {"name": meal.name, "ingredients": meal.ingredients, "meal_picture": meal.meal_picture}
        for meal in breakfasts
    ],
    "levels": levels,
    "ingredients_per_level": ingredients_per_level
}

# Save the game data as JSON
with open("game_data.json", "w") as json_file:
    json.dump(game_data, json_file, indent=4)


###########################################################################################
# This is what it would look like in the main pygame file :)
###########################################################################################
import pygame
import json

# Initialize Pygame and screen

# Load game data from JSON
with open("game_data.json", "r") as json_file:
    game_data = json.load(json_file)

# Initialize game elements using the loaded data
breakfasts = [BreakfastMeal(**data) for data in game_data["breakfasts"]]
levels = game_data["levels"]
ingredients_per_level = game_data["ingredients_per_level"]

# Set up Level 1
level_index = 0  # Index of Level 1 in the 'levels' list
current_level = levels[level_index]
correct_ingredients = ingredients_per_level[level_index]

# Display the meal picture (you can replace this with your image loading logic)
meal_picture = pygame.image.load(breakfasts[current_level[0]].meal_picture)

# Display the ingredients
y_offset = 100
for ingredient in correct_ingredients:
    text = FONT.render(ingredient, True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
    screen.blit(text, text_rect)
    y_offset += 40

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input (e.g., select ingredients)

    # Check correctness and update score and level
    if set(player.selected_ingredients) == set(correct_ingredients):
        player.score += 1
        player.current_level += 1
        player.selected_ingredients = []
        
        # Transition to the next level if available
        if player.current_level < len(levels):
            level_index = player.current_level
            current_level = levels[level_index]
            correct_ingredients = ingredients_per_level[level_index]
            
            # Update the meal picture and ingredients display (similar to the above code)

    # Update the display
    pygame.display.flip()

# Clean up and quit
pygame.quit()
