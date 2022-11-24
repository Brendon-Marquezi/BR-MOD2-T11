from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        super().__init__(BIRD, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index > 9:
            self.index = 0

        screen.blit(self.image[self.index // 5], self.rect) # "0" to "9" integer division "//"" by "5" gives between 0 and 1
        self.index += 1