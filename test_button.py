import pygame
import json

pygame.init()
screen = pygame.display.set_mode((1280, 720))

# Load data from the JSON file
with open('breakfast_meal.json', 'r') as file:
    data = json.load(file)

# Defining Class Button
class Button:
    def __init__(self, text, pos, font_size=26):
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)  # Using Pygame's default font
        self.selected = False
        self.hovered = False
        self.clicked = False
        self.clickcounter = 0

        # Calculating size of rectangle based on rendered text
        text_surf = self.font.render(self.text, True, (0, 0, 0, 0))
        text_rect = text_surf.get_rect()
        self.size = (text_rect.width + 20, text_rect.height + 20)  # Adding some padding for rectangle

    def draw(self):
        outline_color = (14, 204, 52) if self.selected else (0, 0, 0)
        
        # Render the text with a transparent background
        text_surf = self.font.render(self.text, True, (0, 0, 0, 0))
        text_rect = text_surf.get_rect(center=(self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2))

        # Draw the rectangular outline around the button
        pygame.draw.rect(screen, outline_color, (*self.pos, *self.size), 2)  # Thickness 2 for the outline
        screen.blit(text_surf, text_rect)

    def handle_events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.pos[0] < event.pos[0] < self.pos[0] + self.size[0] and \
               self.pos[1] < event.pos[1] < self.pos[1] + self.size[1]:
                self.hovered = True
            else:
                self.hovered = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.pos[0] < event.pos[0] < self.pos[0] + self.size[0] and \
               self.pos[1] < event.pos[1] < self.pos[1] + self.size[1]:
                self.clicked = True
                self.selected = not self.selected
                self.clickcounter += 1
                print(f"I am clicked ({self.clickcounter} times)")
                print(f"Selected = {self.selected}")
            else:
                self.clicked = False

# Initialize Buttons
buttons = []

def create_buttons(level):
    ingredients = data['breakfasts'][level]['all_ingredients']
    button_y = 100
    for ingredient in ingredients:
        buttons.append(Button(ingredient, (200, button_y)))
        button_y += 50

current_level = 0
create_buttons(current_level)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            button.handle_events(event)

    screen.fill((255, 255, 255))

    for button in buttons:
        button.draw()

    pygame.display.flip()

pygame.quit()