import random
import pygame
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.burger import Burger

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0
        

    def generate_power_ups(self, points):
        self.points = points

        if len(self.power_ups) == 0:
            type = random.randint(0,2)
            if type == 0:
                if self.when_appears == self.points:
                    print("generating power up shield")
                    self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                    self.power_ups.append(Shield())
        
            if type == 1:
                if self.when_appears == self.points:
                    print("generating power up hammer")
                    self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                    self.power_ups.append(Hammer())
            if type == 2:
                if self.when_appears == self.points:
                    print("generating power up hammer")
                    self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                    self.power_ups.append(Burger())
                    
                    

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            
            if player.dino_rect.colliderect(power_up.rect):
                player.shield = True
                player.type = power_up.type

                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = start_time + (time_random * 1000)

                self.power_ups.remove(power_up)
            #elif player.dino_rect.colliderect(power_up.rect):
                
                

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)