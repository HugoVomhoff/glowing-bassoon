import pygame

class Button():
	
	def __init__(self, x, y, image, scale):
		
		self.screen_Width, self.screen_Height = pygame.display.get_surface().get_size()
		self.scale = self.screen_Width / 1920 
		
		self.Screen_Width, self.Screen_Height = pygame.display.get_surface().get_size()
		
		self.image_Width = image.get_width() * self.scale
		self.image_Height = image.get_height() * self.scale

		self.image = pygame.transform.scale(image, (int(self.image_Width * scale), int(self.image_Height * scale)))
		
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		
	
		from skärpning import dum
		if dum != 5:
			dum += 1
		
		else:
			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
					self.clicked = True
					action = True
					dum = 0

			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action