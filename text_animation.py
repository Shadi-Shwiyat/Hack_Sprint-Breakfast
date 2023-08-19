import pygame
import time
import json

# Load data from the JSON file
with open('breakfast_meal.json', 'r') as file:
    data = json.load(file)

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
            text_rect = text_surface.get_rect(topleft=(self.x - self.width // 2, self.y + y_offset))
            text_rect.width = self.width
            screen.blit(text_surface, text_rect)
            y_offset += text_rect.height  # Adjust y offset for the next line

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakfast Meal Text Animation")

# Set up font
font = pygame.font.Font(None, 24)

# Initialize TextAnimation
current_level = 0
current_sentence_index = 0
animation_data = data['breakfasts'][current_level]['wes_says']
text_animation = TextAnimation(animation_data, screen_width // 2, 50, font, (0, 0, 0), 250, 0.05, 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Update and draw text animation
    text_animation.update()
    text_animation.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
