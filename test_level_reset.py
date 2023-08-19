import pygame
import time
import json

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakfast Cooking Game")

# Define colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FONT = pygame.font.Font('freesansbold.ttf', 20)

# Load JSON data
with open('breakfast_meal.json') as json_file:
    data = json.load(json_file)
breakfasts = data['breakfasts']

# TextAnimation class
class TextAnimation:
    def __init__(self, sentences, x, y, font, color, width, delay, erase_delay):
        self.sentences = sentences
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.width = width
        self.delay = delay
        self.erase_delay = erase_delay
        self.finished = False
        self.start_time = time.time()
        self.current_sentence_index = 0
        self.current_index = 0
        self.display_text = ""

    def update(self):
        if not self.finished:
            current_time = time.time()
            if current_time - self.start_time >= self.delay:
                if self.current_index < len(self.sentences[self.current_sentence_index]):
                    self.display_text += self.sentences[self.current_sentence_index][self.current_index]
                    self.current_index += 1
                    self.start_time = current_time
                else:
                    if current_time - self.start_time >= self.erase_delay:
                        if self.current_sentence_index < len(self.sentences) - 1:
                            self.current_sentence_index += 1
                            self.current_index = 0
                            self.display_text = ""
                            self.start_time = current_time
                        else:
                            self.finished = True

    def draw(self, screen):
        words = self.display_text.split()
        lines = []
        current_line = ""
        
        for word in words:
            test_line = f"{current_line} {word}".strip()
            test_width, _ = self.font.size(test_line)
            
            if test_width <= self.width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        
        lines.append(current_line)
        
        y_offset = 0
        for line in lines:
            text_surface = self.font.render(line, True, self.color)
            text_rect = text_surface.get_rect(topleft=(self.x, self.y + y_offset))
            text_rect.width = self.width
            screen.blit(text_surface, text_rect)
            y_offset += text_rect.height  # Adjust y offset for the next line

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, highlight_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.highlight_color = highlight_color
        self.text = text
        self.action = action
        self.highlighted = False

    def draw(self, screen):
        if self.highlighted:
            pygame.draw.rect(screen, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text_surface = FONT.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

# Create TextAnimation instances for each level
level1_sentences = [
    "Hello! I am Chef Wes!",
    "This is my kitchen where I'd like to cook some breakfast with you.",
    "Lets get the ingredients ready.",
    "We will be making Eggs and Sasuage.",
    "Pick the right ingredients below for Eggs and Sasuage."
]

level2_sentences = [
    "Awesome! You've completed Level 1.",
    "Now let's dive into more advanced recipes in Level 2."
]

level1_animation = TextAnimation(level1_sentences, 275, 100, FONT, BLACK, 250, 0.1, 3)
level2_animation = TextAnimation(level2_sentences, 275, 100, FONT, BLACK, 250, 0.1, 3)

# Set the active animation (change this based on the level)
active_animation = level1_animation

# Create ingredient buttons
def create_ingredient_buttons(ingredients):
    buttons = []
    button_x = 50
    button_y = screen_height - 100
    button_width = 100
    button_height = 40
    for ingredient in ingredients:
        button = Button(button_x, button_y, button_width, button_height, ingredient, BLACK, GREEN)
        buttons.append(button)
        button_x += button_width + 10
    return buttons

current_level = 1
current_level_data = breakfasts[current_level - 1]
current_level_right_ingredients = current_level_data['right_ingredients']
current_level_all_ingredients = current_level_data['all_ingredients']
selected_ingredients = []
ingredient_buttons = create_ingredient_buttons(current_level_all_ingredients)

# Create "Cook this!" button
cook_button = Button(screen_width - 150, screen_height - 50, 100, 40, "Cook this!", BLACK, GREEN)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse hover and click events
        if event.type == pygame.MOUSEMOTION:
            for button in ingredient_buttons + [cook_button]:
                if button.rect.collidepoint(event.pos):
                    button.highlighted = True
                else:
                    button.highlighted = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # Check if an ingredient button was clicked
            for button in ingredient_buttons:
                if button.rect.collidepoint(x, y):
                    ingredient = button.text
                    if ingredient in selected_ingredients:
                        selected_ingredients.remove(ingredient)
                    else:
                        selected_ingredients.append(ingredient)

            # Check if "Cook this!" button was clicked
            if cook_button.rect.collidepoint(x, y):
                if set(selected_ingredients) == set(current_level_right_ingredients):
                    # Ingredients are correct, move to the next level
                    current_level += 1
                    if current_level > len(breakfasts):
                        print("Congratulations! You have completed all levels!")
                        running = False
                    else:
                        # Load data for the new level
                        current_level_data = breakfasts[current_level - 1]
                        current_level_right_ingredients = current_level_data['right_ingredients']
                        current_level_all_ingredients = current_level_data['all_ingredients']
                        selected_ingredients = []  # Clear selected ingredients for the new level
                        active_animation = level2_animation if current_level == 2 else level1_animation

    screen.fill(WHITE)

    # Update and draw the active text animation
    active_animation.update()
    active_animation.draw(screen)

    # Draw ingredient buttons and "Cook this!" button
    for button in ingredient_buttons + [cook_button]:
        button.draw(screen)

    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()

