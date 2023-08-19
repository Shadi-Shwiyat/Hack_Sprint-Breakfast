import pygame
import time

class TextAnimation:
    def __init__(self, sentences, x, y, font, color, width, delay, erase_delay):
        # Initialize the TextAnimation object
        self.sentences = sentences   # List of sentences to display
        self.x = x                   # X-coordinate for display
        self.y = y                   # Y-coordinate for display
        self.font = font             # Font for the text
        self.color = color           # Color of the text
        self.width = width           # Maximum width of each line
        self.delay = delay           # Delay between displaying each character
        self.erase_delay = erase_delay  # Delay before erasing text
        self.finished = False        # Flag to indicate if animation is finished
        self.start_time = time.time()  # Time tracking for delays
        self.current_sentence_index = 0  # Index of the current sentence
        self.current_index = 0       # Index of the current character in sentence
        self.display_text = ""       # Text to display on the screen

    def update(self):
        # Update the text animation
        if not self.finished:
            current_time = time.time()
            if current_time - self.start_time >= self.delay:
                if self.current_index < len(self.sentences[self.current_sentence_index]):
                    # Add the next character to the display text
                    self.display_text += self.sentences[self.current_sentence_index][self.current_index]
                    self.current_index += 1
                    self.start_time = current_time
                else:
                    if current_time - self.start_time >= self.erase_delay:
                        if self.current_sentence_index < len(self.sentences) - 1:
                            # Move to the next sentence
                            self.current_sentence_index += 1
                            self.current_index = 0
                            self.display_text = ""
                            self.start_time = current_time
                        else:
                            # Animation is finished
                            self.finished = True

    def draw(self, screen):
        # Draw the text animation on the screen
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
