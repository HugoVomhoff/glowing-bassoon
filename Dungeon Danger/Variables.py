# Sätter hur fönstret ska se ut och fixar fullsceen i pygame
import pygame
skärm = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Sätter skärmens storlek i variabler
screen_Width, screen_Height = pygame.display.get_surface().get_size()
scale = screen_Width / 1920

# ritar en semitransparent rektangel
def draw_rect_alpha(surface, color, rect):
            shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
            surface.blit(shape_surf, rect)

# sätter alla fonter

Font1_30 = pygame.font.Font("Fonts/Font1.TTF",int(30*scale))  
Font1_40 = pygame.font.Font("Fonts/Font1.TTF",int(40*scale))  
Font1_70 = pygame.font.Font("Fonts/Font1.TTF",int(70*scale))
Font1_100 = pygame.font.Font("Fonts/Font1.TTF", int(100 *scale))
Font1_120 = pygame.font.Font("Fonts/Font1.TTF",int(120*scale))

Font6_25 = pygame.font.Font("Fonts/Font6.ttf", int(25 *scale))
Font6_35 = pygame.font.Font("Fonts/Font6.ttf", int(35 *scale)) 
Font6_55 = pygame.font.Font("Fonts/Font6.ttf", int(55 *scale))
Font6_70 = pygame.font.Font("Fonts/Font6.ttf", int(70 *scale))
Font6_80 = pygame.font.Font("Fonts/Font6.ttf", int(80 *scale))
 
fonts = [Font1_30, Font1_40, Font1_70, Font1_100, Font1_120, Font6_25, Font6_35, Font6_55, Font6_70, Font6_80]

# Sätter alla scenbakgrunder och detaljer

Background = pygame.transform.scale(pygame.image.load("Bilder/Scener/Room1 v2 - oilpaint.png"), (screen_Width, screen_Height))
Background1 = pygame.transform.scale(pygame.image.load("Bilder/Scener/Shop - oilpaint.png"), (screen_Width, screen_Height))
Background2 = pygame.transform.scale(pygame.image.load("Bilder/Scener/Kista - stängd - oilpaint.png"), (screen_Width, screen_Height))
Background3 = pygame.transform.scale(pygame.image.load("Bilder/Scener/Kista - öppen - oilpaint.png"), (screen_Width, screen_Height))
Background4 = pygame.transform.scale(pygame.image.load("Bilder/Scener/Tre dörrar v3- oilpaint.png"), (screen_Width, screen_Height))
Background5 = pygame.transform.scale(pygame.image.load("Bilder/Scener/spindel - oilpaint.png"), (screen_Width, screen_Height))
Background6 = pygame.transform.scale(pygame.image.load("Bilder/Scener/spindel du dog - oilpaint.png"), (screen_Width, screen_Height))
Background7 = pygame.transform.scale(pygame.image.load("Bilder/Scener/spindel - död - oilpaint.png"), (screen_Width, screen_Height))
Background8 = pygame.transform.scale(pygame.image.load("Bilder/Scener/spindel - tie - oilpaint.png"), (screen_Width, screen_Height))
Background9 = pygame.transform.scale(pygame.image.load("Bilder/Scener/Trap1 - oilpaint.png"), (screen_Width, screen_Height))
Background10= pygame.transform.scale(pygame.image.load("Bilder/Scener/Trap1 - dodge - oilpaint.png"), (screen_Width, screen_Height))
Background11 = pygame.transform.scale(pygame.image.load("Bilder/Scener/Trap1 du dog - oilpaint.png"), (screen_Width, screen_Height))
Character = pygame.image.load("Bilder/Scener/Character - oilpaint.png")
Character1 = pygame.transform.scale(Character, ((Character.get_width() * scale * 0.9), Character.get_height() * scale * 0.9))
Gold = pygame.image.load("Bilder/Scener/GULD.png")
Gold1 = pygame.transform.scale(Gold, ((Gold.get_width() * scale), Gold.get_height()*scale))

Scene_details = [Background, Background1, Background2, Background3, Background4, Background5, Background6, Background7, Background8, Background9, Background10, Background11, Character, Character1, Gold, Gold1]