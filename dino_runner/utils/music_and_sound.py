import pygame


def Music(music, volume = 0.3):
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

def Sound(sound, volume = 0.3):
    sound = pygame.mixer.Sound(sound)
    sound.set_volume(volume)
    sound.play()