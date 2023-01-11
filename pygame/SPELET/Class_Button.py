import pygame

class Button():
	
	# Knappen initieras med en position, en bild och en skala på bilden
	def __init__(self, x, y, image, scale):
		
		self.screen_Width, self.screen_Height = pygame.display.get_surface().get_size()
		self.scale = self.screen_Width / 1920 
		
		self.Screen_Width, self.Screen_Height = pygame.display.get_surface().get_size()
		
		self.image_Width = image.get_width() * self.scale
		self.image_Height = image.get_height() * self.scale

		self.image = pygame.transform.scale(image, (int(self.image_Width * scale), int(self.image_Height * scale)))
		
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	# Bilden på knappen ritas ut
	def draw(self, surface):
		
		surface.blit(self.image, (self.rect.x, self.rect.y))
	
	# Om du klickar på knappen så returnas True alla andra ticks returnas False
	def clicked(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
				if event.button == 1:
					return True

		return False

	# Om du håller muspekaren över knappen så returnar funktionen hover True
	def hover(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			return True
		