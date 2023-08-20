import pygame
from button import Button

def start_cooking_button(screen):
    start_cooking_button = Button("Start/nCooking", (100, 200), (200, 50), font_size=24)
    start_cooking_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_cooking_button.rect.collidepoint(event.pos):
                return True # indicates the button was clicked
            
    return False # indicates the button was not clicked