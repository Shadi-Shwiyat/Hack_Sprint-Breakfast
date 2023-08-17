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

#More Difficult Meals with detailed ingredients
    BreakfastMeal("Quiche",["Eggs", "Cheese", "Milk", "Vegetables", "Water", "Flour", "Salt", "Butter" ], meal_picture, meal_sound)")
    BreakfastMeal("Bacon Pancakes",["Pancake Batter", "Bacon", "Maple Syrup", "Butter"], meal_picture, meal_sound)")
    BreakfastMeal("Breakfast Burrito",["Tortilla", "Scrambled Eggs", "Sausage", "Cheese", "Salsa"], meal_picture, meal_sound)")
    BreakfastMeal("Chocolate Chip Waffles", ["Milk", "Eggs", "Flour", "Baking Powder", "Sugar", "Butter", "Chocolate Chips", "Syrup"], meal_picture, meal_sound)")
    BreakfastMeal("Full English Breakfast",["Eggs", "Bacon", "Toast", "Hash Browns", "Sausage", "Baked Beans", "Tomato", "Mushrooms"], meal_picture, meal_sound)")
    BreakfastMeal("Chinese Congee", ["Rice", "Water", "Fried Egg", "Ginger", "Green Onion", "Soy Sauce"], meal_picture, meal_sound)")
    BreakfastMeal("Japanese Breakfast", ["Rice", "Miso Soup", "Grilled Fish", "Pickled Vegetables", "Fermented Soybean", "Rolled Omelette", "Seaweed"], meal_picture, meal_sound)")
