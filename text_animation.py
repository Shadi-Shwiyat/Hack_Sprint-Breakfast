import pygame
import time

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

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text Animation Class Example")

# Define colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font('freesansbold.ttf', 20)

# Define sentences for each level
level1_sentences = [
    "Hello! I am Chef Wes!",
    "This is my kitchen where I'd like to cook some breakfast with you.",
    "Lets get the ingredients ready.",
    "We will be making Eggs and Sasuage.",
    "Pick the right ingredients below for Eggs and Sasuage."
]

level2_sentences = [
    "Awesome! You've completed Level 1.",
    "BLAH BLAH BLAH"
]

# Create TextAnimation instances for each level
level1_animation = TextAnimation(level1_sentences, 275, 100, FONT, BLACK, 250, 0.1, 3)
level2_animation = TextAnimation(level2_sentences, 275, 100, FONT, BLACK, 250, 0.1, 3)

# Set the active animation (change this based on the level)
active_animation = level1_animation

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Update and draw the active text animation
    active_animation.update()
    active_animation.draw(screen)

    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()
