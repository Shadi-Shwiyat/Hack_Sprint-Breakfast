import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text Animation")

# Define colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font('freesansbold.ttf', 20)

# Define text box dimensions
text_box_x = 50
text_box_y = 50
text_box_width = 300
text_box_height = 150

# Initialize variables
texts = [
    "Hello! I am Chef Wes! Today we are going to learn to cook a few things!",
    "Today we will be cooking Eggs and Sausage! Let's select the right ingredients to get started!"
]
current_text_index = 0
text_index = 0
text_display_duration = 4 * 1000  # 4 seconds in milliseconds
text_display_start_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(WHITE)
    
    current_time = pygame.time.get_ticks()
    
    if current_time < text_display_start_time + text_display_duration:
        displayed_text = texts[current_text_index][:text_index]
        text_index = (current_time * len(texts[current_text_index])) // text_display_duration
    elif current_text_index < len(texts) - 1:
        current_text_index += 1
        text_display_start_time = current_time
        text_index = 0
    else:
        displayed_text = ""
    
    # Draw text box
    pygame.draw.rect(screen, BLACK, (text_box_x, text_box_y, text_box_width, text_box_height), 2)
    
    lines = displayed_text.split('\n')
    y_position = text_box_y + 10
    for line in lines:
        words = line.split()
        current_line = ""
        for word in words:
            test_line = current_line + " " + word if current_line else word
            test_text = FONT.render(test_line, True, BLACK)
            if test_text.get_width() <= text_box_width - 20:
                current_line = test_line
            else:
                text_surface = FONT.render(current_line, True, BLACK)
                text_rect = text_surface.get_rect(midtop=(screen_width // 2, y_position))
                screen.blit(text_surface, text_rect)
                y_position += text_surface.get_height() + 5
                current_line = word
        if current_line:
            text_surface = FONT.render(current_line, True, BLACK)
            text_rect = text_surface.get_rect(midtop=(screen_width // 2, y_position))
            screen.blit(text_surface, text_rect)
            y_position += text_surface.get_height() + 5
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_text_index >= len(texts) and current_time >= text_display_start_time + text_display_duration:
        running = False

    pygame.time.Clock().tick(60)

pygame.quit()
