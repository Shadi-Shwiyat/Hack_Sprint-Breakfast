class BreakfastMeal:
    def __init__(self, name, ingredients, meal_picture, meal_sound):
        self.name = name
        self.ingredients = ingredients = ingredients
        self.meal_picture = meal_picture
        self.meal_sound = meal_sound
    


#Breakfast Meals to be used per level
    
breakfasts = [
    BreakfastMeal("Eggs and Sasauge",["Eggs", "Sasuage"], meal_picture, meal_sound)
    BreakfastMeal("Bagel and Cream Cheese",["Bagel", "Cream Cheese"], meal_picture, meal_sound)
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Pie Crust"], meal_picture, meal_sound)
#Breakfast Meals to be used per level (More Difficult)
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Water", "Flour", "Salt", "Butter" ], meal_picture, meal_sound)")
    BreakfastMeal("Bacon Pancakes",["Pancake Batter", "Bacon", "Maple Syrup", "Butter"], meal_picture, meal_sound)")
    BreakfastMeal("Breakfast Burrito",["Tortilla", "Scrambled Eggs", "Sausage", "Cheese", "Salsa"], meal_picture, meal_sound)")
    BreakfastMeal("Chocolate Chip Waffles", ["Milk", "Eggs", "Flour", "Baking Powder", "Sugar", "Butter", "Chocolate Chips", "Syrup"], meal_picture, meal_sound)")
    BreakfastMeal("Full English Breakfast",["Eggs", "Bacon", "Toast", "Jam" "Hash Browns", "Sausage", "Baked Beans", "Tomato", "Mushrooms"], meal_picture, meal_sound)")
    BreakfastMeal("Chinese Congee", ["Rice", "Water", "Fried Egg", "Ginger", "Green Onion", "Soy Sauce"], meal_picture, meal_sound)")
    BreakfastMeal("Japanese Breakfast", ["Rice", "Miso Soup", "Grilled Fish", "Pickled Vegetables", "Fermented Soybean", "Rolled Omelette", "Seaweed"], meal_picture, meal_sound)")
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
