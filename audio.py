import pygame

class GameAudio:
    def __init__(self):
        pygame.mixer.init()
        self.load_sound_effects()
        self.load_background_music()

    def load_sound_effects(self):
        self.preping_food = pygame.mixer.Sound('audio/preping_food.mp3')
        self.click_sound = pygame.mixer.Sound('audio/select_sound.mp3')
        self.boo_sound = pygame.mixer.Sound('audio/boo_sound.mp3')
        self.vomiting_sound = pygame.mixer.Sound('audio/vomit_sound.mp3')
        #self.yay_sound = pygame.mixer.Sound('audio/yay.mp3')
        #self.next_level_sound = pygame.mixer.Sound('music/next_level_sound.mp3')

    def load_background_music(self):
        self.menu_music = pygame.mixer.Sound('audio/intro_music.mp3')

    def play_background_music(self, scenario):
        pygame.mixer.music.stop()
        if scenario == 'intro':
            self.menu_music.play(-1)
            self.menu_music.set_volume(0.2)

    def play_sound_effect(self, scenario):
        pygame.mixer.music.stop()
        if scenario == 'select button':
            self.click_sound.play(0)
            self.click_sound.set_volume(0.3)
        elif scenario == 'cooking food':
            self.preping_food.play(0)
            self.preping_food.set_volume(0.4)
        elif scenario == 'failing level':
            self.boo_sound.play(0)
            self.boo_sound.set_volume(0.4)
        #elif scenario == 'yay':
            #self.yay_sound.play(1)
            #self.yay_sound.set_volume(0.4)
        elif scenario == 'vomiting':
            self.vomiting_sound.play(1)
            self.vomiting_sound.set_volume(0.4)
        #elif scenario == 'yes':
            #self.next_level_sound.play(1) # DONT HAVE YET
            #self.next_level_sound.set_volume(0.4)
        

if __name__ == "__main__":
    pygame.init()
    audio = GameAudio()
    
    audio.play_background_music('intro')
    
    audio.play_sound_effect('select button')
    audio.play_sound_effect('cooking food')
    audio.play_sound_effect('failing level')
    audio.play_sound_effect('vomiting')
    #audio.play_sound_effect('yay')
    #audio.play_sound_effect('yes')
