# Importerar och initializar pygame

import pygame
pygame.init()   
 
# Hämtar scenhanteraren som heter gamestate från textfilen som också heter gamestate
from Game_State import game_state

# Sätter fönsternanet till spelets namn och gör så att muspekaren är synlig
pygame.display.set_caption("Dungeon Danger")
pygame.mouse.set_visible(True) 

# Fixar tick för spelet
Clock = pygame.time.Clock()

# Sätter tickhastigheten och startar igång första scenen
while True:
    game_state.state_manager()
    pygame.display.flip()            
    Clock.tick(60)


