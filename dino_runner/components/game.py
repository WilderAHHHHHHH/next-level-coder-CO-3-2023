import pygame
from dino_runner.components.music.music import Music
from dino_runner.components.obstacles.clouds.clouds import Cloud
from dino_runner.components.player_hearts.heart_manager import HeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import (
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS,
    FONT_ARIAL,
    
    
    )

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager_1 import ObstacleManager



# from dino_runner.components.music.music import Music

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #ancho: 1100, alto: 600
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20

        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        
        self.player = Dinosaur()
        self.obstacle_manager_1 = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = HeartManager()
        self.cloud = Cloud()
        self.music = Music()

    def increase_score(self):
        self.points += 1
        if self.points % 200 == 0:
            self.game_speed += 1

        self.player.check_invincibility()
        self.player.check_hammer_use()
    
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #self.musica.play()
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.music.update()
        self.cloud.update(self.game_speed) # ----------
        self.obstacle_manager_1.update(self.game_speed, self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.increase_score()
       
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((232, 232, 232 ))
        self.draw_background()
        self.cloud.draw(self.screen) #------
        self.player.draw(self.screen)
        self.obstacle_manager_1.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.heart_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
 
    def draw_score(self):
        font = pygame.font.Font(FONT_ARIAL, 30)
        surface = font.render((f'Score: {self.points}'  ), True, (0, 0, 0))
        rect = surface.get_rect()
        rect.x = 980
        rect.y = 10
        self.screen.blit(surface, rect)

    def change_background(self):
        
        if not self.points == 500 :
            self.screen.fill((114, 113, 113)) 
            #self.screen.fill((225, 225, 225)) 
        else:
            self.screen.fill((114, 113, 113)) 
            
    def show_clouds(Self):
         pass
# 

        #self.change_background()