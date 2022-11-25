import random
import pygame
import sys
import time
import math

pygame.init()
Clock = pygame.time.Clock()

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Davids Äventyr")
pygame.mouse.set_visible(True)
denna = 1

class GameState():
    def __init__(self):
        self.Titlecard()
    
    def Titlecard(self):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
                bakgrund = pygame.image.load("Bilder/hahha.jpg")
                
                
                #bakgrund = pygame.image.load("Bilder/lika.png")
                
                while True:
                    for x in range (0, (3800-screen_width)):
                        global denna
                        if denna == 0:
                            screen.blit(bakgrund, ((3800 - screen_width)+ x, 0))
                            time.sleep(0.01)
                            pygame.display.flip()
                        if denna == 1:
                            screen.blit(bakgrund, (-x, 0))
                            time.sleep(0.01)
                            pygame.display.flip()
                    denna = not denna   
                
            
            """
            for x in range(1, 1000):
                
                screen.blit(bakgrund, (x, y))
                time.sleep(0.5)

            pygame.display.flip()
            """

game_state = GameState()

while True:
    game_state.Titlecard()
    Clock.tick(60)   


