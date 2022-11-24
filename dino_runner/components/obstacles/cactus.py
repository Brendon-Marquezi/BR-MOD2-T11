import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

Y_SMALL = 325
Y_LARGE = 300


class Cactus(Obstacle):
    def __init__(self):
        self.type = random.randint(0, 2)
        self.image = self.cactus_toggle()
        super().__init__(self.image, self.type)
        self.rect.y = self.y_toggle()
    
    def cactus_toggle(self):
        list = [SMALL_CACTUS, LARGE_CACTUS]
        image = list[random.randint(0, 1)]
        return image
        
    def y_toggle(self):
        if self.image == SMALL_CACTUS:
            y = Y_SMALL
        elif self.image == LARGE_CACTUS:
            y = Y_LARGE
        return y