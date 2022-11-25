import pygame

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


pygame.init()
screen = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()

Open_Chest = pygame.image.load("renders/Färdigt/Kista - öppen - oilpaint.png")
background_Width = Open_Chest.get_width() 
background_Height = Open_Chest.get_height() 
open_Chest = pygame.transform.scale(Open_Chest, (background_Width, background_Height)) 
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(Open_Chest, (0, 0))
    draw_rect_alpha(screen, (0, 0, 0, 100), (55, 90, 140, 140,))

    pygame.display.flip()

pygame.quit()
exit()
