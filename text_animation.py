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
FONT = pygame.font.Font(None, 36)

# Define table dimensions
table_x = 100
table_y = screen_height - 150
table_width = screen_width - 2 * table_x
table_height = 100

# Initialize variables
text_to_display = "Hello! I am Chef Wes and I am going to teach you how to make a delicious breakfast!"
text_index = 0
text_display_duration = 5 * 1000  # 5 seconds in milliseconds
text_display_start_time = pygame.time.get_ticks()



second_text = "Today we are going to pick the right ingredients for Eggs and Sausage."
second_text_index = 0
second_text_display_duration = 5 * 1000  # 5 seconds in milliseconds
text_display_start_time = pygame.time.get_ticks()
second_text_display_start_time = text_display_start_time + text_display_duration

running = True
while running:
    screen.fill(WHITE)
    
    current_time = pygame.time.get_ticks()
    
    if current_time < text_display_start_time + text_display_duration:
        displayed_text = text_to_display[:text_index]
        text_index = (current_time * len(text_to_display)) // text_display_duration
    elif text_display_start_time + text_display_duration <= current_time < second_text_display_start_time + second_text_display_duration:
        displayed_text = second_text[:second_text_index]
        second_text_index = (current_time * len(second_text)) // second_text_display_duration
    else:
        displayed_text = ""
        text_index = 0
        text_display_start_time = current_time
        second_text_index = 0
        second_text_display_start_time = text_display_start_time + text_display_duration
    
    # Draw table
    pygame.draw.rect(screen, BLACK, (table_x, table_y, table_width, table_height), 2)
    
    lines = []
    current_line = ""
    words = displayed_text.split()
    for word in words:
        test_line = current_line + " " + word if current_line else word
        test_text = FONT.render(test_line, True, BLACK)
        if test_text.get_width() <= table_width - 20:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    y_position = table_y + 10
    for line in lines:
        text_surface = FONT.render(line, True, BLACK)
        text_rect = text_surface.get_rect(midleft=(table_x + 10, y_position))
        screen.blit(text_surface, text_rect)
        y_position += text_surface.get_height() + 5
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.Clock().tick(60)

pygame.quit()
