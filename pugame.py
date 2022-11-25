import time
import pygame
import sys
pygame.init()

screen = pygame.display.set_mode([1000, 500])

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((0, 0, 0))
font_color = (255,255,255)

pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(250, 217, 500, 75), 5)
    
font_obj = pygame.font.Font("C:\Windows\Fonts\Bahnschrift.ttf",50)
text_obj = font_obj.render("Davids Äventyr",True,font_color)

font_obj2 = pygame.font.Font("C:\Windows\Fonts\Bahnschrift.ttf",25)
text_obj2 = font_obj2.render("Press space bar to continue",True,font_color)

while True:
    screen.blit(text_obj,(325,225))
    screen.blit(text_obj2,(325,450))

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


