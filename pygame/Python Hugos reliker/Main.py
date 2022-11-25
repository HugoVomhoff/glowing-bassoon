import pygame
import sys
import button

class Frogg(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('1_frog.png'))
		self.sprites.append(pygame.image.load('2_frog.png'))
		self.sprites.append(pygame.image.load('3_frog.png'))
		self.sprites.append(pygame.image.load('4_frog.png'))
		self.sprites.append(pygame.image.load('5_frog.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

class GameState():
    def __init__(self):
        self.state = 'Titlecard'
    
    def Titlecard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'Svårhetsgrad'

        
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(250, 217, 500, 75), 5)
        screen.blit(text_obj,(325,225))
        screen.blit(text_obj2,(325,450)) 
        frogg.attack()
        moving_sprites.draw(screen)
        moving_sprites.update(0.06)

        pygame.display.flip()
    
    def Svårhetsgrad(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if L_button.draw(screen):
                print('START')
                self.state = 'Menu_1'
            if N_button.draw(screen):
                print('EXIT')
                self.state = 'Menu_1'
            if S_button.draw(screen):
                print('svår')
                self.state = 'Menu_1'    
        
        screen.fill((0, 0, 0))
        S_button.draw(screen)
        N_button.draw(screen)
        L_button.draw(screen)
        pygame.display.flip()
    
    def Menu_1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    frogg.attack()
                if event.key == pygame.K_SPACE:
                    self.state = 'main_game' 
    
    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                    self.state = 'main_game'  

        screen.fill((0,0,0))
        
        pygame.display.flip()
    
    def state_manager(self):
        if self.state == 'Titlecard':
            self.Titlecard()
        if self.state == 'Svårhetsgrad':
            self.Svårhetsgrad()
        if self.state == 'Menu_1':
            self.Menu_1()
        if self.state == 'main_game':
            self.main_game()

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

pygame.init()
Clock = pygame.time.Clock()
game_state = GameState()

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DÖDA GRODOR")
pygame.mouse.set_visible(True)

# TITLECARD
font_color = (255,255,255)

obj = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(250, 217, 500, 75), 5)
    
font_obj = pygame.font.Font("C:\Windows\Fonts\Bahnschrift.ttf",50)
text_obj = font_obj.render("Davids Äventyr",True,font_color)

font_obj2 = pygame.font.Font("C:\Windows\Fonts\Bahnschrift.ttf",25)
text_obj2 = font_obj2.render("Press space bar to continue",True,font_color)

#Frogg
moving_sprites = pygame.sprite.Group()
frogg = Frogg(450,153)
moving_sprites.add(frogg)

#Svårhetsgrad
font_obj3 = pygame.font.Font("C:\Windows\Fonts\Bahnschrift.ttf",45)
text_obj3 = font_obj3.render("Välj svårighetsgrad!",True,font_color)

image1 = pygame.image.load("Lätt.png").convert_alpha()
image2 = pygame.image.load("normal.png").convert_alpha()
image3 = pygame.image.load("svår.png").convert_alpha()

L_button = button.Button(100, 200, image1, 0.8)
N_button = button.Button(450, 200, image2, 0.8)
S_button = button.Button(700, 200, image3, 0.8)


while True:
    game_state.state_manager()
    Clock.tick(120)




