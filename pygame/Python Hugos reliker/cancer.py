import pygame
import sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()



pygame.init()
Clock = pygame.time.Clock()

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("Blue.png")
pygame.mouse.set_visible(False)

crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(background,(0,0))
    crosshair_group.draw(screen)
    crosshair_group.update()
    Clock.tick(60)



























