import pygame


class WriteOnScreen:
    def __init__(self, screen):
        self.font_style = "freesansbold.ttf"
        self.screen = screen

    def write(self, text, font_size, pos_x, pos_y):
        font = pygame.font.Font(self.font_style, font_size)
        text = font.render(text, True , (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (pos_x, pos_y)
        self.screen.blit(text, text_rect)
        
        