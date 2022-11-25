import pygame
import sys
import random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()   
        self.gunshot = pygame.mixer.Sound("Game_bullet.mp3")  
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self,picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect() 
        self.rect.center = [pos_x, pos_y]    

class GameState():
    def __init__(self):
        self.state = 'intro'
    
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

        pygame.display.flip()
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(ready_text,(screen_width/2-115,screen_height/2-33))
        crosshair_group.draw(screen)
        crosshair_group.update()
        
        pygame.display.flip()
    
    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()

        pygame.display.flip()
        screen.blit(background,(0,0))
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        screen.fill((0,0,0))
        pygame.display.flip()
    
    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()
    

pygame.init()
Clock = pygame.time.Clock()
game_state = GameState()

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("Blue.png")
ready_text = pygame.image.load("text_ready.png")
pygame.mouse.set_visible(False)

crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target
target_group = pygame.sprite.Group()
for target in range (50):
    new_target = Target("attack_1.png",random.randrange(0,screen_width),random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    game_state.state_manager()
    Clock.tick(60)




























