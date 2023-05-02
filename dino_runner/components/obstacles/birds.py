import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.index = 0
        super().__init__(image, self.type)
        self.rect.y = 170
        self.rect.x = 600 
    
    
    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = SCREEN_WIDTH
        self.dino_rect.y = self.rect.y
  
        self.step_index += 1
        
 #random.randint[260, 220, 170]       