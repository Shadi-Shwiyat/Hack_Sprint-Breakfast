import os
import pygame
import json
from sys import exit
import time

# Fixing audio issue
os.environ['SDL_AUDIODRIVER'] = 'dsp'

# Importing Json dictionary of meals and ingredients
with open('breakfast_meal.json') as json_file:
    data = json.load(json_file)

# Initializing pygame and window size
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Setting title of window
pygame.display.set_caption("Rise and Dine: Wes's Cozy Kitchen")

# Set up font
font = pygame.font.Font(None, 24)


# Start menu stuff below
##########################################################################################################
# rendering a text written in 
# this font 
# Background Image
background = pygame.image.load("images/kitchen_background.jpeg")
background = pygame.transform.scale(background, (1480, 900))
screen.blit(background, (-110, -50))

# Wes Image
delicioso = pygame.image.load("images/delicioso.png")
delicioso = pygame.transform.scale(delicioso, (690, 830))
screen.blit(delicioso, (530, 45))

# Menu Buttons
text = font.render('Start' , True , (255, 255, 255)) 
text = font.render('Quit' , True , (255, 255, 255)) 

while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if screen_width/2 <= mouse[0] <= screen_width/2+140 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
                pygame.quit() 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if screen_width/2 <= mouse[0] <= screen_width/2+140 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
        pygame.draw.rect(screen,(100, 100, 100),[screen_width/2,screen_height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,(55, 171, 95),[screen_width/2,screen_height/2,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (screen_width/2+50,screen_height/2)) 
      
    # updates the frames of the game 
    pygame.display.update() 

########################################################################################################

# Update the display
pygame.display.flip()

# Limit frame rate to 60 FPS
clock.tick(60)

pygame.quit()
exit()
