import pygame
import sys
import random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        #self.gunshot = pygame.mixer.Sound("boom.wav")
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    #def shoot(self):
        #self.gunshot.play()
        #pygame.sprite.spritecollide(crosshair,target_sprites, True)

class Target(pygame.sprite.Sprite):
    def __int__(self,picture_path,pos_x,pos_y):
        super().__init__()
        self.iamge = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
class GameState():
    def __init__(self):
        self.state= 'main_game'

    def main_game(slf):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
                
                       
        screen.blit(background,(0,0))
        target_sprites.draw(screen)
        player_group.draw(screen)
        player_group.update()

        pygame.display.flip()


pygame.init()
clock = pygame.time.Clock()
game_state = GameState()



screen_w = 1000
screen_h = 500
screen  = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("sprites")
background = pygame.image.load("Blue.png")
pygame.mouse.set_visible(False)

crosshair = Crosshair(200,200,"crosshair.png")
player_group = pygame.sprite.Group()
player_group.add(crosshair)

target_sprites = pygame.sprite.Group()
for target in range(50):
    new_target = Target("attack_10.png", random.randrange(0, screen_w), random.randrange(0, screen_h))
    target_sprites.add(new_target)

while True:
    game_state.main_game()
    clock.tick(60)

    