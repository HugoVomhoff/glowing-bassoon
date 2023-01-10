import pygame
pygame.init()   
 
from Game_State import game_state

pygame.display.set_caption("Andreas Äventyr")
pygame.mouse.set_visible(True) 

Clock = pygame.time.Clock()

while True:
    game_state.state_manager()
    pygame.event.clear()
    Clock.tick(60)


