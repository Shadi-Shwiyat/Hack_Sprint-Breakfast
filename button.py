import pygame
from game import screen

# Defining Class Button
class Button:
    def __init__(self, text, pos, size, font_size=32):
        self.text = text
        self.pos = pos
        self.size = size
        self.font = pygame.font.Font(None, font_size)  # Using Pygame's default font
        self.selected = False

    def draw(self):
        outline_color = (14, 204, 52) if self.selected else (0, 0, 0)
        
        # Render the text with a transparent background
        text_surf = self.font.render(self.text, True, (0, 0, 0, 0))
        text_rect = text_surf.get_rect(center=(self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2))

        # Draw the rectangular outline around the button
        pygame.draw.rect(screen, outline_color, (*self.pos, *self.size), 2)  # Thickness 2 for the outline
        screen.blit(text_surf, text_rect)
