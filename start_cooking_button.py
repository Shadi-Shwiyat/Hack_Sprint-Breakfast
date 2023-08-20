import pygame
from button import Button

# Creating an instance of the Button class
start_cooking_button = Button("Start Cooking!", (160, 100), 30)

ingredients_compared = False

def handle_start_cooking_button(screen, event, start_cooking_clicked, selected_ingredients, level_ingredients, result_message):
    global ingredients_compared
    
    start_cooking_button.update_rect()

    if start_cooking_clicked:
        correct_ingredients = level_ingredients.get("right_ingredients", [])
        
        if sorted(selected_ingredients) == sorted(correct_ingredients):
            print("Ingredients match!")
            result_message = "THERE IS A GOD!"
        else:
            print("Ingredients do not match..")
            result_message = "Fuck me in the ass!"
            
        ingredients_compared = True
        selected_ingredients = []
        start_cooking_clicked = False
    
    start_cooking_button.draw(screen)
    
    if ingredients_compared:
        result_font = pygame.font.Font(None, 36)
        result_surf = result_font.render(result_message, True, (0, 0, 0))
        result_rect = result_surf.get_rect(center=(screen.get_width() // 2, 650))
        screen.blit(result_surf, result_rect)
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_cooking_button.rect.collidepoint(event.pos):
            start_cooking_clicked = True
            selected_ingredients = []
    
    return start_cooking_clicked, selected_ingredients
