import random
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import BURGER, BURGER_TYPE

class Burger(PowerUp):
    def __init__(self):
        self.image = BURGER
        self.type = BURGER_TYPE
        super().__init__(self.image, self.type)
        self.rect.y = random.choice([350, 250, 120]) 
        