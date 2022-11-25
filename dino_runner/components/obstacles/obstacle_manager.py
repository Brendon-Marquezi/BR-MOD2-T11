import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SOUND_DEATH, SOUND_END, MUSIC_MENU, SOUND_IMPACT
from dino_runner.utils.music_and_sound import Music, Sound


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            rand = random.randint(0, 1)
            if rand == 0:
                self.obstacles.append(Cactus())
            elif rand == 1:
                self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    Sound(SOUND_DEATH, 0.1)
                    pygame.time.delay(600)
                    game.playing = False
                    game.death_count += 1
                    pygame.mixer.music.stop()
                    Sound(SOUND_END, 0.1)
                    pygame.time.delay(500)
                    Music(MUSIC_MENU)
                    game.update_max_score()
                    game.reset_score()
                    break
                elif game.player.type == 'hammer':
                    Sound(SOUND_IMPACT, 0.1)
                    self.obstacles.remove(obstacle)          

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        