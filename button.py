import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

# Defining Class Button
class Button:
    def __init__(self, text, pos, font_size=26):
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)  # Using Pygame's default font
        self.selected = False

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
