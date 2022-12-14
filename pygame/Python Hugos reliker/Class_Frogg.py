import pygame

class Frogg(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('Bilder/1_frog.png'))
		self.sprites.append(pygame.image.load('Bilder/2_frog.png'))
		self.sprites.append(pygame.image.load('Bilder/3_frog.png'))
		self.sprites.append(pygame.image.load('Bilder/4_frog.png'))
		self.sprites.append(pygame.image.load('Bilder/5_frog.png'))
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