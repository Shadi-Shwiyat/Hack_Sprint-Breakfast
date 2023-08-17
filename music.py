import pygame

pygame.mixer.init()

# Load sound effects
chop_items = pygame.mixer.Sound('sound/jump.wav')#chop
click_sound = pygame.mixer.Sound('sound/pickup.wav')#pop
sizzle_sound = pygame.mixer.Sound('sound/explosion.wav')
ding_sound = pygame.mixer.Sound('sound/explosion.wav')#dings when food is ready
humming_sound = pygame.mixer.Sound('sound/explosion.wav')#when food is cooking in the oven
boo_sound = pygame.mixer.Sound('sound/explosion.wav')#crowd boos
vomiting_sound = pygame.mixer.Sound('sound/explosion.wav')


# Load background music
menu_music = pygame.mixer.Sound('music/level1_music.ogg')#for menu and possibly intro if we get there
gameplay_music = pygame.mixer.Sound('music/level2_music.ogg')#for when playing the different levels
transition_music = pygame.mixer.Sound('music/transition.ogg')#when transitioning to the next level


def play_background_music(scenario):
    pygame.mixer.music.stop()  # Stop the current music
    if scenario == 'intro':
        menu_music.play(-1)
    elif scenario == 'gameplay':
        gameplay_music.play(-1)
    elif scenario == 'transition':
        transition_music.play(-1)


def play_sound_effect(scenario):
    pygame.mixer.music.stop()
    if scenario == 'select ingredient': # selecting ingredients
        click_sound.play()
    elif scenario == 'cooking food': # chopping food
        chop_items.play()
    elif scenario == 'cooking food': # sizzling food
        sizzle_sound.play()
    elif scenario == 'cooking food': # sound effect for when the food is done cooking
        ding_sound.play()
    elif scenario == 'cooking food': # for when the food is cooking in the oven
        humming_sound.play()
    elif scenario == 'failing level': # booing of the crowd for when you get a dish wrong
        boo_sound.play()
    elif scenario == 'failing level': # Wes vomiting for when you get a dish wrong
        vomiting_sound.play()
        
# play backgroung music
play_background_music('intro')
play_background_music('gameplay')
play_background_music('transition')
