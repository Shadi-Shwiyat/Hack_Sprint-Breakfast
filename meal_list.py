class BreakfastMeal:
    def __init__(self, name, ingredients, meal_picture):
        self.name = name
        self.ingredients = ingredients = ingredients
        self.meal_picture = meal_picture
    

# Breakfast Meals to be used per level
breakfasts = [
    BreakfastMeal("Eggs_and_Sasauge",["Eggs", "Sasuage"], "Eggs_and_Sasuage.jpg")
    BreakfastMeal("Bagel_and_Cream_Cheese",["Bagel", "Cream Cheese"], "Bagel_and_Cream_Cheese.jpg")
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Pie Crust"], "Quiche.jpg")
    # Breakfast Meals to be used per level (More Difficult)
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Water", "Flour", "Salt", "Butter" ], "Quiche.jpg")
    BreakfastMeal("Bacon_Pancakes",["Pancake Batter", "Bacon", "Maple Syrup", "Butter"], "Bacon_Pancakes.jpg")
    BreakfastMeal("Breakfast_Burrito",["Tortilla", "Scrambled Eggs", "Sausage", "Cheese", "Salsa"], "Breakfast_Burrito.jpg")
    BreakfastMeal("Chocolate_Chip_Waffles", ["Milk", "Eggs", "Flour", "Baking Powder", "Sugar", "Butter", "Chocolate Chips", "Syrup"], "Chocolate_Chip_Waffles.jpg")
    BreakfastMeal("Full_English_Breakfast",["Eggs", "Bacon", "Toast", "Jam" "Hash Browns", "Sausage", "Baked Beans", "Tomato", "Mushrooms"], "Full_English_Breakfast.jpg")
    BreakfastMeal("Chinese_Congee", ["Rice", "Water", "Fried Egg", "Ginger", "Green Onion", "Soy Sauce"], "Chinese_Congee.jpg")
    BreakfastMeal("Japanese_Breakfast", ["Rice", "Miso Soup", "Grilled Fish", "Pickled Vegetables", "Fermented Soybean", "Rolled Omelette", "Seaweed"], "Japanese_Breakfast.jpg")
    ]


# List of right and wrong ingredients to be used per level
Level1Ingredients = ["Eggs", "Sasuage", "Toast", "Bacon"]
Level2Ingredients = ["Bagel", "Cream Cheese", "Tortilla", "Hash Browns"]
Level3Ingredients = ["Eggs", "Cheese", "Milk", "Vegetables", "Pie Crust" "Tortilla", "Syrup", "Hash Browns", "Bacon", "Sasuage"]
# List of right and wrong ingredients to be used per level (More Difficult)
Level4Ingredients = ["Eggs", "Cheese", "Milk", "Vegetables", "Water", "Flour", "Salt", "Butter", "Torilla", "Syrup", "Hash Browns", "Bacon", "Sasuage", "Bagel", "Cream Cheese", "Seaweed", "Baked Beans"]
Level5Ingredients = ["Pancake Batter", "Bacon", "Maple Syrup", "Butter", "Eggs", "Cheese", "Toast", "Sausage"]
Level6Ingredients = ["Tortilla", "Scrambled Eggs", "Sausage", "Cheese", "Salsa", "Toast", "Pie Crust", "Bagel", "Panckae Batter", "Chocolate Chips"]
Level7Ingredients = ["Milk", "Eggs", "Flour", "Baking Powder", "Sugar", "Butter", "Chocolate Chips", "Syrup", "Bacon", "Green Onion", "Cheese", "Pie Crust", "Ginger", "Soy Sauce", "Vegetables", "Mushrooms"]
Level8Ingredients = ["Eggs", "Bacon", "Toast", "Jam", "Hash Browns", "Sausage", "Baked Beans", "Tomato", "Mushrooms", "Rice", "Pancake Batter", "Vegetables", "Milk", "Flour", "Soy Sauce", "Fermented Soybean", "Green Onion", "Pickled Vegetables"]
Level9Ingredients = ["Rice", "Water", "Fried Egg", "Ginger", "Green Onion", "Soy Sauce", "Miso Soup", "Pickled Vegetables", "Rolled Omelette", "Milk", "Flour", "Syrup"]
Level10Ingredients = ["Rice", "Miso Soup", "Grilled Fish", "Pickled Vegetables", "Fermented Soybean", "Rolled Omelette", "Seaweed", "Eggs", "Baking Powder", "Jam", "Cheese", "Muhsrooms", "Butter", "Milk"] 

#Levels would look like this
levels = [
    breakfasts[0], #Level 1
    breakfasts[1], #Level 2
    breakfasts[2], #Level 3
    
]
