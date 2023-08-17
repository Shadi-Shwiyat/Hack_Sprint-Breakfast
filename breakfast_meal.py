import json

class BreakfastMeal:
    def __init__(self, name, ingredients, meal_picture):
        self.name = name
        self.ingredients = ingredients
        self.meal_picture = meal_picture

breakfasts = [
    BreakfastMeal("Eggs_and_Sausage", ["Eggs", "Sausage"], "Eggs_and_Sausage.jpg"),
    BreakfastMeal("Bagel_and_Cream_Cheese",["Bagel", "Cream Cheese"], "Bagel_and_Cream_Cheese.jpg"),
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Pie Crust"], "Quiche.jpg"),
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Water", "Flour", "Salt", "Butter" ], "Quiche.jpg"),
    BreakfastMeal("Bacon_Pancakes",["Pancake Batter", "Bacon", "Maple Syrup", "Butter"], "Bacon_Pancakes.jpg"),
    BreakfastMeal("Breakfast_Burrito",["Tortilla", "Scrambled Eggs", "Sausage", "Cheese", "Salsa"], "Breakfast_Burrito.jpg"),
    BreakfastMeal("Chocolate_Chip_Waffles", ["Milk", "Eggs", "Flour", "Baking Powder", "Sugar", "Butter", "Chocolate Chips", "Syrup"], "Chocolate_Chip_Waffles.jpg"),
    BreakfastMeal("Full_English_Breakfast",["Eggs", "Bacon", "Toast", "Jam" "Hash Browns", "Sausage", "Baked Beans", "Tomato", "Mushrooms"], "Full_English_Breakfast.jpg"),
    BreakfastMeal("Chinese_Congee", ["Rice", "Water", "Fried Egg", "Ginger", "Green Onion", "Soy Sauce"], "Chinese_Congee.jpg"),
    BreakfastMeal("Japanese_Breakfast", ["Rice", "Miso Soup", "Grilled Fish", "Pickled Vegetables", "Fermented Soybean", "Rolled Omelette", "Seaweed"], "Japanese_Breakfast.jpg")
]

levels = [
    [0], # Level 1
    [1], # Level 2
    [2], # Level 3
    [3], # Level 4
    [4], # Level 5
    [5], # Level 6
    [6], # Level 7
    [7], # Level 8
    [8], # Level 9
    [9] # Level 10
]

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
    "breakfasts":# List of BreakfastMeal objects need to figure out how to make this a list of strings
    "levels": levels,
    "ingredients_per_level": ingredients_per_level
}

# Save the game data as JSON
with open("game_data.json", "w") as json_file:
    json.dump(game_data, json_file, indent=4)

print("Game data saved as game_data.json")
