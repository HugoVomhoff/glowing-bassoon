import pygame

from Game_State import game_state

pygame.init()

Clock = pygame.time.Clock()

while True:
    game_state.state_manager()
    pygame.event.clear()   
    Clock.tick(30)
