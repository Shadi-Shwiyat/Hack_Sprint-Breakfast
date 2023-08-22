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
        self.wes_hooray = pygame.mixer.Sound('audio/wes_hooray.mp3')
        self.hooray_kids = pygame.mixer.Sound('audio/hooray_kids.mp3')
        self.yes_sound = pygame.mixer.Sound('audio/yes.mp3')

    def load_background_music(self):
        self.menu_music = pygame.mixer.Sound('audio/intro_music.mp3')
        self.credit_music = pygame.mixer.Sound('audio/credit_music.mp3')

    def play_background_music(self, scenario):
        pygame.mixer.music.stop()
        if scenario == 'intro':
            self.menu_music.play(-1)
            self.menu_music.set_volume(0.1)
            self.intro_playing = True
        elif scenario == 'credits':
            self.credit_music.play(0)
            self.credit_music.set_volume(0.2)
            self.credit_playing = True

    def play_sound_effect(self, scenario, delay_ms=0):
        pygame.mixer.music.stop()
        if scenario == 'select button':
            self.click_sound.play(0)
            self.click_sound.set_volume(0.3)
        elif scenario == 'cooking food':
            self.preping_food.play(0)
            self.preping_food.set_volume(0.8)
        elif scenario == 'failing level':
            if delay_ms > 0:
                pygame.time.delay(delay_ms)
            self.boo_sound.play(0)
            self.boo_sound.set_volume(0.3)
        elif scenario == 'level success':
            self.wes_hooray.play(0)
            self.wes_hooray.set_volume(0.5)
            self.hooray_kids.play(0)
            self.hooray_kids.set_volume(0.4)
        elif scenario == 'level success 2':
            self.yes_sound.play(0)
            self.yes_sound.set_volume(0.4)
            #pygame.time.delay(2500)
        elif scenario == 'vomiting':
            if delay_ms > 0:
                pygame.time.delay(delay_ms)
            self.vomiting_sound.play(1)
            self.vomiting_sound.set_volume(0.3)
            #pygame.time.delay(3000)
        #elif scenario == 'yes':
            #self.next_level_sound.play(1) # DONT HAVE YET
            #self.next_level_sound.set_volume(0.4)

    def stop_music(self):
        self.menu_music.stop()

if __name__ == "__main__":
    pygame.init()
    audio = GameAudio()
    
    audio.play_background_music('intro')
    audio.play_background_music('credits')
    
    audio.play_sound_effect('select button')
    audio.play_sound_effect('cooking food')
    audio.play_sound_effect('failing level')
    audio.play_sound_effect('vomiting')
    audio.play_sound_effect('hooray')
