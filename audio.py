import pygame

class GameAudio:
    def __init__(self):
        pygame.mixer.init()
        self.load_sound_effects()
        self.load_background_music()

    def load_sound_effects(self):
        self.preping_food = pygame.mixer.Sound('music/preping_food.mp3')
        self.click_sound = pygame.mixer.Sound('music/select_sound.mp3')
        self.boo_sound = pygame.mixer.Sound('sound/boo_sound.mp3')
        self.vomiting_sound = pygame.mixer.Sound('sound/vomit_sound.mp3')
        self.next_level_sound = pygame.mixer.Sound('sound/next_level_sound.mp3')

    def load_background_music(self):
        self.menu_music = pygame.mixer.Sound('music/intro_music.mp3')
        self.gameplay_music = pygame.mixer.Sound('music/gameplay_music.mp3')

    def play_background_music(self, scenario):
        pygame.mixer.music.stop()
        if scenario == 'intro':
            self.menu_music.play(-1)
        elif scenario == 'gameplay':
            self.gameplay_music.play(-1)

    def play_sound_effect(self, scenario):
        pygame.mixer.music.stop()
        if scenario == 'select select button':
            self.click_sound.play()
        elif scenario == 'cooking food':
            self.preping_food.play()
        elif scenario == 'failing level':
            self.boo_sound.play()
        elif scenario == 'vomiting':
            self.vomiting_sound.play()
        elif scenario == 'next level':
            self.next_level_sound.play() # DONT HAVE YET

if __name__ == "__main__":
    pygame.init()
    audio = GameAudio()
    
    audio.play_background_music('intro')
    audio.play_background_music('gameplay')
    
    audio.play_sound_effect('select button')
    audio.play_sound_effect('cooking food')
    audio.play_sound_effect('failing level')
    audio.play_sound_effect('vomiting')
