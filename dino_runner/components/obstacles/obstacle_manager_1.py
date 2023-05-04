import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS
from dino_runner.components.obstacles.birds import Bird

class ObstacleManager:
    def __init__(self):
        self.POS_Y = 170
        self.POS_X = 600
        self.step_index = 0
        self.obstacles = []
       
        
    def update(self, game_speed, game):
        
        if len(self.obstacles) == 0:

            type = random.randint(0,2)

            if type == 0:
                self.obstacles.append(Bird(BIRD))
                
            elif type == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif type == 2:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            
    
            
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                game.heart_manager.reduce_heart()

                if not game.player.shield and game.heart_manager.heart_count < 1:
                    pygame.time.delay(300)
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
       

## Explicacion

#  mejoras, implementaciones...

#  class 5 ejercices


